Task = input("Enter your Task:")
Piriority = input("Piriority(high/medium/low)")
Time_bound = input("Is it time-bound? (yes/no):")

match Piriority:
    case _ if Piriority == "High" and Time_bound == "yes":
        print(f"'{Task}' This Task is high priority Task that requires immediate attention today! ")
        
    case _ if Piriority == "low" and Time_bound == "no":
        print(f"Note: '{Task}' is a low priority Task. Consider completing it when you have free time. ")
        
    case _ if Piriority == "high" and Time_bound == "no":
        print(f"Note: '{Task}' This Task is high priority Task that requires immediate attention next days")
        
    case _ if Piriority == "low" and Time_bound == "yes":
        print(f"Note: '{Task}' This Task is low priority Task but time bound so requires immediate attention today!")
        
    case _ if Piriority == "medium" and Time_bound == "yes":
        print(f"Note: '{Task}' This Task has a medium priority  but time bound so requires immediate attention today!")
        
    case _ if Piriority == "medium" and Time_bound == "no":
        print(f"Note: '{Task}' This Task has medium priority. Consider completing it when you have free time.")
    case _ :
        print("you must enter a Task")    
        