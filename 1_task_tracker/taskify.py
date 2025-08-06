"""
# Taskify (Task Tracker) 😎

# python taskify.py [command] [subcommand] (text)

# commands:
# add (text)
# list
# update 1 (text)
# delete 2
"""

# color: colorama
# table: tabulate

# Start APP
import sys
from colorama import Fore, Back, Style
import json
from datetime import datetime as dt
import os
from tabulate import tabulate


# Good Thing TODO
# TODO: make own file structrue saver

# Enum Status
# class Status(Enum):
#     TODO = "todo"
#     DONE = "done"
#     IN_PROGRESS = "in-progress"


# const - Global
TODO = "todo"
DONE = "done"
IN_PROGRESS = "in-progress"

FILENAME = "tasks.json"


def get_time_now():
    """Function Return date and time current as string"""
    return dt.now().strftime("%Y-%m-%d %H:%M:%S")


def where_is_it(filename=FILENAME):
    if not os.path.exists(filename):
        return 0

    with open(filename, "r") as file:
        tasks = json.load(file)
    return len(tasks)


def read_all_tasks(filename=FILENAME):
    """Function To read all json file tasks"""
    try:
        if os.path.exists(filename):
            with open(filename, "r") as file:
                return json.load(file)
        else:
            return None
    except:
        with open(filename, "w") as file:
            file.write("[]")


def save_changes(task, filename=FILENAME):
    tasks = []
    if os.path.exists(filename):
        with open(filename, "r") as file:
            tasks = json.load(file)
    else:
        with open(filename, "w") as file:
            file.write("[]")

    # append
    tasks.append(task)

    # the result is a JSON string:
    with open(filename, "w") as file:
        json.dump(tasks, file)


def main():
    # check argumanet is avalable
    if len(sys.argv) > 1:
        manage_arg(sys.argv)
    else:
        print(
            Fore.RED
            + Style.BRIGHT
            + "Please Enter a Argument when you run a application"
        )
        exit(1)


def manage_arg(arguments):
    # command
    arg = arguments[1].lower()

    # Add Task
    if arg in ["add", "a"]:
        os.system("clear")
        # just add new task
        last_added = add_task(arguments[2])
        # just show last added
        temp_list = []
        temp_list.append(last_added)

        list_task(temp_list)
        del temp_list

    elif arg in ["del", "delete", "remove"]:
        delete_task()
    elif arg in ["update", "edit"]:
        update_task()

    # Show Table
    elif arg in ["show", "list", "table"]:
        os.system("clear")
        list_task(read_all_tasks())

    # clear Tasks
    elif arg in ["clear", "clean"]:
        clear_list()

    else:
        print(Fore.YELLOW + Style.BRIGHT + "Invalid Command.")


def add_task(text):
    # text
    # text append list
    # save_changes()
    # show table
    new_task = {
        # id
        # title
        # status
        # creadted_at
        # updated_at
        "id": where_is_it(),
        "title": text,
        "status": TODO,
        "created_at": get_time_now(),
        "updated_at": get_time_now(),
    }

    save_changes(new_task)

    return new_task

    # show list : TODO


def delete_task():
    pass


def update_task():
    pass


def list_task(tasks):
    """Funciton To Show List in Table Tasks"""
    table = []

    if not tasks:
        print(Fore.RED + Style.BRIGHT + "\nNo Avalable Tasks !\n")
        return

    # loop inject tasks to task and finaly inject to table(rows)
    for task in tasks:
        table.append(
            [
                task["id"],
                task["title"],
                task["status"],
                task["created_at"],
                task["updated_at"],
            ]
        )

    # combine rows and column
    final_table = tabulate(
        table, headers=["ID", "Title", "Status", "Created At", "Updated At"]
    )

    # just show table
    print(Fore.GREEN + Style.BRIGHT + f"\n\n{final_table}\n\n")


def clear_list(filename=FILENAME):
    os.system("clear")

    # claering
    with open(filename, "w") as file:
        file.write("[]")

    print(Fore.YELLOW + Style.BRIGHT + "All Tasks cleared.")


if __name__ == "__main__":
    main()
