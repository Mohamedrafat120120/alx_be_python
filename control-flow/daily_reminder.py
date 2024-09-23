task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    
    case "high":
        
        reminder=f"this {task} has a high priority so it is require to do in the fastest time "  
    case "medium":
        
        reminder=f"this {task} has a medium priority so make it in your attention "
    case "low":
        
        reminder=f"this {task} has a low priority so it is require to do in any free time "
        
if time_bound== "yes" and priority =="high":
    
    reminder+= f"Reminder: '{task}' is a high priority task that requires immediate attention today!" 
       
if time_bound== "no" and priority =="low":
    
    reminder+= f"Note: '{task}' is a low priority task. Consider completing it when you have free time."  
    
    
print(reminder)              