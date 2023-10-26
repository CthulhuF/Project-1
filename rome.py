

def rome_to_arabic(rome_number: str) -> int:
    """
    Function for translate the rome numbers to arabic

    :param rome_number: str
    :return: int
    """
    result = 0
    arabic_interp = []
    rome_equals_arabic = {
        'I': 1,
        'i': 1,
        'V': 5,
        'v': 5,
        'X': 10,
        'x': 10,
        'L': 50,
        'l': 50,
        'C': 100,
        'c': 100,
        'D': 500,
        'd': 500,
        'm': 1000,
        'M': 1000,
    }

    '''translate rome into arabic'''
    for i in range(len(rome_number)):
        if rome_number[i] in rome_equals_arabic:
            arabic_interp.append(rome_equals_arabic[rome_number[i]])
        else:
            return -1

    '''check the rome number for the rules of writing'''
    for i in range(len(arabic_interp) - 1):
        if arabic_interp[i] < arabic_interp[i + 1] and (arabic_interp[i] == 5 or arabic_interp[i] == 50):
            return -1
        elif arabic_interp[i] < arabic_interp[i + 1] and (arabic_interp[i] % 10 == 0 or arabic_interp[i] == 1):
            arabic_interp[i] *= -1
            i += 1

    for i in range(len(arabic_interp)):
        result += arabic_interp[i]
    return result


a = []
temp = 0
list_of_numbers = []

while temp != '':
    temp = input('Enter: ')
    list_of_numbers.append(temp)
else:
    list_of_numbers.pop()

for i in range(len(list_of_numbers)):
    temp = list_of_numbers[i]
    print(rome_to_arabic(temp))
