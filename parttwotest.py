import random
def cpuplay():
    
    strings = ["door1", "door2", "door3"]

    randdoorselect = random.choice(strings)

    strings2 = ["switch", "stay"]
    randswitchstayselect = random.choice(strings2)
    return randdoorselect, randswitchstayselect

returnedvalues = cpuplay()
print(returnedvalues[0])
print(returnedvalues[1])