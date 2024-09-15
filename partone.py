import random
door1 = 'goat'
door2 = 'goat'
door3 = 'goat'
strings = ["door1", "door2", "door3"]

randselect = random.choice(strings)
globals()[randselect]='car'

userselect = str(input('Input door1 to choose Door1, door2 to choose Door2, door3 to choose Door3 or any other key to quit '))

print('Round #1')
if userselect in ("door1", "door2", "door3"):
    goatselect = random.choice(strings)
    print(goatselect,globals()[goatselect])
    userselect2=input('Stay or Switch, w to switch, s to stay, and any other key to quit.')
    if userselect2 == 'w':
        switch=print(globals()[userselect])
        if switch == 'car':
            print('You Switched..... You Win!')
        else:
            print('You Switched..... You Lose!')
    elif userselect2 == 's':
        stay=print(globals()[userselect])
        if stay == 'car':
            print('You Stayed..... You Win!')
        else:
            print('You Stayed..... You Lose!')

    else:
        print('Thanks for Playing, Good Bye.')
        exit()
else:
    print('Thanks for Playing, Good Bye.')
    exit()
    
    