# pyrefly: ignore [missing-import]
from fastapi import FastAPI

#create the FastAPI Application

app = FastAPI(
    title = "Task Management API",
    version = "1.0.0",
    description = "Task Management API",
)

#Home API
#FastAPI automatically converts the Python dictionary into JSON

@app.get('/')
def home():
    return{"message" : "Welcome to the Task Management API"}