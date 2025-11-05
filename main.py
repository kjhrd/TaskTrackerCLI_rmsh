from datetime import datetime
import json, argparse
from enum import Enum


class STATUS(Enum):
    TODO = "todo"
    IN_PROGRESS = "in-progress"
    DONE = "done"


class TaskManager:
    def __init__(self):
        self.tasks = json.load(open('tasks.json'))

    def add_task(self, name):
        if name:
            _id = len(self.tasks) + 1
            t = datetime.now()
            self.tasks[_id] = {"id": _id,
                               "description": name,
                               "status": STATUS.TODO,
                               "createdAt": t,
                               "updatedAt": t}
            with open('tasks.json', 'w') as fp:
                json.dump(self.tasks, fp)
            print("Task added successfully (ID: {})".format(_id))
        else:
            print("Unable to add the task (no name provided)")

    def update_task(self, _id, name):
        if _id in self.tasks:
            if name:
                self.tasks[_id]["description"] = name
                self.tasks[_id]["updatedAt"] = datetime.now()
                print("Task updated successfully")
            else:
                print("Unable to update the task (no name provided)")
        else:
            print("Unable to update the task (invalid ID)")

    def list_tasks(self, flag):
        for i in self.tasks.values:
            if flag and flag == i["status"]:
                print("ID: {}\nDescribtion: {}\n STATUS: {}\nCreated At: {}\nUpdated At: {}".format(i["id"],
                                                                                                    i["description"],
                                                                                                    flag,
                                                                                                    i["createdAt"],
                                                                                                    i["updatedAt"]))

            elif not flag:
                print("ID: {}\nDescribtion: {}\n STATUS: {}\nCreated At: {}\nUpdated At: {}".format(i["id"],
                                                                                                    i["description"],
                                                                                                    i["status"],
                                                                                                    i["createdAt"],
                                                                                                    i["updatedAt"]))

    def mark_task(self, _id, mark):
        if _id in self.tasks:
            if mark in STATUS:
                self.tasks[_id]["status"] = mark
            else:
                print("Unable to update status: wrong mark (it must be done/in-progress/todo)")
        else:
            print("Unable to update status: invalid ID")


if __name__ == "__main__":
    tm = TaskManager()
