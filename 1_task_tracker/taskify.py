# Task Tracker (TodoApp)

"""
- Program Name: Task Tracker
- Description: A simple command-line task tracker that allows users to add, view, update, delete, and mark tasks as complete.
"""

"""
1. Program Need Run in Terminal
2. Program Need use Arguments
3. Read And Wirte Json File
4. If Json File Not Exist, Create New One

_ command line arguments:
- add -> Add a new task
- update -> Update an existing task
- delete -> Delete a task
- mark -> Mark a task as complete (done, in-progres, todo)
- list -> List all tasks
- help -> Show help message
- clear -> Delete all tasks
"""

import json
import os
from rich.console import Console
from rich.table import Table
import time
import sys
from enum import Enum

FILENAME = "tasks.json"


class task_status(Enum):
    """
    Enum class to difine task status. todo, in-progress, done
    """

    TODO = "TODO"
    IN_PROGRESS = "IN_PROGRESS"
    DONE = "DONE"


# config
console = Console()


# JSON HANDLER
def json_create_file(filename=FILENAME):
    """
    this is for create json file def
    """

    with open(filename, "w") as file:
        json.dump([], file)
        console.print(f"\n[green bold]New task file created: {filename}\n")


def json_write_file(task_list, filename=FILENAME):
    """
    This function to write the task list to a JSON file
    """

    with open(filename, "w") as file:
        json.dump(task_list, file)
        console.print(f"\n[green bold]Task saved to {filename}\n")


def json_read_file(filename=FILENAME):
    """
    this funciton to read the task list from a Json File
    """

    if not os.path.exists(filename):
        console.print(f"\n[yellow bold]No tasks found. Creating new file {filename}\n")
        json_create_file()
        return []

    with open(filename, "r") as file:
        task_list_read = json.load(file)
        console.print(f"\n[green bold]Tasks loaded from {filename}\n")
        return task_list_read


# JSON HANDLER


def taskify(task_list):
    """
    Main Funciuton to run the task tracker application.
    """

    # Check if command line argumant are provoded
    if len(sys.argv) > 1:
        # If arguments are provided, manage them
        manage_arguments(argument=sys.argv, task_list=task_list)
        return


def manage_arguments(argument, task_list):
    """
    Function to manage command line arguments for the task tracker.
    """

    match argument[1].lower():
        case "add":
            currnet_task = add_task(
                task_list, argument[2] if len(argument) > 2 else None
            )
            show_tasks([currnet_task])
        case "list":
            show_tasks(task_list)
        case "update":
            pass
        case "delete":
            pass
        case "mark-done":
            pass
        case "mark-in-progress":
            pass
        case "help":
            pass
        case "clear":
            pass
        case _:
            console.print(
                f"\n[yellow bold]Invalid argument. Use 'help' to see available commands.\n"
            )


def get_time_now():
    """
    Function get the current time and date.
    """
    return time.strftime("%Y-%m-%d %H:%M:%S")


# add task
def add_task(task_list, task=None):
    """
    Function to add a new task to the task list.
    """

    # TODO read from json file for get len
    task_id = len(task_list)

    try:
        if task:
            new_task = {
                "id": task_id,
                "description": task,
                "status": task_status.TODO.value,
                "created_at": get_time_now(),
                "updated_at": get_time_now(),
            }

            task_list.append(new_task)
            json_write_file(task_list)

            return new_task

        else:
            console.print(f"\n[yellow bold]Invalid Input task cannot be empty\n")

    except Exception as e:
        raise Exception(f"\n Error adding task: {e}")


def show_tasks(task_list):
    """
    Function to list all taks in the task list. and display to user
    """

    if not task_list:
        console.print(f"\n[red bold]No tasks available.\n")
        return

    # Create a Table instance for displaying tasks
    table = Table(title="Task Tracker", show_lines=True)
    # Create a table to display tasks
    table.add_column("ID", justify="left", style="red", no_wrap=True)
    table.add_column("Description", justify="left", style="blue", no_wrap=False)
    table.add_column("Status", justify="left", style="cyan")
    table.add_column("Created At", justify="left", style="#f0932b")
    table.add_column("Updated At", justify="left", style="yellow")

    for task in task_list:
        table.add_row(
            str(task["id"] + 1),
            task["description"],
            task["status"],
            task["created_at"],
            task["updated_at"],
        )

    console.print(table)
    del table


if __name__ == "__main__":
    """
    Entry point of the application.
    It runs the task tracker function to start the application.
    """

    # Clear Console before starting
    os.system("clear")

    # Load Json File
    task_list = json_read_file()

    # application
    taskify(task_list)
