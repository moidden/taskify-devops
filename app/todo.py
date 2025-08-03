tasks = []

def add_task(task):
    tasks.append(task)
    return tasks

def remove_task(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
    return tasks

def list_tasks():
    return tasks
