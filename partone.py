import random
print('Choose: Door 1, Door 2, or Door 3')
doorchoice=int(input('Choose a Door: '))
windoor=(random.randint(1,3))
if windoor == doorchoice:
    print('Sorry, but there was a goat in door',doorchoice)
    exit()
else:
    print('There was a goat in door' )