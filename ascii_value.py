
character = chr(input("Enter the character : "))


def asciii(char):
    ascii_value = ord(char)
    return ascii_value

value = asciii(character)
print( "The asciii value of  " ,character," is ", value)
