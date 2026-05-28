#!/usr/bin/env python
# coding:utf-8

import operator
from typing import Annotated, Sequence, TypedDict, Union, Dict, Any
from langgraph.graph import StateGraph, END
from ..models.context import SystemContext
from ..models.message import AgentMessage

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
    def __init__(self, ctx: SystemContext):
        self.ctx = ctx
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
        # GovernanceManager call would go here
        return {"next_step": "process"}

    def node_agent(self, state: AgentState):
        print(f"🤖 [Graph] Agent {state['active_persona']} is working...")
        # SDK Provider call would go here
        return {"messages": [AgentMessage(role="assistant", content="Work completed.")]}

    def node_quality_gate(self, state: AgentState):
        print("⚖️ [Graph] Verifying results...")
        return {"metadata": {"quality_score": 1.0}}

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
