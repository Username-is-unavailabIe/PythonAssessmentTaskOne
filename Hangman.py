import random
score = 0
ComScore = 0
def GetWord():
   ListofWords = ['apple', 'interpolate', 'incredible', 'from', 'tertiary', 'unsuccessful', 'dismay'] 
   return random.choice(ListofWords)

def Guess():
    global WrongGuessTally
    guess = (input("Please enter a letter to guess: ")).upper()
    if guess in wordlist:
        guessindex = (word.index(guess))
        #print(guessindex)
        for i, c in enumerate(word):
            #print(i, c)
            if c == guess:
                hiddenWordList[i] = guess
                #print(hiddenWordList, type(c), type(guess))
    elif guess in Guesses or guess in hiddenWordList:
        print("You have already guessed that letter! try again")
    else:
        print("Incorrect Guess!")
        WrongGuessTally = WrongGuessTally+1
        Guesses.append(guess)
        print(f"Incorrect Guesses So Far: {Guesses}")
        if WrongGuessTally > 9:
            print("Game Over! You lose")
            ComScore = ComScore+1
    print(hiddenWordList)

while True:
    word = GetWord().upper()
    wordlist = list(word)
    print(wordlist)
    hiddenWord= len(word)*'*'
    hiddenWordList=list(hiddenWord)
    WrongGuessTally = 0
    HasWon = False
    Guesses = []
    while WrongGuessTally < 10:
        if HasWon == False: 
            Guess()
            if '*' not in hiddenWordList:
                print("You guessed the word! You win")
                HasWon = True
                score = score+1
        else:
            break
    
    print(f"Score: {score}, computer's score: {ComScore}")

    if input("Would you like to play again? type 'Yes' to do so.") == 'Yes':
        continue
    else:
        break








