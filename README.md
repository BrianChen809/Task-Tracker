# Task Tracker CLI

A simple command-line task tracker built with Python that allows users to create, update, delete, and manage tasks. Tasks are stored locally in a JSON file, allowing them to persist between program executions.

This project is based on the [Task Tracker project from roadmap.sh](https://roadmap.sh/projects/task-tracker).

## Features

- Add new tasks with unique IDs
- Update task descriptions
- Delete existing tasks
- Mark tasks as in progress or completed
- List all tasks or filter by status
- Automatically record task creation and modification timestamps
- Store tasks locally using JSON
- Handle invalid task IDs and missing command arguments

## Technologies Used

- **Python 3**
- **JSON** for data storage
- **Python Standard Library** (`sys`, `json`, `datetime`)

No external dependencies are required.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/BrianChen809/task-tracker.git
   ```

2. Navigate to the project directory:

   ```bash
   cd task-tracker
   ```

3. Make sure Python 3 is installed:

   ```bash
   python --version
   ```

## Usage

Run commands from the terminal using `task_cli.py`.

### Add a Task

```bash
python task_cli.py add "Finish homework"
```

### List All Tasks

```bash
python task_cli.py list
```

Example output:

```text
1. Finish homework [todo]
2. Study Python [in-progress]
3. Apply for internships [done]
```

### Update a Task

Update a task's description using its ID:

```bash
python task_cli.py update 1 "Finish math homework"
```

### Delete a Task

```bash
python task_cli.py delete 1
```

### Update Task Status

Mark a task as in progress:

```bash
python task_cli.py mark-in-progress 2
```

Mark a task as completed:

```bash
python task_cli.py mark-done 2
```

### Filter Tasks by Status

List tasks that haven't been started:

```bash
python task_cli.py list todo
```

List tasks currently in progress:

```bash
python task_cli.py list in-progress
```

List completed tasks:

```bash
python task_cli.py list done
```

## Data Storage

Tasks are stored in a local `tasks.json` file, which is automatically created when a task is added.

Each task contains the following fields:

- `id`: Unique task identifier
- `description`: Task description
- `status`: Current task status (`todo`, `in-progress`, or `done`)
- `createdAt`: Timestamp when the task was created
- `updatedAt`: Timestamp when the task was last modified

Example JSON structure:

```json
[
    {
        "id": 1,
        "description": "Finish homework",
        "status": "todo",
        "createdAt": "2026-10-16T14:00:00+00:00",
        "updatedAt": "2026-10-16T15:30:00+00:00"
    }
]
```

## Project Reference

[roadmap.sh — Task Tracker](https://roadmap.sh/projects/task-tracker)