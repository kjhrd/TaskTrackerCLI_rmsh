from datetime import datetime
import json, argparse
from enum import Enum


class STATUS(Enum):
    TODO = "todo"
    IN_PROGRESS = "in-progress"
    DONE = "done"

    def toJSON(self):
        return json.dumps(
            self,
            default=lambda o: o.__dict__,
            sort_keys=True,
            indent=4)


class TaskManager:
    def __init__(self):
        self.tasks = dict(json.load(open('tasks.json')))

    def add_task(self, name):
        if name:
            _id = len(self.tasks) + 1
            t = str(datetime.now())
            self.tasks[_id] = {"id": _id,
                               "description": name,
                               "status": STATUS.TODO.value,
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
                self.tasks[_id]["updatedAt"] = str(datetime.now())
                with open('tasks.json', 'w') as fp:
                    json.dump(self.tasks, fp)
                print("Task updated successfully")
            else:
                print("Unable to update the task (no name provided)")
        else:
            print("Unable to update the task (invalid ID)")


    def del_task(self, _id):
        if _id in self.tasks:
            del self.tasks[_id]
            with open('tasks.json', 'w') as fp:
                json.dump(self.tasks, fp)
        else:
            print("Unable to delete task: invalid ID")

    def list_tasks(self, flag):
        for i in self.tasks.items():
            i = i[1]
            if flag:
                if flag == i["status"]:
                    print("ID: {}\nDescribtion: {}\nSTATUS: {}\nCreated At: {}\nUpdated At: {}\n".format(i["id"],
                                                                                                        i["description"],
                                                                                                        flag,
                                                                                                        i["createdAt"],
                                                                                                        i["updatedAt"]))

            elif not flag:
                print("ID: {}\nDescribtion: {}\nSTATUS: {}\nCreated At: {}\nUpdated At: {}\n".format(i["id"],
                                                                                                    i["description"],
                                                                                                    i["status"],
                                                                                                    i["createdAt"],
                                                                                                    i["updatedAt"]))

    def mark_task(self, _id, mark):
        if _id in self.tasks:
            if mark in STATUS:
                self.tasks[_id]["status"] = mark
                with open('tasks.json', 'w') as fp:
                    json.dump(self.tasks, fp)
            else:
                print("Unable to update status: wrong mark (it must be done/in-progress/todo)")
        else:
            print("Unable to update status: invalid ID")


if __name__ == "__main__":
    tm = TaskManager()
    parser = argparse.ArgumentParser(
        prog='TASK TRACKER',
        description='You can manage your tasks',
        epilog='idk, bottom text 🥀')
    parser.add_argument('command1')
    parser.add_argument('command2', nargs='?')
    parser.add_argument('command3', nargs='?')
    args = parser.parse_args()
    if args.command1 == "add":
        tm.add_task(args.command2)
    elif args.command1 == "update":
        tm.update_task(args.command2, args.command3)
    elif args.command1 == "delete":
        tm.del_task(args.command2)
    elif args.command1 == "list":
        tm.list_tasks(args.command2)
    elif "mark-" in args.command1:
        tm.mark_task(args.command2, args.command1.replace('mark-', ''))