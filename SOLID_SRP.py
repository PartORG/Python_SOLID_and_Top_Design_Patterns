# BAD CLASS - this class violates SRP - class has many responsibilities:
class ToDoList:
    def __init__(self):
        self.tasks = []

    # this manages task
    def add_task(self, task):
        self.tasks.append(task)

    # this manages task
    def delete_task(self, task):
        self.tasks.remove(task)

    # this displays task
    def display_task(self):
        for task in self.tasks:
            print(task)

    # this handles user input
    def input_task(self):
        task = input("Enter a task: ")
        self.add_task(task)

    # this handles user input
    def remove_task(self):
        task = input("Enter the task to remove: ")
        self.delete_task(task)


# REFACTORED VERSION - adheres to SRP - each class has only one responsibility:
class TaskManager:
    def __init__(self):
        self.tasks = []

    # this manages task
    def add_task(self, task):
        self.tasks.append(task)

    # this manages task
    def delete_task(self, task):
        self.tasks.remove(task)

class TaskPresenter:
    # this displays task
    @staticmethod
    def display_task(tasks):
        for task in tasks:
            print(task)

class TaskInput:
    # this handles user input
    @staticmethod
    def input_task():
        return input("Enter a task: ")

    # this handles user input
    @staticmethod
    def remove_task():
        return input("Enter the task to remove: ")