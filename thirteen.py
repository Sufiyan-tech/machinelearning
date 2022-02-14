string = '0123456789'

# for char in string:
#     print(char)

# my_iter = iter(string)
# print(my_iter)
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))

# my_iter = iter(string)
#
# for char in my_iter:
#     print(char)

list = ['Mon','Tues','Wed','Thurs','Fri','Sat','Sun']
my_iter = iter(list)

for i in range(0 , len(list)):
    res = next(my_iter)
    print(res)