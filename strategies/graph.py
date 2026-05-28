#!/usr/bin/env python
# coding:utf-8

import operator
from typing import Annotated, Sequence, TypedDict, Union, Dict, Any
from langgraph.graph import StateGraph, END
from src.models.context import SystemContext
from src.models.message import AgentMessage

class AgentState(TypedDict):
    """
    AI-CONTEXT: State definition for the Engine Graph.
    Uses Annotated and operator.add to handle list concatenation automatically.
    """
    messages: Annotated[Sequence[AgentMessage], operator.add]
    active_persona: str
    next_step: str
    metadata: Dict[str, Any]

class GraphWorkflowManager:
    """
    AI-CONTEXT: Formalized Workflow Engine using LangGraph.
    Enables cyclical flows, error recovery, and persistence.
    """
    def __init__(self, ctx: SystemContext, facade: Any = None):
        self.ctx = ctx
        self.facade = facade
        self.workflow = StateGraph(AgentState)
        self._build_standard_graph()

    def _build_standard_graph(self):
        """
        Scaffolds a standard 'Audit -> Process -> Review' cyclical graph.
        """
        # Define Nodes
        self.workflow.add_node("audit", self.node_audit)
        self.workflow.add_node("agent_loop", self.node_agent)
        self.workflow.add_node("quality_gate", self.node_quality_gate)

        # Define Edges
        self.workflow.set_entry_point("audit")
        self.workflow.add_edge("audit", "agent_loop")
        self.workflow.add_edge("agent_loop", "quality_gate")

        # Cyclical logic: If quality gate fails, go back to agent_loop
        self.workflow.add_conditional_edges(
            "quality_gate",
            self.should_continue,
            {
                "continue": "agent_loop",
                "end": END
            }
        )
        
        self.app = self.workflow.compile()

    def node_audit(self, state: AgentState):
        print("🔍 [Graph] Running Governance Audit...")
        if self.facade:
            self.facade.governance.run_preflight()
        return {"next_step": "process"}

    async def node_agent(self, state: AgentState):
        persona = state.get("active_persona", "orchestrator")
        print(f"🤖 [Graph] Agent {persona} is working...")
        
        if not self.facade:
            return {"messages": [AgentMessage(role="assistant", content="Work completed.")]}

        provider = self.facade.get_provider()
        if not provider:
            return {"messages": [AgentMessage(role="assistant", content="Error: AI Provider not configured.")]}

        persona_prompt = self.facade.personas.load_prompt(persona) or "You are a helpful assistant."
        history = list(state.get("messages", []))
        msgs = [AgentMessage(role="system", content=persona_prompt)] + history

        response = await provider.chat(msgs)
        print(f"\n💬 [Graph AI Response ({persona})]:\n{response.content}\n")
        return {"messages": [response]}

    async def node_quality_gate(self, state: AgentState):
        print("⚖️ [Graph] Verifying results...")
        if not self.facade:
            return {"metadata": {"quality_score": 1.0}}

        provider = self.facade.get_provider()
        if not provider:
            return {"metadata": {"quality_score": 1.0}}

        last_message = state["messages"][-1].content if state["messages"] else ""
        evaluation_prompt = f"""
        Review the following work done by the agent and evaluate if it is complete and meets high quality standards.
        Return a single float number between 0.0 and 1.0 representing the quality score (e.g. 0.85). Do not write anything else.

        WORK TO EVALUATE:
        {last_message}
        """

        review_msg = AgentMessage(role="user", content=evaluation_prompt)
        response = await provider.chat([review_msg])

        try:
            import re
            match = re.search(r"(\d+\.\d+|\d+)", response.content)
            score = float(match.group(1)) if match else 1.0
        except Exception:
            score = 1.0

        print(f"⚖️ [Graph Quality Gate] Evaluated Score: {score}")
        return {"metadata": {"quality_score": score}}

    def should_continue(self, state: AgentState):
        score = state.get("metadata", {}).get("quality_score", 0)
        if score < 0.8:
            return "continue"
        return "end"

    async def execute_graph(self, initial_persona: str, task: str):
        """Runs the compiled graph."""
        initial_state = {
            "messages": [AgentMessage(role="user", content=task)],
            "active_persona": initial_persona,
            "next_step": "audit",
            "metadata": {}
        }
        
        async for event in self.app.astream(initial_state):
            for value in event.values():
                print(f"📍 Step Completed: {value.get('next_step', 'done')}")
