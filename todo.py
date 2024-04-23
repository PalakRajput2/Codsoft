class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("The Task  is added successfully!")

    def remove_task(self, task_index):
        if task_index < len(self.tasks):
            del self.tasks[task_index]
            print("The Task is removed successfully!")
        else:
            print("Invalid task index!! Please enter the valid index")

    def display_tasks(self):
        if self.tasks:
            print("Your To-Do List is here :")
            for i, task in enumerate(self.tasks):
                print(f"{i+1}. {task}")
        else:
            print("Your To-Do List is empty!! Please add some entries in it ")

def main():
    todo_list = ToDoList()

    while True:
        print ("***************************************")
        print("Welcome to the to-do list ")
        print("\nChoose an option according to your choice :")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Display Tasks")
        print("4. Quit")

        choice = input("Enter your choice that you want to perform : ")

        if choice == "1":
            task = input("Please Enter the task: ")
            todo_list.add_task(task)
        elif choice == "2":
            task_index = int(input("Enter task index to remove: ")) - 1
            todo_list.remove_task(task_index)
        elif choice == "3":
            todo_list.display_tasks()
        elif choice == "4":
            print("Exiting...")
            print("\nThank you for using this!!! Hope you finish all your work on time")
            break
        else:
            print("Invalid choice! Please choose again the valid index.")

if __name__ == "__main__":
    main()
