print("Welcome to Calculate your life left")
age = input("What is your current age?")

//Currently I'm asuming the death age as 90
balance = 90-int(age)

//There are 365 days in a year
days = balance*365

//There are 52 weeks in a year
weeks = balance*52

//There are 12 months in a year
months = balance*12

print(f"You have {days} days, {weeks} weeks, and {months} months left.")
