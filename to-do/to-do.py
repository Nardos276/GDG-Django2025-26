import json
import os


class TodoItem:
    def __init__(self, number, description, is_done=False):
        self.number = number
        self.description = description
        self.is_done = is_done

    # convert object → dictionary
    def convert_to_dict(self):
        return {
            "number": self.number,
            "description": self.description,
            "is_done": self.is_done
        }

    # convert dictionary → object
    @classmethod
    def create_from_dict(cls, info):
        return cls(
            info["number"],
            info["description"],
            info["is_done"]
        )


class TodoStorage:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.todo_list = []
        self.read_file()

    # load JSON file
    def read_file(self):
        if os.path.isfile(self.filename):
            with open(self.filename, "r") as f:
                try:
                    content = json.load(f)
                    for item in content:
                        todo = TodoItem.create_from_dict(item)
                        self.todo_list.append(todo)
                except:
                    self.todo_list = []

    # save JSON file
    def write_file(self):
        data = []
        for todo in self.todo_list:
            data.append(todo.convert_to_dict())

        with open(self.filename, "w") as f:
            json.dump(data, f, indent=4)

    # add new todo
    def create_task(self, description):
        new_number = len(self.todo_list) + 1
        task = TodoItem(new_number, description)
        self.todo_list.append(task)
        self.write_file()
        print("Task successfully added.")

    # show all todos
    def show_all(self):
        if len(self.todo_list) == 0:
            print("No tasks available.")
            return

        print("\nCurrent Tasks:")
        for task in self.todo_list:
            mark = "Done" if task.is_done else "Pending"
            print(f"{task.number}. {task.description} [{mark}]")

    # modify task
    def modify_task(self, number, description=None, status=None):
        found = False

        for task in self.todo_list:
            if task.number == number:
                found = True

                if description is not None:
                    task.description = description

                if status is not None:
                    task.is_done = status

                break

        if found:
            self.write_file()
            print("Task updated.")
        else:
            print("Task does not exist.")

    # remove task
    def remove_task(self, number):
        new_list = []

        for task in self.todo_list:
            if task.number != number:
                new_list.append(task)

        self.todo_list = new_list

        # renumber tasks
        count = 1
        for task in self.todo_list:
            task.number = count
            count += 1

        self.write_file()
        print("Task removed.")


def start_app():
    storage = TodoStorage()

    while True:
        print("\n TODO MANAGER ")
        print("1. Add task")
        print("2. Display tasks")
        print("3. Edit task")
        print("4. Delete task")
        print("5. Quit")

        option = input("Enter option: ")

        if option == "1":
            text = input("Enter description: ")
            storage.create_task(text)

        elif option == "2":
            storage.show_all()

        elif option == "3":
            try:
                num = int(input("Enter task number: "))
            except:
                print("Invalid input.")
                continue

            print("1. Change description")
            print("2. Mark as done")
            print("3. Mark as pending")

            sub = input("Select option: ")

            if sub == "1":
                new_text = input("Enter new description: ")
                storage.modify_task(num, description=new_text)

            elif sub == "2":
                storage.modify_task(num, status=True)

            elif sub == "3":
                storage.modify_task(num, status=False)

        elif option == "4":
            try:
                num = int(input("Enter task number to delete: "))
                storage.remove_task(num)
            except:
                print("Invalid number.")

        elif option == "5":
            print("Exiting program.")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    start_app()
