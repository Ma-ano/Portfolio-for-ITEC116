# Laboratory Activity #4: Advanced API Implementation

This activity involves implementing versioning, authentication, and proper HTTP exception handling in a FastAPI application. The API manages a to-do list with two versions (`apiv1` and `apiv2`) and requires an API key for access.

## Features
- **Versioning**: Two versions of the API (`apiv1` and `apiv2`) with identical functionality.
- **Authentication**: API key validation via headers or query parameters.
- **HTTP Exception Handling**: Proper status codes for success and error responses.
- **Environment Variables**: Secure storage of the API key using a `.env` file.

## Endpoints

### Version 1 (`apiv1`)
- **GET /apiv1/database/{task_id}**: Retrieve a task by its ID.
- **POST /apiv1/database**: Create a new task.
- **PATCH /apiv1/database/{task_id}**: Update an existing task.
- **DELETE /apiv1/database/{task_id}**: Delete a task by its ID.

### Version 2 (`apiv2`)
- **GET /apiv2/database/{task_id}**: Retrieve a task by its ID.
- **POST /apiv2/database**: Create a new task.
- **PATCH /apiv2/database/{task_id}**: Update an existing task.
- **DELETE /apiv2/database/{task_id}**: Delete a task by its ID.

### General Endpoints
- **GET /**: Welcome message.
- **GET /health**: Health check endpoint.

## Example Usage
- **Create a Task**:
  - Request: `POST /apiv1/database`
    ```json
    {
      "task_title": "New Task",
      "task_desc": "This is a new task.",
      "is_finished": false
    }
    ```
  - Response:
    ```json
    {
      "message": "Task successfully created.",
      "task": {
        "task_id": 2,
        "task_title": "New Task",
        "task_desc": "This is a new task.",
        "is_finished": false
      }
    }
    ```

- **Retrieve a Task**:
  - Request: `GET /apiv1/database/1`
  - Response:
    ```json
    {
      "task_id": 1,
      "task_title": "Laboratory Activity",
      "task_desc": "Create Lab Act 2",
      "is_finished": false
    }
    ```

## Requirements
- Python 3.7+
- FastAPI (`pip install fastapi`)
- Uvicorn (`pip install uvicorn`)
- Python-dotenv (`pip install python-dotenv`)

## Running the Application
1. Create a `.env` file with the following content:
   ```text
   LAB4_API_KEY=RawrBarney