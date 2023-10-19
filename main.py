a = []
while 1 == 1:
    input_variable = input('Enter the next number: ')
    if input_variable == '':
        break
    else:
        a.append(int(input_variable))


target = int(input('Enter the target number: '))


def sum_of_two(self, ):
    for i in a:
        if a[i] + a[- 1] == target:
            print(i, len(a))
            break

    a.pop()
    sum_of_two(a)


sum_of_two(a)
print(a)

