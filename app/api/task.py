from fastapi import APIRouter
from app.schemas.task_schema import TaskCreate
from app.services.task_service import TaskService

router = APIRouter()
task_service = TaskService()

@router.get('/tasks')
def get_tasks():
    return task_service.get_tasks()

@router.get('/tasks/{task_id}')
def get_task(task_id: int):
    return {
        "id": task_id,
        "title": "Learn FastAPI",
        "description": "Learn FastAPI",
        "completed": False
    }

@router.post('/tasks')
def create_task(task: TaskCreate):
    return task_service.create_task(task)


