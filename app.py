from functions import add_task, find_task, remove_task, update_task, view_task, find_category


while True:
    option = input("""
1. Add Task
2. View Task
3. Find Task
4. Find by Category
5. Update Task
6. Remove Task
q. Quit
                Choice: """)
    print()
    if option == '1':
        add_task()
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
    if option == 'q':
        break
