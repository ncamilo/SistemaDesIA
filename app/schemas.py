from datetime import datetime
from enum import StrEnum
from typing import Annotated

from pydantic import BaseModel, ConfigDict, StringConstraints, model_validator

Title = Annotated[str, StringConstraints(strip_whitespace=True, min_length=1, max_length=120)]
Description = Annotated[str, StringConstraints(strip_whitespace=True, max_length=2000)]
Reference = Annotated[str, StringConstraints(strip_whitespace=True, max_length=80)]


class Status(StrEnum):
    pending = "pending"
    in_progress = "in_progress"
    done = "done"


class InputModel(BaseModel):
    model_config = ConfigDict(extra="forbid")


class ProjectCreate(InputModel):
    title: Title
    customer: Title
    order_reference: Reference = ""
    description: Description = ""


class PatchModel(InputModel):
    @model_validator(mode="before")
    @classmethod
    def reject_nulls_and_empty(cls, value):
        if isinstance(value, dict) and (not value or any(v is None for v in value.values())):
            raise ValueError("Informe pelo menos um campo, sem valores nulos.")
        return value


class ProjectUpdate(PatchModel):
    title: Title | None = None
    customer: Title | None = None
    order_reference: Reference | None = None
    description: Description | None = None


class ProjectRead(ProjectCreate):
    id: int
    created_at: datetime
    status: Status
    total_tasks: int
    completed_tasks: int
    progress: int


class TaskCreate(InputModel):
    title: Title
    description: Description = ""


class TaskUpdate(PatchModel):
    title: Title | None = None
    description: Description | None = None
    status: Status | None = None


class TaskRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    project_id: int
    title: str
    description: str
    status: Status
    created_at: datetime
