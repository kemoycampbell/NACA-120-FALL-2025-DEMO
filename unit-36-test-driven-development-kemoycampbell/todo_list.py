tasks = []

def get_tasks_size():
    return len(tasks)

def add_task(task_name):
    task = {"name": task_name, "status":"todo"}
    tasks.append(task)