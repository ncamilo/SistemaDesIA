from sqlalchemy import select
from sqlalchemy.orm import Session, selectinload

from app.models import Project, Task


class Repository:
    def __init__(self, session: Session):
        self.session = session

    def projects(self):
        return self.session.scalars(
            select(Project).options(selectinload(Project.tasks)).order_by(Project.id.desc())
        ).all()

    def project(self, project_id):
        return self.session.get(Project, project_id)

    def task(self, task_id):
        return self.session.get(Task, task_id)

    def tasks(self, project_id, status=None):
        query = select(Task).where(Task.project_id == project_id).order_by(Task.id)
        if status is not None:
            query = query.where(Task.status == status)
        return self.session.scalars(query).all()

    def save(self, entity):
        self.session.add(entity)
        self.session.commit()
        self.session.refresh(entity)
        return entity

    def delete(self, entity):
        self.session.delete(entity)
        self.session.commit()
