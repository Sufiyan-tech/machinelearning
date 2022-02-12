# name = 'Sufiyan'
#
# while True:
#     print('Enter The Name : ')
#     name1 = input()
#     if name == name1:
#         break
#
# print('Yes ' , name)


name = 'Sufiyan'

while True:
    print('Enter Your Name : ')
    name1 = input()
    if name != name1:
        continue

    print('Enter Your Password : ')
    password = input('')

    if password == '123456':
        break


print('Congratulation')