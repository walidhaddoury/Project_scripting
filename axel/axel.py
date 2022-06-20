letters = str(input("Entrez string:"))


def split_letters(string):
    return list(string)


def convert_letter_to_ascii(string):
    array = []
    for letter in split_letters(string):
        array.append(ord(letter))
    return array


print(convert_letter_to_ascii(letters))
