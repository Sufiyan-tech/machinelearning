def function1():
    print('Knowledge Shelf')

def add():
    var1 = int(input('Enter The Value Of Var 1'))
    var2 = int(input('Enter The Value Of Var 2'))

    var3 = var1+var2

    print('Sum : ',str(var3))

def sub(var1 , var2):
    var3 = var1-var2
    print('Sub:',str(var3))

def multiply():
    var1 = int(input('Enter The Value Of Var 1'))
    var2 = int(input('Enter The Value Of Var 2'))

    var3 = var1*var2
    return var3

def div(var1 , var2):
    var3 = var1/var2

    return var3;

var4 = div(49,9)
print(var4)