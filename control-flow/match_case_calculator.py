num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))

choose_operation=input("Choose the operation (+, -, *, /):")


match choose_operation:
    
    case  "+":
        print(f"The result is {num1+num2}.")
        
    case  "-":
        print(f"The result is {num1 - num2}.")
        
    case  "*":
        print(f"The result is {num1 * num2}.")
    
    case "/":
        if  num2 ==0:
           print("canot divide by zero")
        else:   
           print(f"The result is {num1/num2}.")    
    case _ :
        print("you must choose from this four operations only (+, -, *, /):")    
            