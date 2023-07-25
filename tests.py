from classes import Task
import random

from functions import add_task, view_task
from modules import remove_all_tasks


def create_job(num: int = 0):
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


def create_shop(num: int = 0):
    for _ in range(num):
        name = random.choice(
            ['go to shop', 'buy a milk', 'buy a eggs', 'go to market', 'go buy coffe'])
        user = random.choice(
            ['mike', 'john', 'joe', 'richard', 'dani', 'hani', 'shani', '', 'hen', 'rafi'])
        created_date = f"{random.randrange(1,31)}-{random.randrange(1,12)}-{random.randrange(2020,2023)}"
        completed_date = f"{random.randrange(1,31)}-{random.randrange(1,12)}-{random.randrange(2020,2023)}"
        task_info = random.choice(['aaaa', 'yyyy', 'iiii', 'ffff', 'bbbb'])
        category = 'shop'
        add_task(Task(name=name, user=user, created_date=created_date,
                 completed_date=completed_date, task_info=task_info, category=category))


def create_sport(num: int = 0):
    for _ in range(num):
        name = random.choice(
            ['go to gym', 'do a thing', 'do a exersizes', 'go to walk', 'make a rest'])
        user = random.choice(
            ['avi', 'tal', 'gal', 'raz', 'haim', 'roni', 'shani', '', 'hen', 'rafi'])
        created_date = f"{random.randrange(1,31)}-{random.randrange(1,12)}-{random.randrange(2020,2023)}"
        completed_date = f"{random.randrange(1,31)}-{random.randrange(1,12)}-{random.randrange(2020,2023)}"
        task_info = random.choice(['wwww', 'cccc', 'jjjj', 'gggg', 'bbbb'])
        category = 'sport'
        add_task(Task(name=name, user=user, created_date=created_date,
                 completed_date=completed_date, task_info=task_info, category=category))


def create_cleaning(num: int = 0):
    for _ in range(num):
        name = random.choice(
            ['wash a car', 'clean the car', 'do a thing', 'clean the room', 'clean the bath'])
        user = random.choice(
            ['avi', 'tal', 'gal', 'raz', 'haim', 'roni', 'shani', '', 'hen', 'rafi'])
        created_date = f"{random.randrange(1,31)}-{random.randrange(1,12)}-{random.randrange(2020,2023)}"
        completed_date = f"{random.randrange(1,31)}-{random.randrange(1,12)}-{random.randrange(2020,2023)}"
        task_info = random.choice(['wwww', 'cccc', 'jjjj', 'gggg', 'bbbb'])
        category = 'cleaning'
        add_task(Task(name=name, user=user, created_date=created_date,
                 completed_date=completed_date, task_info=task_info, category=category))


view_task()
