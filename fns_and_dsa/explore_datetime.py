import datetime
from datetime import date,time

def display_current_datetime():
    current_date = datetime.datetime.now()
    print(f"Current date and time: {current_date}")

display_current_datetime()

number_of_days = int(input("Enter a number of days: "))

def calculate_future_date():
      future_date = datetime.timedelta(days=number_of_days)+datetime.date.today()
      print(future_date)
calculate_future_date()      
    
    
    