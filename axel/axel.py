letters = str(input("Entrez string:"))


def split_letters(string):
    return list(string)


def convert_letter_to_ascii(string):
    array = []
    for letter in split_letters(string):
        array.append(ord(letter))
    return array


def to_binary(string):
    array1, array2 = convert_letter_to_ascii(string), []
    for i in array1:
        array2.append(int(bin(i)[2:]))  # [2:] Slice two first characters from the beginning
    return array2


print(to_binary(letters))
