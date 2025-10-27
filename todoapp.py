# Syntecxhub Internship - Week 1 Task
# Project 3: To-Do List Manager
# Author: Riyaz Diwan

import json

FILE_NAME = "tasks.json"

# Load existing tasks from file
def load_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save tasks to file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

# Display all tasks
def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks found!")
    else:
        print("\n===== YOUR TASKS =====")
        for i, task in enumerate(tasks, start=1):
            status = "✅ Done" if task["done"] else "❌ Pending"
            print(f"{i}. {task['title']} - {status}")

# Main menu
def main():
    tasks = load_tasks()
    while True:
        print("\n===== TO-DO LIST MANAGER =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            title = input("Enter task title: ")
            tasks.append({"title": title, "done": False})
            save_tasks(tasks)
            print("✅ Task added successfully!")

        elif choice == '2':
            show_tasks(tasks)

        elif choice == '3':
            show_tasks(tasks)
            try:
                num = int(input("Enter task number to mark as done: "))
                tasks[num - 1]["done"] = True
                save_tasks(tasks)
                print("✅ Task marked as done!")
            except (ValueError, IndexError):
                print("⚠️ Invalid task number!")

        elif choice == '4':
            show_tasks(tasks)
            try:
                num = int(input("Enter task number to delete: "))
                del tasks[num - 1]
                save_tasks(tasks)
                print("🗑️ Task deleted successfully!")
            except (ValueError, IndexError):
                print("⚠️ Invalid task number!")

        elif choice == '5':
            print("👋 Goodbye! Tasks saved successfully.")
            break

        else:
            print("⚠️ Invalid choice! Please select between 1–5.")

if __name__ == "__main__":
    main()
