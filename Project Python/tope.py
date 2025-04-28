class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        return f"{self.description} - {status}"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)

    def delete_task(self, index):
        try:
            del self.tasks[index]
        except IndexError:
            print("Invalid task index.")

    def mark_task_completed(self, index):
        try:
            self.tasks[index].mark_completed()
        except IndexError:
            print("Invalid task index.")

    def view_tasks(self):
        for index, task in enumerate(self.tasks):
            print(f"{index + 1}. {task}")

def main():
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List App")
        print("1. Add task")
        print("2. Delete task")
        print("3. Mark task completed")
        print("4. View tasks")
        print("5. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            description = input("Enter task description: ")
            todo_list.add_task(description)
        elif choice == "2":
            index = int(input("Enter task index to delete: ")) - 1
            todo_list.delete_task(index)
        elif choice == "3":
            index = int(input("Enter task index to mark completed: ")) - 1
            todo_list.mark_task_completed(index)
        elif choice == "4":
            todo_list.view_tasks()
        elif choice == "5":
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
