def perform_operation (num1 ,num2 ,operation):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'division' and num2 == 0:
         raise ValueError("Error: Division by zero is not allowed")
    elif operation == 'division':
        return num1 / num2
    else:
        return "you must choose from these operation only(+,-,*,/)"