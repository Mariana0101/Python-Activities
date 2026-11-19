"""
To-Do List Application

A small Python project with a user interface
that allows users to manage pending and completed tasks.

Features:
- Add new tasks
- Display pending tasks
- Mark tasks as complete
- Display completed tasks
- Validate empty inputs and duplicate entries
- Make multiple lists and switch between them
"""
class ToDoList:
    def __init__(self):
        self.tasks = []
        self.complete = []
    
    def addTask(self, task):
        clean_task = task.strip()
        if clean_task == "":
            print("Task can't be empty ;(")
        elif any(t.lower() == clean_task.lower() for t in self.tasks):
            print("Task already added :)")
        else:
            self.tasks.append(clean_task)
            print(f"Task {clean_task} has been added!")
    
    def toDo(self):
        print(f"These are the remaining tasks in your ToDoList: {self.tasks}")
    
    def markComplete(self, task):
        task_new = task.strip().lower()
        if task_new == "":
            print("Task can't be empty ;(")
            return
        for t in self.tasks:
            if t.lower() == task_new:
                self.complete.append(t)
                self.tasks.remove(t)
                print(f"{t} has been marked as complete!")
                return
        print("Task not in ToDoList :0")
    
    def completed(self):
        print(f"These are all your completed tasks: {self.complete}")


lists = {"default<3": ToDoList()}  
name_list = "default<3"

while True:
    print("TO DO LIST !")
    active_list = lists[name_list]
    print(f"Current List: {name_list}")
    print("1. Add Task")
    print("2. View Remaining Tasks")
    print("3. Mark Task Complete")
    print("4. View Completed Tasks")
    print("5. Create New List")
    print("6. Switch List")
    print("7. Quit :(")

    choice = input("Choose an option (1-7): ").strip()

    if choice == "1":
        while True:
            task = input("Enter task to add: ")
            if task.strip() == "":
                break
            active_list.addTask(task)
    elif choice == "2":
        active_list.toDo()
    elif choice == "3":
        while True:
            task = input("Enter task completed! : ")
            if task.strip() == "":
                break
            active_list.markComplete(task)
    elif choice == "4":
        active_list.completed()
    elif choice == "5":
        new_name = input("Enter the name for your New List!: ").strip()
        if not new_name:
            print("List name cannot be empty.")
        elif any(k.lower() == new_name.lower() for k in lists):
            print(f"A list named '{new_name}' already exists!")
        else:
            lists[new_name] = ToDoList()  
            name_list = new_name          
            print(f"Created and switched to '{new_name}'!")
    elif choice == "6":
        print(f"Available lists: {', '.join(lists.keys())}")
        target = input("Enter the list name to switch to: ").strip().lower()
        matched_key = next((k for k in lists if k.lower() == target), None)
        if matched_key:
            name_list = matched_key   
            print(f"Switched to '{name_list}'!")
        else:
            print("List not found.")
    elif choice == "7":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 7.")
