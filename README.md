# Introduction to FastAPI To-Do List API

This is a simple To-Do List API built with **FastAPI** and **MongoDB**. It allows you to create, read, update, and delete tasks.

## Features

  * **Create a new task**: Add a new task to your to-do list.
  * **Get all tasks**: Retrieve a list of all non-deleted tasks.
  * **Update a task**: Modify the details of an existing task.
  * **Delete a task**: Mark a task as deleted.

## API Endpoints

The following endpoints are available:

| Method | Endpoint | Description |
| --- | --- | --- |
| `GET` | `/` | Get all tasks |
| `POST` | `/` | Create a new task |
| `PUT` | `/{task_id}` | Update an existing task |
| `DELETE` | `/{task_id}` | Delete a task |

## Project Structure

```
├── .gitignore
├── configuration.py
├── database
│   ├── models.py
│   └── schemas.py
└── mongoapi.py
```

  * **`mongoapi.py`**: This is the main application file that contains the FastAPI app and all the API routes.
  * **`database/models.py`**: This file defines the Pydantic model for the `Todo` items.
  * **`database/schemas.py`**: This file contains functions to serialize the data from MongoDB into a JSON-friendly format.
  * **`configuration.py`**: This file handles the connection to the MongoDB database.
  * **`.gitignore`**: This file specifies that the `.env` file should not be tracked by Git.

## Getting Started

### Prerequisites

  * Python 3.8+
  * MongoDB account
  * `pip` installed

### Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/your-repository-name.git
    cd your-repository-name
    ```

2.  **Create a virtual environment and activate it:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the dependencies:**

    ```bash
    pip install fastapi "uvicorn[standard]" pymongo python-dotenv
    ```

4.  **Set up your environment variables:**

      * Create a file named `.env` in the root of your project.
      * Add your MongoDB connection string to the `.env` file:
        ```
        MONGODB_URI="your_mongodb_connection_string"
        ```

### Running the Application

1.  **Start the server:**

    ```bash
    uvicorn mongoapi:app --reload
    ```

2.  **Access the API documentation:**
    Open your browser and go to `http://127.0.0.1:8000/docs` to see the interactive API documentation.
