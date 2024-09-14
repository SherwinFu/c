import random
door1 = 'goat'
door2 = 'goat'
door3 = 'goat'
strings = ["door1", "door2", "door3"]
randselect = random.choice(strings)
globals()[randselect]='car'
print(door1,door2,door3)

print('There are three doors, Door1, Door2 and Door 3.')
userselect = str(input('Input 1 to choose Door1, 2 to choose Door2, 3 to choose Door3 or any other key to quit'))

if userselect in ("1", "2", "3"):
    
    
    