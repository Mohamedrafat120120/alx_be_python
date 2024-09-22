num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))

choose_operation=input("Choose the operation (+, -, *, /):")


match choose_operation:
    
    case _ if choose_operation == "+":
        print(num1 + num2)
        
    case _ if choose_operation == "-":
        print(num1 - num2)
        
    case _ if choose_operation == "*":
        print(num1 * num2)
        
    case _ if choose_operation == "/" and num2 ==0:
        print("canot divide by zero")
    
    case _ if choose_operation == "/":
        print(num1/num2)    
    case _ :
        print("you must choose from this four operations only (+, -, *, /):")    
            