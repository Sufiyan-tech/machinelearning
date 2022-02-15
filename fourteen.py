# my_Cat = {'size':'fat' ,'color':'gray' , 'disposition':'loud'}
#
# print(my_Cat['size'])

# spam1 = ['cat','rat','dog']
# spam2 = ['dog','rat','cat']
#
# print(spam1==spam2)

# spam1 = {'size':'fat' ,'color':'gray' , 'disposition':'loud'}
# spam2 = {'color':'gray' , 'disposition':'loud','size':'fat'}
#
# print(spam1==spam2)

# spam1 = {'name':'Sufiyan','gender':'M','age':23}
#
# # for v in spam1.values():
# #     print(v)
#
# for v in spam1.keys():
#     print(v)

birthdays = {'Sufiyan':'16 Nov' , 'Areeba':'2 Dec' , 'Shahrukh':'2 Nov'}

while True:
    print('Enter Your Name : ')
    name = input()

    if name == '':
        break

    if name in birthdays:
        print(birthdays[name] , ' is the birthday of ' , name)
    else:
        print('There Is No Birthday Info Of ',name)
        print('What Is Your Birthday : ')
        bir = input()
        birthdays[name] = bir
        print('Saved Successfully')