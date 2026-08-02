from fastapi import APIRouter, Depends
from app.schemas.task_schema import TaskCreate
from app.services.task_service import TaskService
from app.dependencies.task_dependencies import get_task_service

router = APIRouter()

@router.get('/tasks')
def get_tasks(task_service: TaskService = Depends(get_task_service)):
    return task_service.get_tasks()

@router.get('/tasks/{task_id}')
def get_task(task_id: int, task_service: TaskService = Depends(get_task_service)):
    return {
        "id": task_id,
        "title": "Learn FastAPI",
        "description": "Learn FastAPI",
        "completed": False
    }

@router.post('/tasks')
def create_task(task: TaskCreate, task_service: TaskService = Depends(get_task_service)):
    return task_service.create_task(task)


