import os

todo_list = []

if os.path.exists("tasks.txt"):
    with open("tasks.txt", "r", encoding="utf-8") as file:
        for line in file:
            task = line.strip()
            if task:
                todo_list.append(task)

print(f"\nWelcome to to-do-list app!!")

def add_task():
    while True:
        task = input(f"Add the task! (type x to exit)  :  ").strip()
        if task.lower() == "x":
            break
        elif task == "":
            print("task cannot be empty!")
            continue
        else:
            todo_list.append(task)
            save_task()
            print(f"Task {task} added!")

def view_task():
    if not todo_list:
            print(f'Theres no task!!\n')
    else: 
        for i, task in enumerate(todo_list, start=1):
            print(f"{i}. {task}")

def del_task():
        for i, task in enumerate(todo_list, start=1):
            print(f"{i}. {task}")
        if not todo_list:
            print(f'Theres no task to delete!!\n')
            return
        while True:
            try:
                identifier = int(input(f"Which Data would you like to remove? \n(input task number!, 0 to exit) : \n"))
            except ValueError:  
                print(" ⚠️  Please Input a Valid Integer!! \n")
                continue 

            if identifier == 0:
                print(f"Cancelled Deletion.\n")
                break
            if 1 <= identifier <= len(todo_list):
                print(f"Data {todo_list[identifier-1]} is removed! ")
                del todo_list[identifier-1]
                save_task()
                break
            else: 
                print(f"There is no task found! \n Choose between 1 and {len(todo_list)}")
                continue

       
def save_task():
        with open("tasks.txt", "w", encoding="utf-8") as file:
            for task in todo_list:
                file.write(task + "\n")


while True:
    print(f"\nPlease Choose an Option")
    print(f"=== 1. Write a task === ")
    print(f"=== 2. View a task === ")
    print(f"=== 3. Delete a task === ")
    print(f"=== 4. Exit === \n")
    
    option = input(f"Your Option : ")

    if option == "1":
        add_task()
    elif option == "2":
       view_task()
    elif option == "3":
         del_task()
    elif option == "4" :
        print(f"Thank You for Using This Program!!")
        exit()
    else:
         print(f"Wrong Input??\n")
         continue