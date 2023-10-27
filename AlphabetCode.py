#ASCIIvalue = ord(input("input a string"))
choice = input("Type 1 to enter a string, type 2 to load a text file: ")
if choice == '1':
    word = input("Please Input a word to be converted with no punctuation: ")
    ConvertedWord = ''
    for char in word:
        ASCIIValue = ord(char)
        print(ASCIIValue)
        

        if (ASCIIValue > 64 and ASCIIValue < 91):
            ASCIIValue = ASCIIValue+13
            if ASCIIValue > 90:
                ASCIIValue = 64+(ASCIIValue-90)
            transChar = chr(ASCIIValue)
            ConvertedWord = ConvertedWord+transChar
        elif (ASCIIValue > 96):
            ASCIIValue = ASCIIValue+13
            if ASCIIValue > 122:
                ASCIIValue = 96+(ASCIIValue-122)
            transChar = chr(ASCIIValue)
            ConvertedWord = ConvertedWord+transChar
        else:
            ConvertedWord = ConvertedWord+char



        
    print("Your encrypted word is: " +ConvertedWord)
elif choice == '2':
    print(":)")
else: print("Invalid Choice!") 

