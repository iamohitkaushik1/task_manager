from data_store import DataStore
from utils import generate_id

class TaskManager:
    def __init__(self):
        self.store = DataStore("tasks.txt")
        self.tasks = self.store.load_tasks()

    def add_task(self, task):
        task_id = generate_id()
        self.tasks[task_id] = task
        self.store.save_tasks(self.tasks)
        print(f"Task added with ID: {task_id}")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks found!")
        for id, task in self.tasks.items():
            print(f"ID: {id} - {task}")

    def delete_task(self, task_id):
        if task_id in self.tasks:
            del self.tasks[task_id]
            self.store.save_tasks(self.tasks)
            print("Task deleted!")
        else:
            print("Task not found!")
