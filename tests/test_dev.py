from unittest.mock import Mock

import pytest

from scripts import dev


def test_install_rejects_incomplete_environment(tmp_path, monkeypatch):
    environment = tmp_path / ".venv"
    environment.mkdir()
    leftover = environment / "old-package.txt"
    leftover.write_text("preserve")
    monkeypatch.setattr(dev, "ROOT", tmp_path)
    monkeypatch.setattr(dev, "PYTHON", environment / "missing-python")
    monkeypatch.setattr(dev.sys, "argv", ["dev.py", "install"])
    run = Mock()
    monkeypatch.setattr(dev.subprocess, "run", run)
    with pytest.raises(SystemExit) as error:
        dev.main()
    assert error.value.code == 2
    run.assert_not_called()
    assert leftover.read_text() == "preserve"


def test_install_rejects_different_environment_version(tmp_path, monkeypatch):
    environment = tmp_path / ".venv"
    environment.mkdir()
    interpreter = environment / "python"
    interpreter.touch()
    monkeypatch.setattr(dev, "ROOT", tmp_path)
    monkeypatch.setattr(dev, "PYTHON", interpreter)
    monkeypatch.setattr(dev.sys, "argv", ["dev.py", "install"])
    monkeypatch.setattr(dev.subprocess, "check_output", lambda *args, **kwargs: "3.14\n")
    run = Mock()
    monkeypatch.setattr(dev.subprocess, "run", run)
    with pytest.raises(SystemExit) as error:
        dev.main()
    assert error.value.code == 2
    run.assert_not_called()
