# Simple To-Do List - Dattatray Bhosale
# For Job Portfolio

import json
from datetime import datetime

TODO_FILE = "todo.json"

def load_todos():
    try:
        with open(TODO_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_todos(todos):
    with open(TODO_FILE, "w") as f:
        json.dump(todos, f, indent=2)

def add_task():
    task = input("Enter new task: ")
    todo = {
        "task": task,
        "status": "Pending",
        "added": datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    todos = load_todos()
    todos.append(todo)
    save_todos(todos)
    print("Task added!")

def view_tasks():
    todos = load_todos()
    if not todos:
        print("No tasks yet.")
        return
    print("\n--- To-Do List ---")
    for i, todo in enumerate(todos, 1):
        status = "✅" if todo["status"] == "Done" else "⭕"
        print(f"{i}. {status} {todo['task']} ({todo['added']})")

def mark_done():
    view_tasks()
    try:
        num = int(input("Enter task number to mark done: ")) - 1
        todos = load_todos()
        todos[num]["status"] = "Done"
        save_todos(todos)
        print("Task marked as done!")
    except:
        print("Invalid number.")

def main():
    while True:
        print("\n=== To-Do List ===")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark as Done")
        print("4. Exit")
        choice = input("Choose option: ")
        
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_done()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()
