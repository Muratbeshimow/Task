from classes import Task
from functions import add_task, find_task, remove_task, update_task, view_task, find_category
from modules import remove_all_tasks


while True:
    option = input("""
1. Add Task
2. View Task
3. Find Task
4. Find by Category
5. Update Task
6. Remove Task
7. Remove All
q. Quit
                Choice: """)
    print()
    if option == '1':
        name = input("Task name: ")
        user = input("User name: ")
        task_info = input("Task info: ")
        category = input("Category name: ")
        add_task(Task(name=name, user=user,
                 task_info=task_info, category=category))
    if option == '2':
        view_task()
    if option == '3':
        find_task()
    if option == '4':
        find_category()
    if option == '5':
        update_task()
    if option == '6':
        remove_task()
    if option == '7':
        remove_all_tasks()
    if option == 'q':
        break
