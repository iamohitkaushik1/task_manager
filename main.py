from task_manager import TaskManager

def main():
    manager = TaskManager()
    while True:
        print("\n1. Add Task\n2. List Tasks\n3. Delete Task\n4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            task = input("Enter task: ")
            manager.add_task(task)
        elif choice == "2":
            manager.list_tasks()
        elif choice == "3":
            task_id = int(input("Enter task ID to delete: "))
            manager.delete_task(task_id)
        elif choice == "4":
            break

if __name__ == "__main__":
    main()
