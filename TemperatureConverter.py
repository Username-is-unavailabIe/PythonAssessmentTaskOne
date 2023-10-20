option = input("Type 1 for C to F, 2 for F to C: ")
#selects which type of degrees to convert to and from
if option == "1":
  celsius = input("Enter the degrees celsius to convert: ")
  #attempts to make it so it only tries to run if it is a number otherwise it's invalid
  if celsius.isdigit():
    celsius = int(celsius)
    fahrenheit = (celsius * 9 / 5) + 32
    print(f"{celsius} degrees celsius is {fahrenheit} degrees fahrenheit")
    #tries to make a graphical representation- a thermometer of sorts
    if celsius < 200: print("|" + "*" * int(celsius / 2) + "-" * (50 - int(celsius / 2)) + "|")
  else:
    print("Invalid Input")
elif option == "2":
  f = input("Enter the degrees fahrenheit to convert: ")
  #attempts to make it so it only tries to run if it is a number otherwise it's invalid
  if f.isdigit():
    f = int(f)
    c = (f - 32) * 5 / 9
    print(f"{f} degrees fahrenheit is {c} degrees celsius")
    #tries to make a graphical representation- a thermometer of sorts
    if c < 200: print("|" + "*" * int(c / 2) + "-" * (50 - int(c / 2)) + "|")
  else:
    print("Invalid Input")
else:
  #If neither option is selected it is invalid
  print("Invalid Input")
print("Thankyou for using this program")

import random
from time import sleep

question = input("Please ask your question for the 8Ball: ")
answers = [
    "Yes", "No", "Stars say no", "Certainly", "Why Not!", "Definitely Not"
]

ANS = random.randint(1, len(answers) - 1)
sleep(1)
print("...")

print(f"The answer to '{question}' is {answers[ANS]}")

