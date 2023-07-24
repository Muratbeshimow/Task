import datetime


class Task:
    def __init__(self, name="Task Management\n"):
        self.name = name
        self.created_date = datetime.date.today()
        self.completed_date = datetime.date(day=29, month=7, year=2023)

    def __repr__(self):
        return f"{self.name}"


class TaskManager:
    def __init__(self, name="", user="", category="", task_info=""):
        self.name = name
        self.user = user
        self.category = category
        self.task_info = task_info
        self.created_date = datetime.date.today()
        self.completed_date = datetime.date(day=30, month=7, year=2023)

    def __repr__(self):
        return f"""
{self.name.capitalize()}\t{self.created_date}\t{self.completed_date}\t{self.user.capitalize()}\t{self.task_info}    {self.category}"""


print("Welcome to", Task(), end='')
