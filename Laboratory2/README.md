# Laboratory Activity 2: Working with HTTP actions and API parameters

This is a CRUD (Create, Read, Update, Delete) API for managing tasks in a to-do list. The API allows users to create, retrieve, update, and delete tasks using FastAPI.

---

## Features
- **Endpoints**:
  - `GET /database/{task_id}`: Retrieve a task by its ID.
  - `POST /database`: Create a new task.
  - `PATCH /database/{task_id}`: Update an existing task.
  - `DELETE /database/{task_id}`: Delete a task by its ID.
  - `PUT /database/{task_id}`: Replace an existing task.

---

## Example Usage

### Retrieve a Task
- **Request**: `GET /database/1`
- **Response**:
  ```json
  {
    "task_id": 1,
    "task_title": "Laboratory Activity",
    "task_desc": "Create Lab Act 2",
    "is_finished": false
  }