'''# A = []  
# A.append(input("Enter your task: "))
# A.append(input("Enter your task: "))       # first try without loop for frame 
# A.append(input("Enter your task: ")) 
# A.append(input("Enter your task: ")) 
# print(A)'''

# A = []

# n = int(input("Enter the numbers of task: "))  # no of task

# for i in range(n):
#     task = input(f"Enter your task {i+1}: ")   # loop to add task in list
#     A.append(task)

# print("\nyour to-do list: ")
# for i ,task in enumerate(A,start=1):           # show each task number wise with to do list print
#     print(f"{i}. {task}")


tasks = []

def show_tasks():
    """Display the to-do list."""
    if not tasks:
        print("\nYour To-Do List is empty!")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

while True:
    print("\nOptions:")
    print("1. Add a Task")
    print("2. Remove a Task")
    print("3. Show To-Do List")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        task = input("Enter your task: ")
        tasks.append(task)
        print("Task added!")

    elif choice == "2":
        show_tasks()
        try:
            task_num = int(input("Enter task number to remove: "))
            if 1 <= task_num <= len(tasks):
                removed_task = tasks.pop(task_num - 1)
                print(f"Task '{removed_task}' removed!")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid number!")

    elif choice == "3":
        show_tasks()

    elif choice == "4":
        print("Exiting... Have a productive day! ✅")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 4.")

M = []

def show_M():
    if not M:
        print("\nyour list is empty")
    else:
        print("\nYour To-Do List:")
        for i, M in enumerate(M, start=1):
            print(f"{i}. {M}")

while True:
    print("\nYour option: ")
    print("1. Add a Task")
    print("2. Remove a Task")
    print("3. Show To-Do List")
    print("4. Exit")
    choice = input("Enter fro 1 to 4")

    if choice == "1":
        M = input("Enter your task")
        M.append(M)
    
    elif choice == "2":
        print()
