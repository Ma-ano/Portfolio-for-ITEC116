# Laboratory Activity # 5: Deploying API in Cloud

This activity involves deploying the API developed in **Laboratory Activity 4** to the cloud platform **Render**. The API manages a to-do list with versioning (`apiv1` and `apiv2`) and requires an API key for access.

---

## Objectives
- Develop and deploy an API to a cloud platform (Render).
- Ensure the deployed API is accessible via a public URL.

---

## Features
- **Versioning**: Two versions of the API (`apiv1` and `apiv2`) with identical functionality.
- **Authentication**: API key validation via headers or query parameters.
- **HTTP Exception Handling**: Proper status codes for success and error responses.
- **Environment Variables**: Secure storage of the API key using Render's environment variables.

---

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

---

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

---

## Requirements
- Python 3.7+
- FastAPI (`pip install fastapi`)
- Uvicorn (`pip install uvicorn`)
- Python-dotenv (`pip install python-dotenv`)

---

## Deployment to Render

### Step 1: Prepare Your Code
1. Ensure your code is pushed to a GitHub repository.
2. Include the following files:
   - `main.py`
   - `requirements.txt`
   - `.gitignore` (to exclude `.env`)

### Step 2: Create a Render Account
1. Sign up for a free account at [Render](https://render.com/).
2. Verify your email address.

### Step 3: Deploy to Render
1. Go to the **Dashboard** and click **New +** > **Web Service**.
2. Connect your GitHub repository.
3. Configure the deployment:
   - **Name**: `itec116_<surname>` (replace `<surname>` with your actual surname).
   - **Region**: Choose the closest region.
   - **Branch**: Select the branch containing your code.
   - **Runtime**: Python 3.
   - **Build Command**: `pip install -r requirements.txt`.
   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port 10000`.
4. Add environment variables:
   - Go to the **Environment** section.
   - Add the following variable:
     - Key: `LAB4_API_KEY`
     - Value: `RawrBarney` (use the same API key as in your code).
5. Click **Create Web Service** to deploy.

### Step 4: Access Your Deployed API
- Once deployed, your API will be accessible at: