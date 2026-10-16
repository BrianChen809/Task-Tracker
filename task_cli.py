import sys
import json
from datetime import datetime, timezone

def main():
    if len(sys.argv) < 2:
        print("Invalid Command")
        return

    if sys.argv[1] == "add":
        if len(sys.argv) < 3:
            print("Please provide a task description.")
            return
        
        tasks = load_tasks()

        timestamp = datetime.now(timezone.utc).isoformat()

        task = {"id": max((task["id"] for task in tasks), default=0) + 1, "description": sys.argv[2], "status": "todo",
                "createdAt": timestamp, "updatedAt": timestamp}
        tasks.append(task)
        
        save_tasks(tasks)

    elif sys.argv[1] == "list":
        valid_statuses = ("todo", "in-progress", "done")
        if len(sys.argv) > 2 and sys.argv[2] not in valid_statuses:
            print("Invalid status. Use todo, in-progress, or done.")
            return
        
        tasks = load_tasks()

        if len(sys.argv) == 2:
            for task in tasks:
                print(f"{task['id']}. {task['description']} [{task['status']}]")
        else:
            for task in tasks:
                if task["status"] == sys.argv[2]:
                    print(f"{task['id']}. {task['description']} [{task['status']}]")

    elif sys.argv[1] in ("mark-done", "mark-in-progress"):
        if len(sys.argv) < 3:
            print("Please provide a task ID.")
            return
        try:
            id = int(sys.argv[2])
        except ValueError:
            print("Task ID must be a number.")
            return

        if sys.argv[1] == "mark-done":
            update_status(id, "done")
        else:
            update_status(id, "in-progress")

    elif sys.argv[1] == "delete":
        if len(sys.argv) < 3:
            print("Please provide a task ID.")
            return
        try:
            id = int(sys.argv[2])
        except ValueError:
            print("Task ID must be a number.")
            return

        delete_task(id)

    elif sys.argv[1] == "update":
        if len(sys.argv) < 4:
            print("Please provide a task ID and a new description.")
            return
        try:
            id = int(sys.argv[2])
        except ValueError:
            print("Task ID must be a number.")
            return

        update_task(id, sys.argv[3])

    else:
        print("Invalid command")

def update_task(task_id, description):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            timestamp = datetime.now(timezone.utc).isoformat()
            task["description"] = description
            task["updatedAt"] = timestamp
            save_tasks(tasks)
            return
    print("Invalid Task ID")
        
def delete_task(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            save_tasks(tasks)
            return
    print("Invalid task ID")

def update_status(task_id, new_status):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            timestamp = datetime.now(timezone.utc).isoformat()
            task["status"] = new_status
            task["updatedAt"] = timestamp
            save_tasks(tasks)
            return

    print("Invalid task ID")

def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

if __name__ == "__main__":
    main()