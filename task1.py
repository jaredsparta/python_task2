from datetime import *
from math import floor

# Asks for name and age and calculates the year they born
name = input("What's your name? ").title()
age = int(input("How old are you? "))
year = datetime.today().year - age

print(f"\nOMG {name} you are {age} years old so you were born in {year} (assuming you've had your birthday)")

day = int(input("\nWhat day were you born? "))
month = int(input("What month were you born (e.g. if born in MAY, input 5)? "))
year = int(input("What was your birth year? "))

# Stores the day, month, year they inputted into a datetime object
# Calculates the age using the current datetime and stores it in a timedelta object
dob = datetime(year, month, day)
age = datetime.today() - dob

# Calculates the age in years and hours
age_years = age / timedelta(days = 365)
age_hours = age / timedelta(hours = 1)

print(f"\nSo you have lived through {age_years} years, making you {floor(age_years)} years old")
print(f"In hours, you are {floor(age_hours)} hours old (to the nearest hour)")