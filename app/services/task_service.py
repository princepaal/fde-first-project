from app.repositories.task_repository import TaskRepository

class TaskService:
    def __init__(self, repository: TaskRepository):
        self.repository = repository

    def get_tasks(self):
        return self.repository.get_tasks()

    def create_task(self, task):
        created_task = self.repository.create_task(task)
        return {
            "message": "Task created successfully",
            "task": created_task
        }  