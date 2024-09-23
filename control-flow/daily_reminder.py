task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    
    case "high":
        
        reminder="high priority task"  
    case "medium":
        
        reminder="medium priority task"
    case "low":
        
        reminder="low priority task"
        
if time_bound== "yes" :
    
    reminder= f"Reminder: '{task}' is a "+reminder+" that requires immediate attention today!" 
       
if time_bound== "no" :
    
    reminder= f"Note: '{task}' is a "+reminder+". Consider completing it when you have free time."
    
    
print(reminder)              