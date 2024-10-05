import random
def cpuplay():
    
    strings = ["door1", "door2", "door3"]

    randdoorselect = random.choice(strings)
    print(randdoorselect)

    strings2 = ["switch", "stay"]
    randswitchstayselect = random.choice(strings2)
    print(randswitchstayselect)

cpuplay()
    