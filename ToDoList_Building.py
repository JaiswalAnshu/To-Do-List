#Making of a ToDoList .


"""
Tasks to be performed for making a To Do List are as follows :-
- Adding Task
- Show Taks 
- Mark Task as done 
- Remove Task
- Update Task
- Exit 

"""
try :
    # Welcoming to the app . 
    print("===== Welcome to the Task Management App ====== \n")
    TasksToBeDone = []


    while True:
        # Asking the user what action he wants to performe .
        ActionToBePerformed = input(" Enter the action to be performed . \n Choose among : \n 1- Add Task \n 2- Delete Task \n 3- Show Task \n 4- Mark Task as done \n 5- Update Task \n 6-Quit : ").lower();


        # Adding and showing Tasks 
        if ActionToBePerformed == "1":
            
            NumberofTasksToBeAdded = int(input("Enter the number of Tasks to be added :"))
        

            for i in range(NumberofTasksToBeAdded) :
                Task = input(f"Enter your task {i+1}: ")
                print(f"Task Added!")

                TasksToBeDone.append(Task)
                i = i+1 ;

            # Printing the list 
            print(" ====== To Do List ======  ")
            for number , letter in enumerate(TasksToBeDone,1):
                print(number , letter );
            
            for i in range(10):

                IfToAddMoreTask= input("Do you want to add any more tasks ? Yes or No : ").lower();
                
                if IfToAddMoreTask == "yes":
                    NewTask= input("Enter your new task to be done :")
                    print(f"Task {NewTask} has been sucessfully added .....  \n ")
                
                    TasksToBeDone.append(NewTask) 

                    print(" ====== To Do List ====== ")

                    for number, task in enumerate(TasksToBeDone,1):
                        print(number, task);
                            
                else :
                    print ("Thanks for Your Response !") 
                    print("\n")
                    break; 
                i +=1 ;

        # Deleting Task
        elif ActionToBePerformed == "2":
            print(" ====== To Do List ======  ")
            for number , letter in enumerate(TasksToBeDone,1):
                print(number , letter );
            
            Task_to_be_deleted = input("Enter the Task you want to delete : ")
            if Task_to_be_deleted in TasksToBeDone:
                Task_to_be_deleted_index = TasksToBeDone.index(Task_to_be_deleted)
                TasksToBeDone.remove(Task_to_be_deleted)
                print("Your Task has been removed sucessfully....")
                print("\n");
            
            else :
                print("Wrong Input \n Try Again !! \n ");

            print("Your Updated To do list is : ")
            for number , task in enumerate(TasksToBeDone ,1 ):
                print ( number , task)

            print("\n");

        # Showing Task           
        elif ActionToBePerformed == "3":
            print("==== Your To Do List ====")
            for range,task in enumerate(TasksToBeDone, 1):
                print(range , task);
            print("\n")

        # Marking Tasks as done .
        elif ActionToBePerformed == "4":
            print("==== Your To Do List is ====")
            for number, task in enumerate(TasksToBeDone,1):
                print(number, task);

            Task_To_be_Marked_Completed = input("Enter the task which is to be marked as Done :")
            print("\n");

            if Task_To_be_Marked_Completed in TasksToBeDone :
                Task_To_be_Marked_Completed_index = TasksToBeDone.index(Task_To_be_Marked_Completed)
                Task_To_be_Marked_Completed += " - done"
                TasksToBeDone[Task_To_be_Marked_Completed_index] = Task_To_be_Marked_Completed;
            
            else :
                print("Wrong Input \n Try Again !! \n ");

            print("==== Your Updated To Do List is ====")
            for number, task in enumerate(TasksToBeDone,1):
                print(number, task);

            print("\n")

        # Updating Task   
        elif ActionToBePerformed == "5":
            print("==== Your To Do List is ====")
            for number , task in enumerate(TasksToBeDone , 1) :
                print(number, task );

            Task_to_be_updated = input("Enter the task you want to Update : ");

            if Task_to_be_updated in TasksToBeDone :
                Task_index = TasksToBeDone.index(Task_to_be_updated)
                Updated_Task = input("Enter the updated task : ")
                TasksToBeDone[Task_index] = Updated_Task ;
                
            else :
                print("Wrong Input")

            print("==== Your Updated To Do List is ====")
            for number, task in enumerate(TasksToBeDone,1):
                print(number, task);

            print("\n")
            


        # Quit 
        elif ActionToBePerformed == "6":
            print("The Program ends here . ")
            break ;

        else :
            print("Incorrect Choice")
            quit ;

except KeyboardInterrupt :
    print("Interupted") ;





