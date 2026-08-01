class TaskService:
    def create_task(self,task):
        return {
            "message": "Task created successfully",
            "task": task
        }   

    def get_tasks(self):
        return {
            "message": "Tasks fetched successfully",
            "tasks": [
                {
                    "id": 1,
                    "title": "Task 1",
                    "description": "Task 1",
                    "completed": False
                },
                {
                    "id": 2,
                    "title": "Task 2",
                    "description": "Task 2",
                    "completed": False
                }
            ]
        }
    