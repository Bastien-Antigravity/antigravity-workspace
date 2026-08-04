import unittest
from unittest.mock import MagicMock, AsyncMock
import sys
from pathlib import Path
import asyncio
from fastapi import FastAPI
from fastapi.testclient import TestClient

# Resolve paths so we can import src.*
_self_dir = Path(__file__).resolve().parent.parent
if str(_self_dir) not in sys.path:
    sys.path.insert(0, str(_self_dir))

import src.bootstrap as bootstrap
from src.rest.rest_handler import SquadRESTHandler
from src.core.controller import CommandController


class TestSquadChatRESTEndpoints(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.mock_controller = MagicMock()
        self.mock_logger = MagicMock()
        self.rest_handler = SquadRESTHandler(self.mock_controller, self.mock_logger)
        
        self.app = FastAPI()
        self.rest_handler.register_routes(self.app)
        self.client = TestClient(self.app)

    def test_route_order_stream_does_not_hit_history(self):
        # Configure mock get_chat_history return
        self.mock_controller.get_chat_history = AsyncMock(return_value=[{"sender": "system", "content": "history"}])
        
        # Request stream endpoint
        response = self.client.get("/api/v1/squad/chat/stream/test_session_123")
        
        # Verify it returned event-stream content type and did NOT call get_chat_history
        self.assertEqual(response.status_code, 200)
        self.assertIn("text/event-stream", response.headers.get("content-type", ""))
        self.mock_controller.get_chat_history.assert_not_called()

    def test_get_chat_history_endpoint(self):
        self.mock_controller.get_chat_history = AsyncMock(return_value=[{"sender": "user", "content": "hello"}])
        
        response = self.client.get("/api/v1/squad/chat/test_session_123")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data.get("success"))
        self.assertEqual(len(data.get("history", [])), 1)
        self.mock_controller.get_chat_history.assert_called_once_with("test_session_123")

    def test_post_chat_message_endpoint(self):
        self.mock_controller.publish_user_message = AsyncMock()
        
        response = self.client.post("/api/v1/squad/chat/test_session_123", json={"message": "Audit code"})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data.get("success"))
        self.mock_controller.publish_user_message.assert_called_once_with("test_session_123", "Audit code")


class TestCommandControllerChatFallback(unittest.IsolatedAsyncioTestCase):
    async def test_publish_and_get_history_without_postgres(self):
        # Create controller with pool=None
        mock_config = MagicMock()
        mock_config.data = {}
        mock_logger = MagicMock()
        controller = CommandController(config=mock_config, logger=mock_logger)
        controller.pool = None
        
        # Publish user message
        await controller.publish_user_message("session_fallback", "Test fallback message")
        
        # Retrieve history
        history = await controller.get_chat_history("session_fallback")
        self.assertGreaterEqual(len(history), 1)
        self.assertEqual(history[-1]["content"], "Test fallback message")
        self.assertEqual(history[-1]["sender"], "user")


if __name__ == "__main__":
    unittest.main()
