FAHRENHEIT_TO_CELSIUS_FACTOR=5/9
CELSIUS_TO_FAHRENHEIT_FACTOR=9/5

def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    print(f"{fahrenheit} °F is {celsius:.2f} °C")
    
    
def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    fahrenheit = celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32
    print(f"{celsius} °C is {fahrenheit:.2f} °F")

temperature = int(input("Enter the temperature to convert: "))

celsius_or_fahrenheit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()   

 
match celsius_or_fahrenheit:
    case "C":
        convert_to_celsius(temperature)
    case "F":
        convert_to_fahrenheit(temperature)
    
    case _:
        raise ValueError ("Invalid temperature. Please enter a numeric value.")        

