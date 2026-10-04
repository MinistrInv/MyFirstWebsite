from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Привет, Хантатон!"}

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id, "name": f"Пользователь {user_id}"}

@app.get("/search")
def search(q: str = "", limit: int = 10):
    return {"query": q, "limit": limit}

class Task(BaseModel):
    title: str
    dicription: str = ""
    completed: bool = False

@app.post("/tasks")
def create_task(task: Task):
    return {"message": "Задача создана", "task": task}

