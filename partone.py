from termcolor import cprint, colored
import random
staywin = 1
switchwin = 1
totalswitch = 1
totalstay = 1
x = 1
c = 1
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
    loop = loop - 0

    cprint(colored('Round #'+str(c),'yellow'))
    c = c + 1
    userselect = str(input(colored('Input door1 to choose Door1, door2 to choose Door2, door3 to choose Door3 or any other key to quit ','yellow')))
    choice = userselect
       
    if userselect in ("door1", "door2", "door3"):
        pass
    else:
        print('Thanks for Playing, Good Bye.')
        exit()
        

    stringremoved = [s for s in strings if s != userselect]
    goatselect = random.choice(stringremoved)
    if globals()[goatselect] == 'car':
        stringremoved = [s for s in strings if s != goatselect]
        goatselect = random.choice(stringremoved)

    else:
        print(colored({goatselect,globals()[goatselect]},'green'))
            
    userselect2=input(colored('Stay or Switch, switch to switch, stay to stay, and any other key to quit.','cyan'))
    action = userselect2

    if userselect2 == 'switch':
        if globals()[userselect] == 'goat':
            print('You switched..... You Win!')
            switchwin = switchwin + 1
            totalswitch = totalswitch + 1
            outcome = 'win'
            print(' ')

        else:
            print('You Switched..... You Lose!')
            totalswitch = totalswitch + 1
            outcome = 'lose'
            print(' ')

    elif userselect2 == 'stay':
            stay=print(globals()[userselect])
            if globals()[userselect] == 'car':
                print('You Stayed..... You Win!')
                totalstay = totalstay + 1
                staywin = staywin + 1
                outcome = 'win'
                print(' ')

            else:
                print('You Stayed..... You Lose!')
                staywin = staywin + 1
                outcome = 'lose'
                print(' ')


    else:
        print('Thanks for Playing, Good Bye.')

    listtable=['Round'+str(x),choice,action,outcome]
    table.append(listtable)
    x = x + 1






for row in table:
    print(row)
staywinpercent = (staywin/totalstay*100)
switchwinpercent = (switchwin/totalswitch*100)
print("Total Wins with Stay =",staywin)
print("Total Wins with Switch =",switchwin)
print("PR(Winning with Stay)=",staywinpercent,"%")
print("PR(Winning with Switch)=",switchwinpercent,"%")