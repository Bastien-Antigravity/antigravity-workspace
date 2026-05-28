#!/usr/bin/env python
# coding:utf-8
"""
🧠 KNOWLEDGE COMPRESSOR (Context Distiller)
Automates the distillation of session logs into 'Fresh Patterns' to keep context clean.
Parses AI-Session-State.md and generates candidate entries for Knowledge-Strategy.md.
"""
import os
import re
import sys
import argparse
from datetime import datetime
from pathlib import Path

# Standardize terminal output encoding for Windows
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except (AttributeError, Exception):
        pass

class KnowledgeCompressor:
    def __init__(self, vault_root: Path):
        self.vault_root = vault_root
        self.session_state_file = vault_root / "AI-Session-State.md"
        self.strategy_file = vault_root / "00-AI-Orchestration" / "Knowledge-Strategy.md"
        self.output_dir = vault_root / "00-AI-Orchestration" / "logs" / "distillations"
        os.makedirs(self.output_dir, exist_ok=True)

    def extract_recent_sessions(self, count=3):
        """Extracts the last N sessions from AI-Session-State.md."""
        if not self.session_state_file.exists():
            print(f"❌ Error: {self.session_state_file} not found.")
            return []

        with open(self.session_state_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Split by H2 headers (Sessions)
        sessions = re.split(r'^##\s+', content, flags=re.MULTILINE)
        # First part is frontmatter/preamble
        if not sessions:
            return []
            
        return [s.strip() for s in sessions[1:count+1]]

    def distill_to_pattern(self, session_text):
        """
        Logic to format a session log into a Decision Pattern.
        In a full implementation, this would call an LLM.
        For now, it provides a structured template based on the session log.
        """
        lines = session_text.split('\n')
        title_line = lines[0] if lines else "Unknown Session"
        
        # Try to extract a meaningful title from the first bullet or the header
        pattern_title = title_line.replace("📡 ", "").split("(")[0].strip()
        
        # Simple extraction of 'Decision' and 'Impact' from bullets
        actions = []
        for line in lines[1:]:
            clean = line.strip()
            if clean.startswith("- "):
                actions.append(clean[2:])

        distillation = [
            f"### [Candidate Pattern] {pattern_title}",
            f"**Distilled from**: {title_line}",
            f"**Context**: Derived from recent session orchestration.",
            f"**Decision**: ",
        ]
        
        for action in actions:
            distillation.append(f"- {action}")
            
        distillation.append(f"**Impact**: Improved fleet synchronization and governance alignment.")
        distillation.append("")
        
        return "\n".join(distillation)

    def run(self, count=1):
        print(f"🔍 Scanning {self.session_state_file.name} for recent wisdom...")
        sessions = self.extract_recent_sessions(count)
        
        if not sessions:
            print("✨ No sessions found to distill.")
            return

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_file = self.output_dir / f"distillation_{timestamp}.md"
        
        candidates = []
        for s in sessions:
            candidates.append(self.distill_to_pattern(s))
            
        report_content = [
            f"# 🧠 Knowledge Distillation Report",
            f"*Generated: {datetime.now().isoformat()}*",
            f"",
            "> [!TIP]",
            "> Review these candidates and append the verified ones to `00-AI-Orchestration/Knowledge-Strategy.md` Section 5.",
            "",
            "## 💎 Pattern Candidates",
            "",
            "\n".join(candidates)
        ]
        
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write("\n".join(report_content))
            
        print(f"✅ Distillation complete! Review candidates in: {report_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Knowledge Compressor - Session Log Distiller")
    parser.add_argument("--count", "-c", type=int, default=1, help="Number of recent sessions to distill")
    args = parser.parse_args()

    # Find vault root (obsidian-brain)
    script_dir = Path(__file__).resolve().parent
    vault_root = script_dir.parent
    
    compressor = KnowledgeCompressor(vault_root)
    compressor.run(count=args.count)
