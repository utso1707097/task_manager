```markdown
# Task Manager Application

The **Task Manager** is a web application built with Django and Django REST framework that allows users to manage their tasks. Users can create, view, update, and delete tasks, and the application also provides RESTful API endpoints for task management.

## Features

- User Authentication: Users can register, log in, and manage their tasks.
- Password Reset: Includes an optional password reset feature.
- Task Management: Users can create tasks with various properties such as title, description, due date, priority, and completion status.
- Task Listing: Tasks can be searched, filtered, and sorted by various criteria.
- Task Details: View detailed information about a task, including associated photos.
- Task Update and Delete: Edit and delete tasks (users can only modify/delete their own tasks).
- RESTful API: Provides API endpoints for managing tasks via HTTP methods (GET, POST, PUT, DELETE).
- PostgreSQL Database: Utilizes PostgreSQL as the database backend.
- Virtual Environment: Uses a virtual environment for package management.
- Environment Variables: Sensitive settings are managed using environment variables.
- Version Control: Git is used for version control, and the codebase is hosted on GitHub.

## Getting Started

To run the application locally, follow these steps:

1. Clone the repository:
```

git clone https://github.com/your-username/task_manager.git

```

2. Create a virtual environment and activate it:

```

python -m venv venv
source venv/bin/activate # On Windows, use: venv\Scripts\activate

```

3. Install the required dependencies:

```

pip install -r requirements.txt

```

4. Configure the PostgreSQL database:
- Create a PostgreSQL database and configure the database settings in the project's settings.py file.

5. Apply database migrations:

```

python manage.py migrate

```

6. Create a superuser account to access the Django admin panel:

```

python manage.py createsuperuser

```

7. Run the development server:

```

python manage.py runserver

```

8. Access the application in your web browser at `http://localhost:8000/`.

## Usage

- Register a new user account or log in with an existing one.
- Use the application to manage your tasks, create new tasks, and update or delete existing ones.
- Access the Django admin panel at `http://localhost:8000/admin/` to manage users and tasks.
- Explore the API endpoints at `http://localhost:8000/api/tasks/` for task management (requires authentication).

## API Documentation

API endpoints are available for task management. You can access the API documentation and test the endpoints using tools like Postman.

- **API Base URL**: `http://localhost:8000/api/tasks/`

### Endpoints

- `GET /api/tasks/`: List all tasks.
- `POST /api/tasks/`: Create a new task.
- `GET /api/tasks/{task_id}/`: Retrieve a specific task.
- `PUT /api/tasks/{task_id}/`: Update a specific task.
- `DELETE /api/tasks/{task_id}/`: Delete a specific task.

### Authentication

To access API endpoints that require authentication, use Basic Authentication with the following credentials:

- **Username**: admin
- **Password**: admin

## Available Views and Endpoints

- `GET /register/`: Register a new user account.
- `POST /register/`: Register a new user account.
- `GET /login/`: Log in with an existing user account.
- `POST /login/`: Log in with an existing user account.
- `GET /logout/`: Log out the current user.
- `GET /password_reset/`: Initiate a password reset request.
- `POST /password_reset/`: Initiate a password reset request.
- `GET /password_reset/done/`: Display a confirmation message after a password reset request.
- `GET /reset/<uidb64>/<token>/`: Allow users to set a new password after a password reset request.
- `GET /reset/done/`: Display a confirmation message after setting a new password.
- `GET /`: Display a list of tasks.
- `POST /create/`: Create a new task.
- `GET /<int:pk>/`: View details of a specific task.
- `GET /<int:pk>/update/`: Update a specific task.
- `GET /<int:pk>/delete/`: Delete a specific task.
- `GET /api/tasks/`: List all tasks via the API.
- `POST /api/tasks/`: Create a new task via the API.
- `GET /api/tasks/{task_id}/`: Retrieve a specific task via the API.
- `PUT /api/tasks/{task_id}/`: Update a specific task via the API.
- `DELETE /api/tasks/{task_id}/`: Delete a specific task via the API.

## Contributing

Contributions are welcome! If you'd like to contribute to the project, please follow these steps:

1. Fork the repository on GitHub.
2. Clone your forked repository to your local machine.
3. Create a new branch for your feature or bug fix: `git checkout -b feature-name`.
4. Make your changes and commit them with descriptive commit messages.
5. Push your changes to your forked repository.
6. Create a pull request to the main repository.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```
