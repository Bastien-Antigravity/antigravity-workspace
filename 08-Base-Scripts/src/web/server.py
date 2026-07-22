#!/usr/bin/env python
# coding:utf-8

"""
ESSENTIAL PROCESS:
FastAPI Web Server for Squad Control Dashboard and MFE registration.
Serves static MFE assets and handles REST API queries.
"""

import sys
import json
import time
import urllib.request
import threading
from pathlib import Path
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI(title="Squad Control Web Server")

# Add CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origin_regex="https?://.*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files (MFE script)
_STATIC_DIR = Path(__file__).parent / "static"
_STATIC_DIR.mkdir(parents=True, exist_ok=True)
app.mount("/static", StaticFiles(directory=str(_STATIC_DIR)), name="static")

# Helper to load routes dynamically
def init_routes(controller, logger):
    from src.rest.rest_handler import SquadRESTHandler
    rest_handler = SquadRESTHandler(controller, logger)
    rest_handler.register_routes(app)

def register_mfe_with_web_interface(config, logger, bs_ip, bs_port):
    """
    Auto-registration daemon that POSTs our MFE definition to the central web-interface.
    """
    time.sleep(2)  # Wait for server to boot

    # Resolve web_interface address from config
    web_ip = "127.0.0.1"
    web_port = 8000
    if config and hasattr(config, "data") and isinstance(config.data, dict):
        try:
            web_cap = config.data.get("capabilities", {}).get("web_interface", {})
            web_ip = web_cap.get("ip", "127.0.0.1")
            web_port = int(web_cap.get("port", 8000))
        except Exception:
            pass

    reg_url = f"http://{web_ip}:{web_port}/api/v1/register"
    mfe_url = f"http://{bs_ip}:{bs_port}/static/mfe.js"
    
    payload = {
        "name": "base-scripts",
        "tag": "base-scripts-mfe",
        "url": mfe_url,
        "navTitle": "🚀 Squad Control"
    }
    
    req_data = json.dumps(payload).encode("utf-8")
    
    logger.info(f"OpenMFE: Starting base-scripts auto-registration loop to {reg_url}")
    for i in range(15):
        try:
            req = urllib.request.Request(
                reg_url, 
                data=req_data, 
                headers={"Content-Type": "application/json"},
                method="POST"
            )
            with urllib.request.urlopen(req, timeout=3) as resp:
                status = resp.status
                if 200 <= status < 300:
                    logger.info(f"OpenMFE: Successfully registered base-scripts MFE at {reg_url}")
                    return
                else:
                    logger.warning(f"OpenMFE: Registration attempt {i+1} failed with status {status}")
        except Exception as e:
            logger.warning(f"OpenMFE: Registration attempt {i+1} failed: {e}")
        time.sleep(3)
    logger.warning("OpenMFE: Failed to register base-scripts MFE after 15 attempts")

def start_async_server(controller, config, logger, host, port):
    """Launches the uvicorn web server and starts the auto-registration daemon thread."""
    init_routes(controller, logger)
    
    # Spawn registration thread
    t = threading.Thread(
        target=register_mfe_with_web_interface,
        args=(config, logger, host, port),
        daemon=True
    )
    t.start()

    logger.info(f"Starting Squad Control FastAPI server on http://{host}:{port}...")
    
    # Run uvicorn in a non-blocking background task or thread-safe runner
    # We will pass loop or run synchronously depending on how uvicorn is called.
    config_uv = uvicorn.Config(app, host=host, port=port, log_level="warning")
    server = uvicorn.Server(config_uv)
    
    # We return the server so it can be run or shut down
    return server
