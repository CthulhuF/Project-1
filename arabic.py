
def int_to_roman(num: int) -> str:
    """
    Transform integer numbers into roman numbers
    (From 1 to 3999)
    :param num:
    :return:
    """
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
    a = 1984
    temp = str(num)
    result = []
    count = len(temp)

    # ones
    if temp[count-1] == '9':
        result.insert(0, 'IX')
    elif int(temp[count-1]) - 5 >= 0:
        result.insert(0, 'V' + (int(temp[count-1]) - 5) * 'I')
    elif int(temp[count-1]) == 4:
        result.insert(0, 'IV')
    else:
        result.insert(0, 'I' * int(temp[count-1]))

    # tens
    if count >= 2:
        if temp[count-2] == '9':
            result.insert(0, 'XC')
        elif int(temp[count-2]) - 5 >= 0:
            result.insert(0, 'L' + (int(temp[count-2]) - 5) * 'X')
        elif int(temp[count-2]) == 4:
            result.insert(0, 'XL')
        else:
            result.insert(0, 'X' * int(temp[count-2]))

    # hundreds
    if count >= 3:
        if temp[count-3] == '9':
            result.insert(0, 'CM')
        elif int(temp[count-3]) - 5 >= 0:
            result.insert(0, 'D' + (int(temp[count-3]) - 5) * 'C')
        elif int(temp[count-3]) == 4:
            result.insert(0, 'CD')
        else:
            result.insert(0, 'C' * int(temp[count-3]))

    # thousands
    if count >= 4:
        result.insert(0, 'M' * int(temp[count-4]))

    return ''.join(result)


while True:

    print(int_to_roman(num=int(input('enter the number: '))))










