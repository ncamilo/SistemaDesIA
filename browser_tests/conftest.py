import os
import socket
import threading
import time

import pytest
import uvicorn
from playwright.sync_api import sync_playwright

from app.main import create_app


@pytest.fixture
def live_url(tmp_path):
    """Run the real app against a disposable database, never the user's data."""
    app = create_app(f"sqlite:///{tmp_path / 'browser.db'}")
    sock = socket.socket()
    sock.bind(("127.0.0.1", 0))
    port = sock.getsockname()[1]
    server = uvicorn.Server(uvicorn.Config(app, log_level="error"))
    thread = threading.Thread(target=server.run, kwargs={"sockets": [sock]}, daemon=True)
    thread.start()
    try:
        deadline = time.monotonic() + 10
        while not server.started:
            if not thread.is_alive() or time.monotonic() > deadline:
                pytest.fail("O servidor isolado não iniciou.")
            time.sleep(0.01)
        yield f"http://127.0.0.1:{port}"
    finally:
        server.should_exit = True
        thread.join(timeout=10)
        sock.close()


@pytest.fixture
def page():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(channel=os.getenv("PLAYWRIGHT_CHANNEL") or None)
        page = browser.new_page()
        yield page
        browser.close()
