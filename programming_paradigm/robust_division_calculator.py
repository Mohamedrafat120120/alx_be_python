def safe_divide(numerator:float, denominator:float):
    try:
        return f"The result of the division is {float(numerator)/float(denominator)}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    finally:
        raise ValueError("Error: Please enter numeric values only.")
  