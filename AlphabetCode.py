#ASCIIvalue = ord(input("input a string"))
word = input("Please Input a word to be converted with no punctuation: ")
ConvertWord = ''
for char in word:
    ASCIIValue = ord(char)
    print(ASCIIValue)

    if (ASCIIValue > 64 and ASCIIValue < 91):
        ASCIIValue = ASCIIValue+13
        if ASCIIValue > 91:
            ASCIIValue = 64+(ASCIIValue-91)
        transChar = chr(ASCIIValue)
        ConvertWord = ConvertWord+transChar
    elif (ASCIIValue > 96):
         ASCIIValue = ASCIIValue+13
         if ASCIIValue > 122:
             ASCIIValue = 96+(ASCIIValue-122)
         transChar = chr(ASCIIValue)
         ConvertWord = ConvertWord+transChar
    elif char == ' ':
        ConvertWord = ConvertWord+' '
    else:
        print("Invaliud Entry")


    
print(ConvertWord)

