from classes import TaskManager
from modules import load_tasks, save_task


def add_task():
    tasks = load_tasks()
    name = input("Task name: ")
    user = input("Task user: ")
    task_info = input("Task info: ")
    category = input("Task category: ")
    new_task = TaskManager(name=name, user=user,
                           task_info=task_info, category=category)
    tasks.append(new_task)
    save_task(tasks)
    print("New Task Added")


def view_task():
    tasks = load_tasks()
    print("Task name\tCreated date\tCompleted date\tUser\tinfo\tCategory")
    print("------------------------------------------------------------------------", end='')
    print(*tasks)


def find_task():
    tasks = load_tasks()
    name = input("Enter Task name or User name to find: ")
    for task in tasks:
        if task.name == name or task.user == name:
            print(
                f"User: {task.user.capitalize()} - Task name: {task.name.capitalize()} - Date created: {task.created_date}")


def find_category():
    tasks = load_tasks()
    category = input("Enter category name: ")
    for task in tasks:
        if task.category in category:
            print(f"Task name: {task.name} - Category: {task.category}")


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


def remove_task():
    tasks = load_tasks()
    user_input = input("Enter task name or user name to remove: ")
    for task in tasks:
        if task.name == user_input or task.user == user_input:
            tasks.remove(task)
            print("Task removed")
            save_task(tasks)
        break
    else:
        print("Task not found.Please try again")
