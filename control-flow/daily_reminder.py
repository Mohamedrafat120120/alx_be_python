task = input("Enter your task: ").lower()
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    
    case "high":
        reminder="high priority"  
    case "medium":
        reminder="medium priority"
    case "low":
        reminder="low priority"
        
if time_bound == "yes":
    
    reminder= f"Reminder:'{task }' is a "+reminder+" task that requires immediate attention today!" 
       
if time_bound == "no":
    
    reminder= f"Note:'{task }' is a "+reminder+" task. Consider completing it when you have free time."  
print(reminder)              