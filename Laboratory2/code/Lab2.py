from fastapi import FastAPI, HTTPException
from typing import Optional

app = FastAPI()

task_db = [
    {"task_id": 1, "task_title": "Laboratory Activity", "task_desc": "Create Lab Act 2", "is_finished": False}
]
@app.get("/database/{task_id}")
def get_task(task_id: int):
    task = next((task for task in task_db if task["task_id"] == task_id), None)
    if not task:
        raise HTTPException(status_code=404, detail=f"Task with ID {task_id} not found.")
    return task

@app.post("/database")
def create_task(task_title: str, task_desc: Optional[str] = "", is_finished: bool = False):
    task_id = len(task_db) + 1
    task = {"task_id": task_id, "task_title": task_title, "task_desc": task_desc, "is_finished": is_finished}
    task_db.append(task)
    return {"message": "Task successfully created.", "task": task}

@app.patch("/database/{task_id}")
def update_task(task_id: int, task_title: Optional[str] = None, task_desc: Optional[str] = None, is_finished: Optional[bool] = None):
    task = next((task for task in task_db if task["task_id"] == task_id), None)
    if not task:
        raise HTTPException(status_code=404, detail=f"Task with ID {task_id} not found.")

    if task_title: task["task_title"] = task_title
    if task_desc: task["task_desc"] = task_desc
    if is_finished is not None: task["is_finished"] = is_finished
    
    return {"message": "Task successfully updated.", "task": task}

@app.delete("/database/{task_id}")
def delete_task(task_id: int):
    task = next((task for task in task_db if task["task_id"] == task_id), None)
    if not task:
        raise HTTPException(status_code=404, detail=f"Task with ID {task_id} not found.")
    
    task_db.remove(task)
    return {"message": "Task successfully deleted."}

@app.put("/database/{task_id}")
def replace_task(task_id: int, task_title: str, task_desc: Optional[str] = "", is_finished: bool = False):
    task = next((task for task in task_db if task["task_id"] == task_id), None)
    if not task:
        raise HTTPException(status_code=404, detail=f"Task with ID {task_id} not found.")
    
    task.update({"task_title": task_title, "task_desc": task_desc, "is_finished": is_finished})
    return {"message": "Task successfully replaced.", "task": task}