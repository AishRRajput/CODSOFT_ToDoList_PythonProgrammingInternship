class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Task added to the to-do list:", task)

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print("Task removed from the to-do list:", task)
        else:
            print("Task not found in the to-do list.")

    def view_tasks(self):
        if self.tasks:
            print("Tasks in the to-do list:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")
        else:
            print("To-do list is empty.")

def main():
    todo_list = TodoList()

    while True:
        print("\nTo-Do List Options:")
        print("1. Add task")
        print("2. Remove task")
        print("3. View tasks")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter task to add: ")
            todo_list.add_task(task)
        elif choice == '2':
            task = input("Enter task to remove: ")
            todo_list.remove_task(task)
        elif choice == '3':
            todo_list.view_tasks()
        elif choice == '4':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
