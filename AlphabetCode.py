#ASCIIvalue = ord(input("input a string")) 
 
def ConvertProgram(word): 
    ConvertedWord = '' 
    for char in word: 
        #Converts to ASCII Value
        ASCIIValue = ord(char) 
         #Converts the ASCII value to the converted letter's ASCII value
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
            #Converts the converted ASCII value back to characters
            transChar = chr(ASCIIValue) 
            ConvertedWord = ConvertedWord+transChar 
        else: 
            ConvertedWord = ConvertedWord+char 
    return ConvertedWord 
word = '' 
 
 
choice = input("Type 1 to enter a string, type 2 to load a text file: ") 
if choice == '1': 
    word = input("Please Input a word to be converted with no punctuation: ") 
    
 #Allows the user to open a text file and convert its contents
elif choice == '2': 
    with open(input('What file would you like to open?'), 'r') as file: 
        word = file.read() 
else: print("Invalid Choice!")  
print("Your encrypted word is: " +ConvertProgram(word))  
 
 
 
 
 