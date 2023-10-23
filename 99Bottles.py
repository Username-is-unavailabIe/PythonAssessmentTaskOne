number = 99

while number > -1:
    if number == 0:
        print("No more bottles of beer on the wall, no more bottles of beer. Go to the store and buy some more, 99 bottles of beer on the wall.")
    elif number == 1:
        print("1 bottle of beer on the wall, 1 bottle of beer. Take one down and pass it around, no more bottles of beer on the wall.")
    elif number == 2:
        print("2 bottles of beer on the wall, 2 bottles of beer. Take one down and pass it around, 1 bottle of beer on the wall.")
    else:
        print(f"{number} bottles of beer on the wall, {number} bottles of beer. Take one down and pass it around, {number-1} bottles of beer on the wall.")
    print("|_" * number)
    number = number - 1
    
