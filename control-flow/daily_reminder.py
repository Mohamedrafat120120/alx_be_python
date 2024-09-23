task = input("Enter your task:")
piriority = input("Piriority(high/medium/low)")
time_bound = input("Is it time-bound? (yes/no):")

match piriority:
    case _ if piriority == "High" and time_bound == "yes":
        print(f"'{task}' This task is high priority task that requires immediate attention today! ")
        
    case _ if piriority == "low" and time_bound == "no":
        print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time. ")
        
    case _ if piriority == "high" and time_bound == "no":
        print(f"Note: '{task}' This task is high priority task that requires immediate attention next days")
        
    case _ if piriority == "low" and time_bound == "yes":
        print(f"Note: '{task}' This task is low priority task but time bound so requires immediate attention today!")
        
    case _ if piriority == "medium" and time_bound == "yes":
        print(f"Note: '{task}' This task has a medium priority  but time bound so requires immediate attention today!")
        
    case _ if piriority == "medium" and time_bound == "no":
        print(f"Note: '{task}' This task has medium priority. Consider completing it when you have free time.")
    case _ :
        print("you must enter a task")    
        