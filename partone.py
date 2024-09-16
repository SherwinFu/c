from termcolor import cprint, colored
import random
c = 1
x = 1
choice = ""
action = ""
outcome = ""
table=[['Round','Choice','Action','Outcome']]
loopcontinue = "y"
while loopcontinue == "y":
    door1 = 'goat'
    door2 = 'goat'
    door3 = 'goat'
    
    strings = ["door1", "door2", "door3"]
    randselect = random.choice(strings)
    globals()[randselect]='car'
    cprint(colored('Round #'+(str(c)),'yellow'))
    userselect = str(input(colored('Input door1 to choose Door1, door2 to choose Door2, door3 to choose Door3 or any other key to quit ','yellow')))
    choice = userselect
    c = c + 1
    if userselect in ("door1", "door2", "door3"):
        pass
    else:
        loopcontinue = "n"
        print('Thanks for Playing, Good Bye.')
        break

    stringremoved = [s for s in strings if s != userselect]
    goatselect = random.choice(stringremoved)
    if globals()[goatselect] == 'car':
        stringremoved = [s for s in strings if s != goatselect]
        goatselect = random.choice(stringremoved)

    else:
        pass     
    userselect2=input(colored('Stay or Switch, switch to switch, stay to stay, and any other key to quit.','cyan'))
    action = userselect2

    if userselect2 == 'switch':
        if globals()[userselect] == 'goat':
            print('You switched..... You Win!')
            print(' ')
            outcome = 'win'
        else:
            print('You Switched..... You Lose!')
            print(' ')            
            outcome = 'lose'

    elif userselect2 == 'stay':
            stay=print(globals()[userselect])
            if globals()[userselect] == 'car':
                print('You Stayed..... You Win!')
                print(' ')
                outcome = 'win'

            else:
                print('You Stayed..... You Lose!')
                print(' ')
                outcome = 'lose'


    else:
        loopcontinue = "n"
        print('Thanks for Playing, Good Bye.')

    listtable=['Round'+str(x),choice,action,outcome]
    table.append(listtable)
    x = x + 1






for row in table:
    print(row)
