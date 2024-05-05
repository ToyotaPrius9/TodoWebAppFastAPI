# API LOGIC!!!

## Technologies Used:
- FastAPI for building the API endpoints
- SQLAlchemy for database management
- SQLite as the lightweight relational database
- Pydantic for data validation and parsing

## API Endpoints:

1. **Create Task**
   - **URL:** `/tasks/`
   - **Method:** POST
   - **Request Body:**
     ```json
     {
       "text": "Task description"
     }
     ```
   - **Response Example:**
     ```json
     {
       "id": 1,
       "text": "Task description",
       "completed": false
     }
     ```

2. **List Tasks**
   - **URL:** `/tasks/`
   - **Method:** GET
   - **Query Parameters:**
     - `skip` (optional): Number of tasks to skip (default: 0)
     - `limit` (optional): Maximum number of tasks to return (default: 10)
   - **Response Example:**
     ```json
     [
       {
         "id": 1,
         "text": "Task 1",
         "completed": false
       },
       {
         "id": 2,
         "text": "Task 2",
         "completed": true
       }
     ]
     ```

3. **Delete Task**
   - **URL:** `/tasks/{task_id}/`
   - **Method:** DELETE
   - **Path Parameter:**
     - `task_id`: ID of the task to delete
   - **Response Example:**
     ```json
     {
       "message": "Task deleted successfully"
     }
     ```

4. **Update Task**
   - **URL:** `/tasks/{task_id}/`
   - **Method:** PUT
   - **Path Parameter:**
     - `task_id`: ID of the task to update
   - **Request Body:**
     ```json
     {
       "completed": true
     }
     ```
   - **Response Example:**
     ```json
     {
       "id": 1,
       "text": "Task description",
       "completed": true
     }
     ```



