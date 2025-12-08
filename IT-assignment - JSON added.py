import json
import os

Store_file = "tasks.json"

if os.path.exists(Store_file):
    with open(Store_file, "r") as file:
        data = json.load(file)
        To_do_list = data.get("To_do_list", [])
        completed_task = data.get("completed_task", [])

def save_my_tasks():
    data = {
        "To_do_list": To_do_list,
        "completed_task": completed_task

        
    }
    with open(Store_file, "w") as file:
        json.dump(data, file, indent=4)


def add_function():
    add_task = input("Tell me the task you want to add: ")
    To_do_list.append(add_task)
    save_my_tasks()

def remove_function():
    remove_task = input("Tell me the task you want to remove: ")
    if remove_task in To_do_list:
        To_do_list.remove(remove_task)
    else:
        print("Task is not even found. check again!")
    save_my_tasks()

def edit_function():
    original_task = input("Tell me the task you want to edit first: ")
    if original_task in To_do_list:
        edited_task = input("Tell me the task you want to replace it with: ")
        To_do_list.remove(original_task)
        To_do_list.append(edited_task)
    else:
        print("Task is not even found. check again!")
    save_my_tasks()
def exit_function():
    print("Thank you! have a nice day")
    save_my_tasks()


while True:
    print("--- TO-DO-LIST ---")
    print(To_do_list)
    print("--- COMPLETED-TASKS---")
    print(completed_task)
    print("___ MAIN MENU ___ \n 1. Add New Task \n 2. Remove Task \n 3. Edit Task \n 4. Mark Task as Completed \n 5. Exit")

    number_choice = str(input("Enter your choice (1-5): "))

    if number_choice == "1":
        add_function()

    elif number_choice == "2":
        remove_function()

    elif number_choice == "3":
        edit_function()

    elif number_choice == "4":
        task_done = input("Tell me a task you completed: ")
        if task_done in To_do_list:
            To_do_list.remove(task_done)
            completed_task.append(task_done)
            save_my_tasks()
        else:
            print("Task not found! check again. ")

    elif number_choice == "5":
        exit_function()
        break
    

    else:
        print("Invalid input! Enter numbers from 1 - 5! ")
