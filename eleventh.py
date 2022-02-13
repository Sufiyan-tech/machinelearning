# var1 = 0
#
# while var1 < 10:
#     print('Var Is {} '.format(var1))
#     var1 += 1


exits = ['north' , 'east' , 'north west']
my_exit = ''

while my_exit not in exits:
    my_exit = input('')
    if my_exit == 'quit':
        print('Game Over')
        break
else:
    print('You Are Done')