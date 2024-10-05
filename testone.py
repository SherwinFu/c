from termcolor import cprint, colored
import random

# Initialize win counters and other variables
staywin = 0
switchwin = 0
totalswitch = 0
totalstay = 0
round_number = 1
choice = ""
action = ""
outcome = ""
table = [['Round', 'Choice', 'Action', 'Outcome']]

# Main game loop for infinite rounds
for _ in range(99999999999999999):
    # Initialize doors with goats
    doors = {'door1': 'goat', 'door2': 'goat', 'door3': 'goat'}

    # Randomly place a car behind one door
    car_door = random.choice(list(doors.keys()))
    doors[car_door] = 'car'

    cprint(colored(f'Round #{round_number}', 'yellow'))
    round_number = round_number + 1

    # Get user's choice
    userselect = input(colored('Input door1 to choose Door1, door2 to choose Door2, door3 to choose Door3 or any other key to quit: ', 'yellow'))

    if userselect not in doors:
        print('Thanks for Playing, Good Bye.')
        break

    # Show a goat behind one of the remaining doors
    remaining_doors = [door for door in doors if door != userselect]
    goat_door = random.choice(remaining_doors)

    if doors[goat_door] == 'car':
        # If the goat door was the car, choose the other remaining door
        remaining_doors.remove(goat_door)
        goat_door = remaining_doors[0]

    print(colored(f'{goat_door} has a goat behind it.', 'green'))

    # Get user's action to stay or switch
    userselect2 = input(colored('Stay or Switch? Type "switch" to switch, "stay" to stay, or any other key to quit: ', 'cyan'))

    if userselect2 == 'switch':
        if doors[userselect] == 'goat':
            print('You switched... You Win!')
            switchwin += 1
            totalswitch += 1
            outcome = 'win'
        else:
            print('You switched... You Lose!')
            totalswitch += 1
            outcome = 'lose'

    elif userselect2 == 'stay':
        if doors[userselect] == 'car':
            print('You stayed... You Win!')
            totalstay += 1
            staywin += 1
            outcome = 'win'
        else:
            print('You stayed... You Lose!')
            totalstay += 1
            outcome = 'lose'

    else:
        print('Thanks for Playing, Good Bye.')
        break

    # Record the outcome
    listtable = [f'Round {round_number-1}', userselect, userselect2, outcome]
    table.append(listtable)

# Print the results table
for row in table:
    print(row)

# Calculate win percentages
staywinpercent = (staywin / totalstay * 100) if totalstay > 0 else 0
switchwinpercent = (switchwin / totalswitch * 100) if totalswitch > 0 else 0

print(f"Total Wins From Staying: {staywinpercent:.2f}%")
print(f"Total Wins From Switching: {switchwinpercent:.2f}%")
