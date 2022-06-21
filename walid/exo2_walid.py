test = ["1000001", "1000011", "100001"]


def complete_octet(array_of_binary):
    """Complete octet if don't have 8 caractere

    Parameter
    ----------
    array_of_binary: array
        With all octet in binary
    Return
    -------
    array
        Octet completed with zero
    """
    for index, octet in enumerate(array_of_binary):
        if len(octet) < 8:
            nb_of_zero = 8 - len(octet)
            i = 0
            while i < nb_of_zero:
                array_of_binary[index] = "0" + array_of_binary[index]
                i += 1
    return array_of_binary


def concat_multiple_string(array):
    """Transform array of octet on string of all octet concated
    Parameter
    ----------
    array: array
        all octets
    Return
    -------
    string
        all octet concated in 1 string
    """
    concat = ''.join(array)
    return concat


finish = complete_octet(test)
print(finish)

concat_octet = concat_multiple_string(finish)
print(concat_octet)
