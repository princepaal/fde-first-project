# pyrefly: ignore [missing-import]
from fastapi import FastAPI
from app.api.task import router as task_router

#create the FastAPI Application

app = FastAPI(
    title = "Task Management API",
    version = "1.0.0",
    description = "Task Management API",
)

#Attach all routes inside task.py to the application.
app.include_router(task_router)

#Home API
#FastAPI automatically converts the Python dictionary into JSON

@app.get('/')
def home():
    return{"message" : "Welcome to the Task Management API"}