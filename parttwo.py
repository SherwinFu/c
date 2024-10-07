from termcolor import cprint, colored
import random

staywin = 0
switchwin = 0
totalswitch = 0
totalstay = 0
round_number = 1
choice = ""
action = ""
outcome = ""
table = [['Round', 'Choice', 'Action', 'Outcome']]

def cpuplay():
    
    strings = ["door1", "door2", "door3"]

    randdoorselect = random.choice(strings)

    strings2 = ["switch", "stay"]
    randswitchstayselect = random.choice(strings2)
    return randdoorselect, randswitchstayselect
x = 0
for _ in range(10000):
    x = x + 1

    returnedvalues = cpuplay()
    # Initialize doors with goats
    doors = {'door1': 'goat', 'door2': 'goat', 'door3': 'goat'}

    # Randomly place a car behind one door
    car_door = random.choice(list(doors.keys()))
    doors[car_door] = 'car'

    round_number = round_number + 1

    # Get user's choice
    userselect = (returnedvalues[0])

    if userselect not in doors:
        break

    # Show a goat behind one of the remaining doors
    remaining_doors = [door for door in doors if door != userselect]
    goat_door = random.choice(remaining_doors)

    if doors[goat_door] == 'car':
        # If the goat door was the car, choose the other remaining door
        remaining_doors.remove(goat_door)
        goat_door = remaining_doors[0]


    # Get user's action to stay or switch
    userselect2 = (returnedvalues[1])

    if userselect2 == 'switch':
        if doors[userselect] == 'goat':
            switchwin += 1
            totalswitch += 1
            outcome = 'win'
        else:
            totalswitch += 1
            outcome = 'lose'

    elif userselect2 == 'stay':
        if doors[userselect] == 'car':
            totalstay += 1
            staywin += 1
            outcome = 'win'
        else:
            totalstay += 1
            outcome = 'lose'

    else:
        break

    # Record the outcome
    listtable = [f'Round {round_number-1}', userselect, userselect2, outcome]
    table.append(listtable)




    if x == 50:
        staywinpercent50 = (staywin / totalstay * 100) if totalstay > 0 else 0
        switchwinpercent50 = (switchwin / totalstay * 100) if totalstay > 0 else 0
        for row in table:
            print(row)  
    if x == 100:
        staywinpercent100 = (staywin / totalstay * 100) if totalstay > 0 else 0
        switchwinpercent100 = (switchwin / totalstay * 100) if totalstay > 0 else 0
    if x == 500:
        staywinpercent500 = (staywin / totalstay * 100) if totalstay > 0 else 0
        switchwinpercent500 = (switchwin / totalstay * 100) if totalstay > 0 else 0
    if x == 1000:
        staywinpercent1000 = (staywin / totalstay * 100) if totalstay > 0 else 0
        switchwinpercent1000 = (switchwin / totalstay * 100) if totalstay > 0 else 0
    if x == 5000:
        staywinpercent5000 = (staywin / totalstay * 100) if totalstay > 0 else 0
        switchwinpercent5000 = (switchwin / totalstay * 100) if totalstay > 0 else 0
    if x == 10000:
        staywinpercent10000 = (staywin / totalstay * 100) if totalstay > 0 else 0
        switchwinpercent10000 = (switchwin / totalstay * 100) if totalstay > 0 else 0
  

print('')
print('The rest were simulated quietly...')
print('')

print(colored(f"Pr(Wins with Staying 50 trials): {staywinpercent50:.2f}%","green"))
print(colored(f"Pr(Wins with Switching 50 trials): {switchwinpercent50:.2f}%","light_red"))
print(colored(f"Pr(Wins with Staying 100 trials): {staywinpercent100:.2f}%","green"))
print(colored(f"Pr(Wins with Switching 100 trials): {switchwinpercent100:.2f}%","light_red"))
print(colored(f"Pr(Wins with Staying 500 trials): {staywinpercent500:.2f}%","green"))
print(colored(f"Pr(Wins with Switching 500 trials): {switchwinpercent500:.2f}%","light_red"))
print(colored(f"Pr(Wins with Staying 1000 trials): {staywinpercent1000:.2f}%","green"))
print(colored(f"Pr(Wins with Switching 1000 trials): {switchwinpercent1000:.2f}%","light_red"))
print(colored(f"Pr(Wins with Staying 5000 trials): {staywinpercent5000:.2f}%","green"))
print(colored(f"Pr(Wins with Switching 5000 trials): {switchwinpercent1000:.2f}%","light_red"))
print(colored(f"Pr(Wins with Staying 10000 trials): {staywinpercent10000:.2f}%","green"))
print(colored(f"Pr(Wins with Switching 10000 trials): {switchwinpercent10000:.2f}%","light_red"))






