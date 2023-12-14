from datetime import datetime
import sys

last_id = 0


class Task:
    def __init__(self, task_name, complete=""):
        self.task_name = task_name
        self.complete = "NO"
        self.date_created = datetime.today().strftime('%d-%m-%y')
        global last_id
        last_id += 1
        self.id = last_id

    def match_task(self, filter):
        return filter.lower() in self.task_name.lower()
    
    def __repr__(self) -> str:
        return (
            f"Task: {self.task_name}, Completed: {self.complete}"
        )


class ToDoList:
    def __init__(self):
        self.tasks = []

    def new_task(self, task_name, complete):
        self.tasks.append(Task(task_name, complete))

    def _find_task(self, task_id):
        for task_name in self.tasks:
            if str(task_name.id) == str(task_name.id):
                return task_name
        return None

    def modify_task(self, task_id, task_name):
        task_name = self._find_task(task_id)
        if task_name:
            task_name.task_name = task_name
            return True
        return False

    def delete_task(self, task_id, complete):
        task = self._find_task(task_id)
        if task:
            task.complete = "YES"
            return self.tasks.remove(task_id-1)
        return False

    def search(self, filter):
        return [task for task in self.tasks if task.match(filter)]
    


class Menu:
    def __init__(self):
        self.toDoList = ToDoList()
        self.choices = {
            "1": self.show_tasks,
            "2": self.search_tasks,
            "3": self.add_tasks,
            "4": self.delete_tasks,
            "5": self.quit,
        }

    def display_menu(self):
        print(
            """
            To Do List menu
            ===============

            1. Show all Tasks 
            2. Search Tasks
            3. Add Tasks
            4. Delete Tasks
            5. Quit

            """

        )

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter an option")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print(f"{choice} is not valid choice")

    def show_tasks(self, tasks=None):
        if not tasks:
            tasks = self.toDoList.tasks
        for task in tasks:
            print(f"{task.id}: {task}")

    def search_tasks(self):
        filter = input("Search tasks:")
        tasks = self.toDoList.search(filter)
        self.show_tasks(tasks)

    def add_tasks(self):
        task_name = input("Enter a task:")
        self.toDoList.new_task(task_name, complete="NO")
        print("Your task has been added:")

    def delete_tasks(self):
        id = input("Enter a task id:")
        task = input("Enter task name:")
        if task:
            self.toDoList.delete_task(id, task)

    def quit(self):
        print("Thank you for using To-Do-List today")
        sys.exit(0)


if __name__ == "__main__":
    Menu().run()
