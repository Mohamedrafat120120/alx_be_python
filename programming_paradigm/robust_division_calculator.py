def safe_divide(numerator:float, denominator:float):
    try:
        if numerator and denominator == float:
           return f"The result of the division is {numerator/denominator}"
        else:
           raise ValueError ("Error: Please enter numeric values only.")
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

  