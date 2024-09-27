FAHRENHEIT_TO_CELSIUS_FACTOR=5/9
CELSIUS_TO_FAHRENHEIT_FACTOR=9/5

def convert_to_celsius(fahrenheit) :
    print(f"{fahrenheit} °F is {fahrenheit * CELSIUS_TO_FAHRENHEIT_FACTOR} °C ")
    
    
def convert_to_fahrenheit(celsius) :
    print(f"{celsius} °C is {celsius * FAHRENHEIT_TO_CELSIUS_FACTOR} °F ")

temperature = int(input("Enter the temperature to convert: "))

celsius_or_fahrenheit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")   

 
match celsius_or_fahrenheit:
    case "C":
        convert_to_fahrenheit(temperature)
    case "F":
        convert_to_fahrenheit(temperature)
    
    case _:
        raise ValueError ("you must enter a valid temperature")        

