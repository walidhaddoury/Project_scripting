letters = str(input("Entrez string"))

def split_letter(string):
    return list(string)

def conver_letter_to_ascii(string):
    array = []
    for letter in split_letter(string):
        array.append(ord(letter))
    return array

print(conver_letter_to_ascii(letters))

