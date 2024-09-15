from termcolor import cprint, colored
import random
x = 1
choice = ""
action = ""
outcome = ""
table=[['Round','Choice','Action','Outcome']]

loop= 3
while loop >0:
    door1 = 'goat'
    door2 = 'goat'
    door3 = 'goat'
    
    strings = ["door1", "door2", "door3"]
    randselect = random.choice(strings)
    globals()[randselect]='car'
    print(door1,door2,door3)
    loop = loop - 1


    userselect = str(input(colored('Input door1 to choose Door1, door2 to choose Door2, door3 to choose Door3 or any other key to quit ','yellow')))
    choice = userselect
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
            
    userselect2=input('Stay or Switch, switch to switch, stay to stay, and any other key to quit.')
    action = userselect2

    if userselect2 == 'switch':
        if globals()[userselect] == 'goat':
            print('You switched..... You Win!')
            outcome = 'win'
        else:
            print('You Switched..... You Lose!')
            outcome = 'lose'

    elif userselect2 == 'stay':
            stay=print(globals()[userselect])
            if globals()[userselect] == 'car':
                print('You Stayed..... You Win!')
                outcome = 'win'

            else:
                print('You Stayed..... You Lose!')
                outcome = 'lose'


    else:
        print('Thanks for Playing, Good Bye.')

    listtable=['Round'+str(x),choice,action,outcome]
    table.append(listtable)
    x = x + 1






for row in table:
    print(row)
