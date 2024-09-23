# Task = input("Enter your Task:")
# Piriority = input("Piriority(high/medium/low)")
# Time_bound = input("Is it time-bound? (yes/no):")

# match Piriority:
#     case _ if Piriority == "High" and Time_bound == "yes":
#         print(f"'{Task}' This Task is high priority Task that requires immediate attention today! ")
        
#     case _ if Piriority == "low" and Time_bound == "no":
#         print(f"Note: '{Task}' is a low priority Task. Consider completing it when you have free time. ")
        
#     case _ if Piriority == "high" and Time_bound == "no":
#         print(f"Note: '{Task}' This Task is high priority Task that requires immediate attention next days")
        
#     case _ if Piriority == "low" and Time_bound == "yes":
#         print(f"Note: '{Task}' This Task is low priority Task but time bound so requires immediate attention today!")
        
#     case _ if Piriority == "medium" and Time_bound == "yes":
#         print(f"Note: '{Task}' This Task has a medium priority  but time bound so requires immediate attention today!")
        
#     case _ if Piriority == "medium" and Time_bound == "no":
#         print(f"Note: '{Task}' This Task has medium priority. Consider completing it when you have free time.")
#     case _ :
#         print("you must enter a Task")    
        
        
        
Task = input("Enter your Task:")
Piriority = input("Piriority(high/medium/low)")
Time_bound = input("Is it time-bound? (yes/no):")

match Piriority:
    
    case "high":
        reminder=f"this {Task} has a high pitiority so it is require to do in the fastest time "  
    case "medium":
        reminder=f"this {Task} has a medium pitiority so make it in your attention"
    case "low":
        reminder=f"this {Task} has a low pitiority so it is require to do in any free time"
        
if Time_bound == "yes" and Piriority =="high":
    reminder+= f"Reminder: '{Task}' is a high priority task that requires immediate attention today!" 
       
if Time_bound == "no" and Piriority =="low":
    reminder+= f"Note: '{Task}' is a low priority task. Consider completing it when you have free time."  
print(reminder)              