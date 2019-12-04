def get_task_status_text(percent):
    if percent == 0:
        return "To do"
    elif percent < 100:
        return "In progress"
    else:
        return "Done"
    
#print (get_task_status_text(0))
#print (get_task_status_text(60))
#print (get_task_status_text(100))


print("Available options:")
print("1. List tasks for today.")
print("2. List all tasks.")
print("3. Update task status.")
print("4. Create task.")
print("5. Exit")
select = int(input("Please, select required option: "))
print(select)
while (True):
    if select == 1:
        get_tasks_for_today = tasks_received
        tasks_received = [
            [0, 70, "Job 1", "30.09.1992"],
            [1, 100, "Job 2", "1.06.1992"],
            [2, 0, "Job 3", "23.05.2001"]
        ]
        print(list(tasks_received)
        # get_tasks_for_today
    # elif select == 2:
    #     get_all_tasks
    # elif select == 3:
    #     print(input("Please, enter task id: "))
    #     get_selected_task
    #     print(input("Please enter task progress: "))
    #     get_updated_task
    # elif select == 4:
    #     print(input("Please enter new task here: \n"))
    #     add_task
    # else:
    #     break
