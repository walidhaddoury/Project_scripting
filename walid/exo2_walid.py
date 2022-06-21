test = ["1000001", "1000011", "100001"]


def complete_octet(array_of_binary):
    for index, octet in enumerate(array_of_binary):
        if len(octet) < 8:
            nb_of_zero = 8 - len(octet)
            i = 0
            while i < nb_of_zero:
                array_of_binary[index] = "0" + array_of_binary[index]
                i += 1
    return array_of_binary


def concat_multiple_string(array):
    concat = ''.join(array)
    return concat


finish = complete_octet(test)
print(finish)

concat_octet = concat_multiple_string(finish)
print(concat_octet)
