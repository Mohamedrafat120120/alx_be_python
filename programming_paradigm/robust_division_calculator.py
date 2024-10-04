def safe_divide(numerator:float, denominator:float):
    try:
        if numerator ==int() and denominator == int():
          return f"The result of the division is {float(numerator)/float(denominator)}"
        else:
            raise ValueError("Error: Please enter numeric values only.")
            
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    
  