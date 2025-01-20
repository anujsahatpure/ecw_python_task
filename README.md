# Task Management Application

## Interview Assignment for ECW

This is my interview assignment for ECW, implementing a  Python web application.

---

## Overview

This is a web application that implements a task management system. The application provides a user-friendly web interface where users can create, update, delete, and mark tasks as complete. The app maintains task state and provides RESTful APIs for all operations.

### Key Features:
- **Web Interface**: Easy-to-use web interface built with Flask
- **Task Management**: Create, read, update, and delete tasks
- **Task Status**: Mark tasks as complete/incomplete
- **Comprehensive Testing**: Includes unit tests with pytest
- **CI/CD Pipeline**: Automated build and deployment using Jenkins
- **Code Quality**: Integrated with SonarQube for code quality analysis

---

## Technical Stack

- **Backend**: Python with Flask framework
- **Testing**: pytest
- **CI/CD**: Jenkins
- **Code Quality**: SonarQube

---

## Project Structure

```
python-project/
├── app.py              # Main Flask application
├── test_app.py         # Unit tests
├── templates/          # HTML templates
├── Jenkinsfile        # Jenkins pipeline configuration
├── sonar-project.properties  # SonarQube configuration
├── requirements.txt    # Project dependencies
└── README.md          # Project documentation
```

---

## How to Use the Application

### Step 1: Setup

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Step 2: Run the Application

1. Start the Flask server:
   ```bash
   python app.py
   ```
2. Open your web browser and navigate to `http://localhost:5000`
3. Use the web interface to manage your tasks

---

## API Endpoints

- `GET /tasks`: Retrieve all tasks
- `POST /tasks`: Create a new task
- `PUT /tasks/<task_id>`: Update a specific task
- `DELETE /tasks/<task_id>`: Delete a specific task
- `PATCH /tasks/<task_id>/done`: Mark a task as complete

---

## Development

### Running Tests
```bash
pytest test_app.py
```

### Check Coverage
```bash
coverage run -m pytest
coverage report
```

### Running SonarQube Analysis
Ensure SonarQube is running locally or configure sonar-project.properties with your SonarQube server details.

---

## CI/CD Pipeline

The project includes a Jenkins pipeline that:
1. Builds the application
2. Runs tests
3. Generates test coverage reports
4. Performs SonarQube analysis
5. Deploys the application (if all checks pass)
