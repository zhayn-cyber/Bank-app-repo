import os
from typing import Optional

def load_data_from_file(filename: str) -> list:
    """
    Loads tasks data from a file and returns a list of tasks.
    
    :param filename: The name of the file to load.
    :return: A list of task dictionaries.
    """
    tasks = []
    if os.path.exists(filename):
        with open(filename, "r") as file:
            lines = file.readlines()
            for line in lines:
                task_data = line.strip().split(",")
                task = {
                    "task_id": int(task_data[0]),
                    "task_name": task_data[1],
                    "task_status": task_data[2],
                    "time_created": task_data[3],
                    "time_finished": task_data[4] if task_data[4] != "None" else None
                }
                tasks.append(task)
    return tasks

def save_data_to_file(filename: str, tasks: list) -> None:
    """
    Saves a list of tasks to a file.
    
    :param filename: The name of the file to save tasks to.
    :param tasks: A list of task dictionaries.
    """
    with open(filename, "w") as file:
        for task in tasks:
            task_line = f"{task['task_id']},{task['task_name']},{task['task_status']},{task['time_created']},{task['time_finished']}\n"
            file.write(task_line)

def save_user_name(name: str) -> None:
    """
    Save the user's name to a file `names.txt`.
    
    :param name: The user's name to be saved.
    """
    with open("names.txt", "w") as file:
        file.write(name)

def load_user_name() -> Optional[str]:
    """
    Load the user's name from `names.txt`.
    
    :return: The user's name if the file exists, otherwise None.
    """
    if os.path.exists("names.txt"):
        with open("names.txt", "r") as file:
            return file.readline().strip()
    return None