from fastapi import APIRouter

from app import crud
from app.models import Task

router = APIRouter(prefix="/tasks", tags=["Tasks"])


@router.post("/")
def create(task: Task):
    task_id = crud.create_task(task)
    return {"id": task_id, "message": "Task created"}


@router.get("/")
def read_all():
    tasks = crud.get_tasks()
    return tasks


@router.put("/{task_id}")
def update(task_id: int, task: Task):
    crud.update_task(task_id, task)
    return {"message": "Task updated"}


@router.delete("/{task_id}")
def delete(task_id: int):
    crud.delete_task(task_id)
    return {"message": "Task deleted"}
