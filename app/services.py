from app.models import Project, Task
from app.repositories import Repository
from app.schemas import ProjectRead, Status


class NotFound(Exception):
    pass


class Conflict(Exception):
    pass


def summarize(statuses: list[str]) -> dict:
    total = len(statuses)
    completed = statuses.count(Status.done)
    status = Status.pending
    if total and completed == total:
        status = Status.done
    elif any(s != Status.pending for s in statuses):
        status = Status.in_progress
    return {
        "status": status,
        "total_tasks": total,
        "completed_tasks": completed,
        "progress": completed * 100 // total if total else 0,
    }


def project_view(project: Project):
    return ProjectRead(
        id=project.id,
        title=project.title,
        customer=project.customer,
        order_reference=project.order_reference,
        description=project.description,
        created_at=project.created_at,
        **summarize([t.status for t in project.tasks]),
    )


class Service:
    def __init__(self, repository: Repository):
        self.repo = repository

    def project(self, project_id):
        project = self.repo.project(project_id)
        if project is None:
            raise NotFound("Projeto não encontrado.")
        return project

    def task(self, task_id):
        task = self.repo.task(task_id)
        if task is None:
            raise NotFound("Tarefa não encontrada.")
        return task

    def create_project(self, data):
        return self.repo.save(Project(**data.model_dump()))

    def update_project(self, project_id, data):
        project = self.project(project_id)
        for key, value in data.model_dump(exclude_unset=True).items():
            setattr(project, key, value)
        return self.repo.save(project)

    def delete_project(self, project_id):
        project = self.project(project_id)
        if project.tasks:
            raise Conflict("Remova as tarefas antes de excluir o projeto.")
        self.repo.delete(project)

    def create_task(self, project_id, data):
        self.project(project_id)
        return self.repo.save(Task(project_id=project_id, **data.model_dump()))

    def update_task(self, task_id, data):
        task = self.task(task_id)
        for key, value in data.model_dump(exclude_unset=True).items():
            setattr(task, key, value)
        return self.repo.save(task)

    def delete_task(self, task_id):
        self.repo.delete(self.task(task_id))
