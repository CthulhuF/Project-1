list_a = []
while 1 == 1:
    input_variable = input('Enter the next number: ')
    if input_variable == '':
        break
    else:
        list_a.append(int(input_variable))

target = int(input('Enter the target number: '))

a = list_a
print(a)


i = 0
while a:
    if i == (len(a)-1):
        a.pop()
        i = 0

    elif a[-1] + a[i] == target:
        final_answer = [(len(a)-1), i]
        print(final_answer)
        break

    else:
        i += 1
        print('success iteration')

if not a:
    print('no solutions')

