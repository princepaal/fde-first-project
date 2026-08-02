from app.repositories.task_repository import TaskRepository
from app.services.task_service import TaskService

#create instance of TaskRepository
def get_task_repository():
    return TaskRepository()

#create instance of TaskService and inject TaskRepository dependency
def get_task_service():
    repository = get_task_repository()
    return TaskService(repository)

#FastAPI will automatically call this function to get an instance of TaskService
#and will inject it into the route handler.
