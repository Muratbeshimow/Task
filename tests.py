from classes import Task
import random

from functions import add_task, find_task, view_task
from modules import save_task, load_tasks


def create_task(num: int = 0):
    for _ in range(num):
        name = random.choice(
            ['go to work', 'do a thing', 'do notes in work', 'make a project', 'take breakfast'])
        user = random.choice(
            ['avi', 'tal', 'gal', 'raz', 'haim', 'roni', 'shani', '', 'hen', 'rafi'])
        created_date = f"{random.randrange(1,31)}-{random.randrange(1,12)}-{random.randrange(2020,2023)}"
        completed_date = f"{random.randrange(1,31)}-{random.randrange(1,12)}-{random.randrange(2020,2023)}"
        task_info = random.choice(['wwww', 'cccc', 'jjjj', 'gggg', 'bbbb'])
        category = 'job'
        add_task(Task(name=name, user=user, created_date=created_date,
                 completed_date=completed_date, task_info=task_info, category=category))


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


def find_task(name="name"):
    tasks = load_tasks()
    for task in tasks:
        if task.name == name:
            return task
    else:
        return print("not found")


def remove_task(name="name"):
    tasks = load_tasks()
    name = input("Enter Task name or User name to remove: ")
    for task in tasks.copy():
        if task.name == name or task.user == name:
            tasks.remove(task)
            print("Task removed")
    save_task(tasks)


# test_task = Task(name="test")
# add_task(test_task)
# found_task = find_task(test_task.name)
# if find_task(test_task.name):
#     print("Add test success")
# else:
#     print("Add test fail")
view_task()
# remove_task()
