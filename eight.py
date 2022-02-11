# name = input('Enter Your Name : ')
# age = int(input("Enter Your Age {0} : ".format(name)))
#
# if age >= 18:
#     print("You Can Vote")
# else:
#     print("You Can't Vote Wait For {0} Years".format(18-age))

print("Kindly Guess The Number B/W 1 to 10")
num = int(input())

if num < 5:
    print('Kindly Guess The Higher Value')
    num = int(input())
    if num == 5:
        print('You Have Guess The Correct Number')
    else:
        print('You Have Guess Incorrect Number')
elif num > 5:
    print('Kindly Guess The Lower Value')
    num = int(input())
    if num == 5:
        print('You Have Guess The Correct Number')
    else:
        print('You Have Guess Incorrect Number')
else:
    print('Correct Attempt On First Time')