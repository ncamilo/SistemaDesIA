from collections.abc import Iterator, Sequence
from typing import Annotated

from fastapi import APIRouter, Depends, Request, Response

from app.models import Task
from app.repositories import Repository
from app.schemas import (
    ErrorResponse,
    ProjectCreate,
    ProjectRead,
    ProjectUpdate,
    Status,
    TaskCreate,
    TaskRead,
    TaskUpdate,
)
from app.services import Service, project_view

router = APIRouter(prefix="/api")


def get_service(request: Request) -> Iterator[Service]:
    with request.app.state.session_factory() as session:
        yield Service(Repository(session))


ServiceDep = Annotated[Service, Depends(get_service)]


@router.get("/projects", response_model=list[ProjectRead])
def list_projects(service: ServiceDep) -> list[ProjectRead]:
    return [project_view(p) for p in service.repo.projects()]


@router.post("/projects", response_model=ProjectRead, status_code=201)
def create_project(data: ProjectCreate, service: ServiceDep) -> ProjectRead:
    return project_view(service.create_project(data))


@router.get(
    "/projects/{project_id}", response_model=ProjectRead, responses={404: {"model": ErrorResponse}}
)
def get_project(project_id: int, service: ServiceDep) -> ProjectRead:
    return project_view(service.project(project_id))


@router.patch(
    "/projects/{project_id}", response_model=ProjectRead, responses={404: {"model": ErrorResponse}}
)
def update_project(project_id: int, data: ProjectUpdate, service: ServiceDep) -> ProjectRead:
    return project_view(service.update_project(project_id, data))


@router.delete(
    "/projects/{project_id}",
    status_code=204,
    responses={404: {"model": ErrorResponse}, 409: {"model": ErrorResponse}},
)
def delete_project(project_id: int, service: ServiceDep) -> Response:
    service.delete_project(project_id)
    return Response(status_code=204)


@router.get(
    "/projects/{project_id}/tasks",
    response_model=list[TaskRead],
    responses={404: {"model": ErrorResponse}},
)
def list_tasks(
    project_id: int, service: ServiceDep, status: Status | None = None
) -> Sequence[Task]:
    service.project(project_id)
    return service.repo.tasks(project_id, status)


@router.post(
    "/projects/{project_id}/tasks",
    response_model=TaskRead,
    status_code=201,
    responses={404: {"model": ErrorResponse}},
)
def create_task(project_id: int, data: TaskCreate, service: ServiceDep) -> Task:
    return service.create_task(project_id, data)


@router.patch(
    "/tasks/{task_id}", response_model=TaskRead, responses={404: {"model": ErrorResponse}}
)
def update_task(task_id: int, data: TaskUpdate, service: ServiceDep) -> Task:
    return service.update_task(task_id, data)


@router.delete("/tasks/{task_id}", status_code=204, responses={404: {"model": ErrorResponse}})
def delete_task(task_id: int, service: ServiceDep) -> Response:
    service.delete_task(task_id)
    return Response(status_code=204)
