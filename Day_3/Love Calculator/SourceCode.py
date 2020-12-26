
print("Welcome to the Love Calculator!")

name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()

name=name1+name2

a=0
b=0

a+=name.count("t")
a+=name.count("r")
a+=name.count("u")
a+=name.count("e")

b+=name.count("l")
b+=name.count("o")
b+=name.count("v")
b+=name.count("e")

c=a*10+b

if c<10 or c>90:
  print(f"Your score is {c}, you go together like coke and mentos.")
elif c>40 and c<50:
  print(f"Your score is {c}, you are alright together.")
else:
  print(f"Your score is {c}.")
