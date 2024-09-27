FAHRENHEIT_TO_CELSIUS_FACTOR=5/9
CELSIUS_TO_FAHRENHEIT_FACTOR=9/5

def convert_to_celsius(fahrenheit):
    
    return {fahrenheit * CELSIUS_TO_FAHRENHEIT_FACTOR}
    
    
def convert_to_fahrenheit(celsius):
    
    return {celsius * FAHRENHEIT_TO_CELSIUS_FACTOR}

temperature = int(input("Enter the temperature to convert: "))

celsius_or_fahrenheit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")   

 
match celsius_or_fahrenheit:
    case "C":
       print(f"{temperature} °F is {convert_to_celsius(temperature)} °C")
    case "F":
        (f"{temperature} °C is {convert_to_fahrenheit(temperature)} °F")
    
    case _:
        raise ValueError ("you must enter a valid temperature")        

