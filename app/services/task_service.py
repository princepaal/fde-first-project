from app.repositories.task_repository import TaskRepository

task_repository = TaskRepository()

class TaskService:
    def create_task(self,task):
        created_task =  task_repository.create_task(task)
        return {
            "message": "Task Created Successfully",
            "task": created_task
        }   

    def get_tasks(self):
        return task_repository.get_tasks()