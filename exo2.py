letters = str(input("Entrez string:"))

'''
params letter 
return array string ["", "" ]
'''
def split_letters(string):
    return list(string)

'''
params letter 
return array ascii  [66, 65, ... ]
'''
def convert_letter_to_ascii(string):
    array = []
    for letter in split_letters(string):
        array.append(ord(letter))
    return array

'''
params letter 
return array binary ["", "" ]
'''
def to_binary(string):
    array1, array2 = convert_letter_to_ascii(string), []
    for i in array1:
        array2.append(int(bin(i)[2:]))  # [2:] Slice two first characters from the beginning
    return array2


print(to_binary(letters))