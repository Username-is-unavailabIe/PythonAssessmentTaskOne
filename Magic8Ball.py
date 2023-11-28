import random
from time import sleep

#Asks the user for their question
question = input("Please ask your question for the 8Ball: ")

#Different answers that can be randomly selected
answers = [
    "Yes", "No", "Stars say no", "Certainly", "Why Not!", "Definitely Not"
]

ANS = random.randint(1, len(answers) - 1)
for i in range(0,3):
    #Build suspense by waiting 1 second and printing an ellipsis three times
    sleep(1)
    print("...")

#Reveals the randomly generated answer
print(f"The answer to '{question}' is {answers[ANS]}")