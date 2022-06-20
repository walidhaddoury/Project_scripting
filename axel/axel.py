letters = str(input("Entrez string:"))


def split_letters(string):
    """Converting the input to a list.

            Parameters
            ----------
            string : string
                The string linked to the input.

            Returns
            -------
            array
                A string convert in list
            """
    return list(string)


def convert_letter_to_ascii(string):
    """Converting the input to an array of ascii characters.

        Parameters
        ----------
        string : string
            The string linked to the input.

        Returns
        -------
        array
            An ascii character array
        """
    array = []
    for letter in split_letters(string):
        array.append(ord(letter))
    return array


def to_binary(string):
    """Conversion de l'input en un tableau de nombres binaires

        Parameters
        ----------
        string : string
            The string linked to the input.

        Returns
        -------
        array
            An array of binary strings
        """
    array1, array2 = convert_letter_to_ascii(string), []
    for i in array1:
        array2.append(int(bin(i)[2:]))  # [2:] Slice two first characters from the beginning
    return array2


print(to_binary(letters))
