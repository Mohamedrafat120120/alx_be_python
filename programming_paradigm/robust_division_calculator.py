def safe_divide(numerator, denominator):
    try:
        return f"The result of the division is {numerator/denominator}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    else:
        raise ValueError("Error: Please enter numeric values only.")
  