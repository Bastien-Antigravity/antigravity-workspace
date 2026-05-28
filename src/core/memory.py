#!/usr/bin/env python
# coding:utf-8

import os
import sqlite3
import json
from datetime import datetime
from typing import List, Optional
from ..models.message import AgentMessage

class MemoryManager:
    """
    AI-CONTEXT: Handles persistence of agent exchanges, thoughts, and words.
    Uses a local SQLite database for reliability and portability.
    """
    def __init__(self, vault_root: str):
        self.db_path = os.path.join(vault_root, "00-AI-Orchestration", "logs", "squad_memory.sqlite")
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        self._init_db()

    def _init_db(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS sessions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    start_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    mode TEXT,
                    client TEXT
                )
            """)
            conn.execute("""
                CREATE TABLE IF NOT EXISTS messages (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    session_id INTEGER,
                    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    role TEXT,
                    content TEXT,
                    thought TEXT,
                    tool_calls TEXT,
                    FOREIGN KEY(session_id) REFERENCES sessions(id)
                )
            """)

    def create_session(self, mode: str, client: str) -> int:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute(
                "INSERT INTO sessions (mode, client) VALUES (?, ?)",
                (mode, client)
            )
            return cursor.lastrowid

    def store_message(self, session_id: int, msg: AgentMessage):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(
                "INSERT INTO messages (session_id, role, content, thought, tool_calls) VALUES (?, ?, ?, ?, ?)",
                (
                    session_id,
                    msg.role,
                    msg.content,
                    msg.thought,
                    json.dumps(msg.tool_calls) if msg.tool_calls else None
                )
            )

    def get_session_history(self, session_id: int) -> List[AgentMessage]:
        messages = []
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute(
                "SELECT role, content, thought, tool_calls FROM messages WHERE session_id = ? ORDER BY timestamp ASC",
                (session_id,)
            )
            for row in cursor:
                messages.append(AgentMessage(
                    role=row[0],
                    content=row[1],
                    thought=row[2],
                    tool_calls=json.loads(row[3]) if row[3] else []
                ))
        return messages
