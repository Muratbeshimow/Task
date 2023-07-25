import datetime


class Task:
    def __init__(self, name="", user="", category="", task_info="", created_date=datetime.date(day=24, month=7, year=2023), completed_date=datetime.date(day=30, month=7, year=2023)):
        self.name = name
        self.user = user
        self.category = category
        self.task_info = task_info
        self.created_date = created_date
        self.completed_date = completed_date

    def __repr__(self):
        return f"""
{self.name.capitalize()}\t{self.created_date}\t{self.completed_date}\t{self.user.capitalize()}\t{self.task_info}\t{self.category}"""
