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