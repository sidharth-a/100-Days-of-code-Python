
print("Welcome to Python Pizza Deliveries!")

size = input("What size pizza do you want? S, M, or L ").upper()
add_pepperoni = input("Do you want pepperoni? Y or N ").upper()
extra_cheese = input("Do you want extra cheese? Y or N ").upper()

price = 0
if size=="S":
  price=15
  if add_pepperoni=="Y":
    price+=2
elif size=="M":
  price=20
  if add_pepperoni=="Y":
    price+=3
elif size=="L":
  price=25
  if add_pepperoni=="Y":
    price+=3
if extra_cheese=="Y":
  price+=1
print(f"Your final bill is: ${price}.")
