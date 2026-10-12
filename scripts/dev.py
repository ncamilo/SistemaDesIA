"""Comandos locais portáveis; executar pelos wrappers Windows/macOS."""

import argparse
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PYTHON = ROOT / ".venv" / ("Scripts/python.exe" if os.name == "nt" else "bin/python")


def run(*args: str) -> None:
    subprocess.run([str(PYTHON), *args], cwd=ROOT, check=True)


def main() -> None:
    parser = argparse.ArgumentParser(description="Automação do MVP de montagem")
    parser.add_argument(
        "command",
        choices=[
            "install",
            "run",
            "demo",
            "test",
            "check",
            "format",
            "browser-install",
            "browser-test",
        ],
    )
    command = parser.parse_args().command
    if sys.version_info[:2] != (3, 14):
        parser.error("Use Python 3.14, conforme o ambiente validado do projeto.")
    if command == "install":
        if not PYTHON.exists():
            subprocess.run([sys.executable, "-m", "venv", str(ROOT / ".venv")], check=True)
        run("-m", "pip", "install", "-r", "requirements.txt")
        run("-m", "pip", "check")
        return
    if not PYTHON.exists():
        parser.error("Ambiente ausente. Execute install primeiro.")
    if command in ("run", "demo"):
        port = "8000"
        if command == "demo":
            # Demo stays separate from the user's montagem.db, even with DATABASE_URL set.
            os.environ["DATABASE_URL"] = "sqlite:///./demo.db"
            port = "8001"
        run("-m", "uvicorn", "app.main:app", "--host", "127.0.0.1", "--port", port)
    elif command == "test":
        run("-m", "pytest", "-q")
    elif command == "check":
        run("-m", "ruff", "check", "app", "tests", "browser_tests", "scripts")
        run("-m", "ruff", "format", "--check", "app", "tests", "browser_tests", "scripts")
        run("-m", "pip", "check")
    elif command == "format":
        run("-m", "ruff", "format", "app", "tests", "browser_tests", "scripts")
    elif command == "browser-install":
        run("-m", "pip", "install", "-r", "requirements-browser.txt")
        run("-m", "playwright", "install", "chromium")
    elif command == "browser-test":
        run("-m", "pytest", "browser_tests", "-q")


if __name__ == "__main__":
    try:
        main()
    except subprocess.CalledProcessError as error:
        sys.exit(error.returncode)
    except KeyboardInterrupt:
        sys.exit(130)
