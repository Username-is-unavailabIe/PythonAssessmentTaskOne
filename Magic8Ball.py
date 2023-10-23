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