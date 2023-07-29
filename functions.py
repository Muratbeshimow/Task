from classes import Task
from modules import load_tasks, save_task


def add_task(task: Task):
    tasks = load_tasks()
    tasks.append(task)
    save_task(tasks)


def view_task():
    tasks = load_tasks()
    print(*tasks)


def find_task():
    tasks = load_tasks()
    name = input("Enter Task name or User name to find: ")
    for task in tasks:
        if task.name == name or task.user == name:
            print(task)


def find_category():
    tasks = load_tasks()
    category = input("Enter category name: ")
    for task in tasks:
        if task.category in category:
            print(task)


def update_task():
    tasks = load_tasks()
    user_input = input("Enter user name to update details: ")
    print()
    for task in tasks:
        if task.user == user_input:
            option = input(f"""
What you want to update for contact: {task.user.capitalize()}

1. Task Name  
2. Task Category 
3. Task info
4. Change All

             Choice: """)
            print()
            if option == '1':
                task.name = input("New task name: ")
                print("Task name updated")
            elif option == '2':
                task.category = input("New category name: ")
                print("Category updated")
            elif option == '3':
                task.task_info = input("Enter task info: ")
                print("Task info updated")
            elif option == '4':
                task.name = input("Task name: ")
                task.user = input("Task user: ")
                task.task_info = input("Task info: ")
                task.category = input("Task category: ")
                print("All details changed")
            save_task(tasks)
            break
    else:
        print("User not found.Please try again.")


def remove_task(name="name"):
    tasks = load_tasks()
    name = input("Enter Task name or User name to remove: ")
    for task in tasks.copy():
        if task.name == name or task.user == name:
            tasks.remove(task)
            print("Task removed")
    save_task(tasks)


def register():
    class Task:
        def __init__(self, name, user, task_info, category):
            self.name = name
            self.user = user
            self.task_info = task_info
            self.category = category

    name = input("Enter Task name: ")
    user = input("Enter User name: ")
    task_info = input("Enter Task info: ")
    category = input("Enter Task category: ")

    new_task = Task(name=name, user=user,
                    task_info=task_info, category=category)
    add_task(new_task)
    print("Task registered successfully!")
