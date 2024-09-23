task  = input("Enter your task : ").lower()
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case _ if priority == "high" and time_bound == "yes":
        print(f"Reminder: '{task }' This task  is high priority task  that requires immediate attention today! ")
        
    case _ if priority == "low" and time_bound == "no":
        print(f"Note: '{task }' is a low priority task . Consider completing it when you have free time. ")
        
    case _ if priority == "high" and time_bound == "no":
        print(f"Reminder: '{task }' This task  is high priority task  that requires immediate attention next days")
        
    case _ if priority == "low" and time_bound == "yes":
        print(f"Note: '{task }' This task  is low priority task  but time bound so requires immediate attention today!")
        
    case _ if priority == "medium" and time_bound == "yes":
        print(f"Note: '{task }' This task  has a medium priority  but time bound so requires immediate attention today!")
        
    case _ if priority == "medium" and time_bound == "no":
        print(f"Note: '{task }' This task  has medium priority. Consider completing it when you have free time.")
    case _ :
        print("you must enter a task ")    
        
        
        
# task  = input("Enter your task :")
# priority = input("priority(high/medium/low)")
# time_bound = input("Is it time-bound? (yes/no):")

# match priority:
    
#     case "high":
#         reminder=f"this {task } has a high pitiority so it is require to do in the fastest time "  
#     case "medium":
#         reminder=f"this {task } has a medium pitiority so make it in your attention"
#     case "low":
#         reminder=f"this {task } has a low pitiority so it is require to do in any free time"
        
# if time_bound == "yes" and priority =="high":
#     reminder+= f"Reminder: '{task }' is a high priority task  that requires immediate attention today!" 
       
# if time_bound == "no" and priority =="low":
#     reminder+= f"Note: '{task }' is a low priority task . Consider completing it when you have free time."  
# print(reminder)              