# Task Tracker (TodoAPP)

# Add Task
# Show Task
# Update Task
# Delete Task

# ---START OF TASK TRACKER---
import os

my_task_list = []
# File


def task_menu(task_list):
    print("\n--- ⏰ Task Tracker Menu ⏰ ---\n")
    print("1. Add Task")
    print("2. Show Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Change Status Task")
    print("6. Exit")

    operation = input("Select an operation (1-6): ")
    if operation == "1":
        add_task(task_list)
        os.system("clear")
    elif operation == "2":
        show_tasks(task_list)
    elif operation == "3":
        update_task(task_list)
    elif operation == "4":
        delete_task(task_list)
    elif operation == "5":
        # TODO with file system wiht json wiht database
        complete_task(task_list)
    elif operation == "6":
        # exit(1)
        return
    else:
        os.system("clear")
        print("\n ‼️ (Invaild selection. Please try again.)\n")
        task_menu(task_list)
    # TODO : change value with temp variable


# Add a new task to the task list
def add_task(task_list):
    os.system("clear")
    task = input("\n |--> Enter the task: ")
    if task:
        task_list.append(task + " ❌")
        print(f"\n✅ (Task '{task}' added successfully.)")
        task_menu(task_list)
    else:
        print("\n‼️ (Task cannot be empty.)")
        add_task(task_list)


# Show all tasks in the task list
def show_tasks(task_list, back_to_menu=True):
    os.system("clear")
    if not task_list:
        print("\n 🚫 (No tasks available.)")
    else:
        print("\n --- Currnet Tasks ---")
        for index, task in enumerate(task_list, start=1):
            print(f"{index}. {task}")
    if back_to_menu:
        task_menu(task_list)


# delete a task from the task list
def delete_task(task_list):
    if not task_list:
        print("\n ‼️ (No tasks available to delete.)")
        task_menu(task_list)

    # if avaialbe
    show_tasks(task_list, False)
    try:
        task_index = int(input("Enter the task number for delete: ")) - 1
        if 0 <= task_index < len(task_list):
            removed_task = task_list.pop(task_index)
            print(f"\n✅ (Task '{removed_task}' deleted successfully.)")
        else:
            print("\n ‼️ (Invalid task number.)")
    except ValueError:
        print("\n ‼️ (Please enter a valid number)")

    task_menu(task_list)


# Update task from the task list
def update_task(task_list):
    if not task_list:
        print("\n ‼️ (No tasks available to update.)")
        task_menu(task_list)

    show_tasks(task_list, False)
    try:
        task_index = int(input("Enter the task number for update: ")) - 1
        if 0 <= task_index < len(task_list):
            new_task = input("Enter the updated task: ")
            if new_task:
                task_list[task_index] = new_task + " ❌"
                print(f"\n✅ (Task updated to '{new_task}'.)")
            else:
                print("\n ‼️ (Task cannot be empty.)")
                update_task(task_list)
        else:
            print("\n ‼️ (Invalid task number.)")
    except ValueError:
        print("\n ‼️ (Please enter a valid number)")

    task_menu(task_list)


# change status to complete ✅ form list
def complete_task(task_list):
    if not task_list:
        print("\n ‼️ (No tasks available to change status.)")
        task_menu(task_list)

    show_tasks(task_list, False)
    try:
        task_index = int(input("Enter the task number for update: ")) - 1
        if 0 <= task_index < len(task_list):
            task_list[task_index] = task_list[task_index][:-1] + " ✅"
            print(f"\n ✅ Your Task :'{task_list[task_index][:-1]} completed.'")
        else:
            print("\n ‼️ (Invalid task number.)")
    except ValueError:
        print("\n ‼️ (Please enter a valid number)")

    task_menu(task_list)


# Start APP
task_menu(my_task_list)
