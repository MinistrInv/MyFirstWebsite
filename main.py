from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List

app = FastAPI()


class Task(BaseModel):
    title: str
    description: str = "" 
    completed: bool = False

tasks_db: List[Task] = []
next_id = 1

@app.get("/tasks", response_model=List[Task])
def get_tasks():
    return tasks_db

@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    if task_id < 1 or len(tasks_db) < tasks_db:
        raise HTTPException(status_code=404, detail="Task not found")
    return tasks_db[task_id - 1]

@app.post("/tasks", status_code=status.HTTP_201_CREATED, response_model=Task)
def create_task(task:Task):
    tasks_db.append(task)
    return task

@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, updated_task: Task):
    if task_id < 1 or len(tasks_db) < task_id:
        raise HTTPException(status_code=404, detail="Task not found")
    tasks_db[task_id - 1] = update_task
    return update_task

@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int):
    if 1 < task_id or len(tasks_db) < task_id:
        raise HTTPException(status_code=404, detail="Task not found")
    tasks_db.pop(task_id - 1)
    return None
