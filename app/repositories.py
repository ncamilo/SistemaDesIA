from collections.abc import Sequence
from typing import TypeVar

from sqlalchemy import select
from sqlalchemy.orm import Session, selectinload

from app.models import Project, Task

Entity = TypeVar("Entity", Project, Task)


class Repository:
    def __init__(self, session: Session) -> None:
        self.session = session

    def projects(self) -> Sequence[Project]:
        return self.session.scalars(
            select(Project).options(selectinload(Project.tasks)).order_by(Project.id.desc())
        ).all()

    def project(self, project_id: int) -> Project | None:
        return self.session.get(Project, project_id)

    def task(self, task_id: int) -> Task | None:
        return self.session.get(Task, task_id)

    def tasks(self, project_id: int, status: str | None = None) -> Sequence[Task]:
        query = select(Task).where(Task.project_id == project_id).order_by(Task.id)
        if status is not None:
            query = query.where(Task.status == status)
        return self.session.scalars(query).all()

    def save(self, entity: Entity) -> Entity:
        self.session.add(entity)
        self.session.commit()
        self.session.refresh(entity)
        return entity

    def delete(self, entity: Project | Task) -> None:
        self.session.delete(entity)
        self.session.commit()
