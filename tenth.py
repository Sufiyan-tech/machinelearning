# for i in range(20,0,-2):
#     print('i is now {}'.format(i))

numbers = '9,25,355,458,9245,21,22'
cleanedNumber = ''
for i in range(0 , len(numbers)):
    if numbers[i] in '0123456789':
        # print(numbers[i] , end='')
        cleanedNumber = cleanedNumber + numbers[i]

newNumber = int(cleanedNumber)
print('The Values Is {}'.format(newNumber))