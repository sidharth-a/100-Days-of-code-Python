print("Welcome to the tip Calculator!")

bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? "))
split = int(input("How many people to split the bill? "))

//Round the final variable into two decimal places
final = round((bill/split)*(1+tip/100),2)

print(f"Each person should pay: ${final}")
