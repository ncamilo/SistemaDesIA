import pytest

from app.services import summarize


@pytest.mark.parametrize(
    "statuses, status, done, progress",
    [
        ([], "pending", 0, 0),
        (["pending", "pending"], "pending", 0, 0),
        (["in_progress"], "in_progress", 0, 0),
        (["done", "pending"], "in_progress", 1, 50),
        (["done", "pending", "pending"], "in_progress", 1, 33),
        (["done", "done"], "done", 2, 100),
    ],
)
def test_project_progress(statuses, status, done, progress):
    assert summarize(statuses) == {
        "status": status,
        "total_tasks": len(statuses),
        "completed_tasks": done,
        "progress": progress,
    }
