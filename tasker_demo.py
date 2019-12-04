import sys
import os

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "LiTaskerDataHandler"))
from DataHandler import *

def get_task_status_text(percent):
    """This function makes a connection between input progress values and task statuses"""
    if percent == 0:
        return "To do"
    elif percent < 100:
        return "In progress"
    else:
        return "Done"

def show_tasks(tasks_list):
    """This function prints tasks from the list in User friendly style""" 
    id_column_width = 4
    progress_column_width = 8
    status_column_width = 11
    description_column_width = 40
    due_date_column_width = 10
    horizontal_line = '-' * (2 + id_column_width + 3 + progress_column_width + 3 + status_column_width + 3 + \
        description_column_width + 3 + due_date_column_width + 2)
    print (horizontal_line) 
    print ("| " + "ID".ljust(id_column_width) + " | " + "Progress".ljust(progress_column_width) + " | " + \
        "Status".ljust(status_column_width) + " | " + "Description".ljust(description_column_width) + " | " + \
            "Due Date".ljust(due_date_column_width) + " |")
    print (horizontal_line) 
    # ljust - is used to return left justified string with width, provided as parameter
    for item in tasks_list:  
            id = item[0]
            progress = item[1]
            status = get_task_status_text(int(progress))
            description = item[2]
            due_date = item[3]
            print ("| " + id.ljust(id_column_width) + " | " + progress.ljust(progress_column_width) + " | " + \
                status.ljust(status_column_width) + " | " + description.ljust(description_column_width) + " | " + \
                due_date.ljust(due_date_column_width) + " |")
    print (horizontal_line) 
    
# create class oblect
dh = DataHandler()

print("Available options:")
print("1. List tasks for today.")
print("2. List all tasks.")
print("3. Update task status.")
print("4. Create task.")
print("5. Exit")
while (True):
    select = int(input("Please, select required option: "))
    if select == 1:
        tasks = dh.get_tasks_for_today()
        show_tasks(tasks)
    elif select == 2:
        tasks = dh.get_all_tasks()
        show_tasks(tasks)
    elif select == 3:
        task_id = input("Please, enter task id: ")
        task_progress = input("Please enter task progress: ")
        dh.update_task(task_id, task_progress)
        print("Good job! Your task progress was successfully updated.")
    elif select == 4:
        add_desc = input("Please enter task description: ")
        add_date = input("Also enter task due date (e.g: 04.12.2001): ")
        dh.add_task(add_desc, add_date)
        print("Your task was successfully added to tasks list!")
    elif select == 5:
        break
print("Thank you for using TaskOrganizer app. Stay organized! :)")