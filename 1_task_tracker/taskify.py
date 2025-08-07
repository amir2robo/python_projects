"""
# Taskify (Task Tracker) 😎 (DONE✅)

# python taskify.py [command] [subcommand] (text)

# commands:
# add (text)
# list
# update 1 (text)
# delete 2
# mark-done 3
# mark-in-progress 2
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


def write_tasks(tasks, filename=FILENAME):
    with open(filename, "w") as file:
        json.dump(tasks, file)


def update_title_by_index(index, new_title, filename=FILENAME):
    tasks = read_all_tasks() or []

    # update
    tasks[index]["title"] = new_title
    tasks[index]["updated_at"] = get_time_now()

    # the result is a JSON string:
    write_tasks(tasks)


#
def delete_task_by_id(index, filename=FILENAME):
    tasks = read_all_tasks() or []

    # append
    tasks.pop(index)

    # the result is a JSON string:
    write_tasks(tasks)


def save_changes(task, filename=FILENAME):
    tasks = read_all_tasks() or []

    # append
    tasks.append(task)

    # the result is a JSON string:
    write_tasks(tasks)


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
    os.system("clear")

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

    # Delete Task
    elif arg in ["del", "delete", "remove"]:
        delete_task(arguments[2])

    # Update or Edit
    elif arg in ["update", "edit"]:
        update_task(arguments[2], arguments[3])

    # Show Table
    elif arg in ["show", "list", "table"]:
        list_task(read_all_tasks())

    # clear Tasks
    elif arg in ["clear", "clean"]:
        clear_list()

    elif arg in ["mark-done", "done"]:
        mark_task(arguments[2], DONE)

    elif arg in ["mark-in-progress", "in-progress", "doing"]:
        mark_task(arguments[2], IN_PROGRESS)

    else:
        print(Fore.YELLOW + Style.BRIGHT + "Invalid Command.")


def mark_task(index, status):
    """Function change status"""
    tasks = read_all_tasks() or []

    # change status
    real_index = int(index) - 1
    tasks[real_index]["status"] = status

    write_tasks(tasks)

    # show table
    list_task(tasks)

    print(Fore.GREEN + Back.WHITE + Style.BRIGHT + f"\n task {index}: {status}")


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


def delete_task(index):
    """Function to delete task by id index"""
    # real index
    real_index = int(index) - 1

    # deleting
    delete_task_by_id(real_index)

    print(Fore.WHITE + Back.RED + Style.BRIGHT + f"id {index} has been deleted.")


def update_task(index, new_title):
    """Function Update Task by index with new_text"""

    # real index
    real_index = int(index) - 1

    #
    update_title_by_index(real_index, new_title)

    #
    print(
        Fore.BLUE
        + Back.WHITE
        + Style.BRIGHT
        + f"\ntask {index} has been updated with {new_title}\n"
    )


def list_task(tasks):
    """Funciton To Show List in Table Tasks"""
    table = []

    if not tasks:
        print(Fore.RED + Style.BRIGHT + "\nNo Avalable Tasks !\n")
        return

    # loop inject tasks to task and finaly inject to table(rows)
    for index, task in enumerate(tasks, start=1):
        table.append(
            [
                index,
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
    # Just Clear Terminal
    os.system("clear")

    # claering
    with open(filename, "w") as file:
        file.write("[]")

    print(Fore.YELLOW + Style.BRIGHT + "All Tasks cleared.")


if __name__ == "__main__":
    main()
