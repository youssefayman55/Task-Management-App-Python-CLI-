def task():

    # an empty list to store user tasks
    tasks = []

    print("------- Welcome To The Task Managment APP-------")

    # variable to store the number of user tasks 
    total_task = int(input("Enter how many task you want to do = "))

    for i in range( 1 , total_task + 1 ):
        task_name = input(f"Enter task {i} = ") # 1 ,2 ,3 , 4, 5
        tasks.append(task_name)

    print(f"Today's tasks are :\n {tasks}")
    
    while True:


        # the number of operation the user want to do
        operation = int(input("Enter :\n 1-Add\n 2-Update\n 3-Delete\n 4-View\n 5-Stop/Exit :"))
        
        if operation == 1:
            added_task = input("Enter task you want to add :")
            tasks.append(added_task)
            print(f"task {added_task} has been successfully added.....")
            print(f"New Tasks Are :\n {tasks}")

        elif operation == 2:

            # the old task that the user want to update
            old_value = input("Enter the task name you want to update :")

            if old_value in tasks:
                new_value = input("Enter New Task : ")
                index = tasks.index(old_value)
                tasks[index] = new_value
                print(f"Updated Task Has Been Successfully.... Done {new_value}")
                print(f"New Tasks Are :\n {tasks}")
                
        elif operation == 3 :
            deleted_task = input("Enter The Task You Want To Delete :")
            if deleted_task in tasks:
                index = tasks.index(deleted_task)
                del tasks[index]
                print(f"Task {deleted_task} Has Been Successfully Deleted...")
                print(f"New Tasks Are :\n {tasks}")

        elif operation == 4:
            print(f"Your Total Tasks Are : {tasks}")

        elif operation == 5:
            print(f"Closing The Programe...")

        else:
            print("Invalid Input..")

task()