word = "APPLE"
position = ''
feedback = []
print(feedback)



def Guess():
    Guess = input("Please Guess a letter!")
    if Guess.upper() in word:
        position = word.find(Guess)
        feedback[position] = Guess
        print(feedback)
Guess()