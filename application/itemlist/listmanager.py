from collections import defaultdict

class SimpleListManager:
    def __init__(self):
        self.listOfItems = []

    def insert_task(self, task=None):
        if task:
            self.insert(task)
        return self.get_all_tasks()

    def delete_task(self, task=None):
        if task:
            self.delete(task)
        return self.get_all_tasks()

    def get_all_tasks(self):
        taskList = []
        for task in self.listOfItems:
            taskList.append(task)
        return taskList
        
    def insert(self,task):
        if task not in self.listOfItems:
            self.listOfItems.append(task)

    def delete(self, task):
        if task in self.listOfItems:
            self.listOfItems.remove(task)

registry = SimpleListManager()