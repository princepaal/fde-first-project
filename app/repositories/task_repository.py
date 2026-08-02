
class TaskRepository:

    def get_tasks(self):
        return [
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

    def create_task(self, task):
        return task