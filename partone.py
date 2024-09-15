from termcolor import cprint, colored
import random
door1 = 'goat'
door2 = 'goat'
door3 = 'goat'
strings = ["door1", "door2", "door3"]
randselect = random.choice(strings)
globals()[randselect]='car'
print(door1,door2,door3)


userselect = str(input(colored('Input door1 to choose Door1, door2 to choose Door2, door3 to choose Door3 or any other key to quit ','yellow')))

cprint(colored('Round #1','yellow'))
if userselect in ("door1", "door2", "door3"):
    print('continue')
else:
    print('Thanks for Playing, Good Bye.')
    exit()
    

stringremoved = [s for s in strings if s != userselect]
goatselect = random.choice(stringremoved)
print(stringremoved)
if globals()[goatselect] == 'car':
    stringremoved = [s for s in strings if s != goatselect]
    goatselect = random.choice(stringremoved)

else:
    print(' ')
print(goatselect,globals()[goatselect])
        
userselect2=input('Stay or Switch, w to switch, s to stay, and any other key to quit.')
if userselect2 == 's':
    if globals()[userselect] == 'car':
        print('You Switched..... You Win!')
    else:
        print('You Switched..... You Lose!')
elif userselect2 == 'w':
        stay=print(globals()[userselect])
        if globals()[userselect] == 'goat':
            print('You Stayed..... You Win!')
        else:
            print('You Stayed..... You Lose!')

else:
    print('Thanks for Playing, Good Bye.')