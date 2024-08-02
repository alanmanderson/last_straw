import random
import copy
from os import system

names = ['Dad', 'Mom', 'Luke', 'Hazel', 'Willow', 'Elowen']
remaining_names = copy.deepcopy(names)
assigned_names = {}
while len(remaining_names) != 0:
    name = None
    while name not in names:
        name = input("What is your name? ")
        if name in assigned_names:
            print("Name already drawn")
            name = None
    if len(remaining_names) == 1 and remaining_names[0] == name:
        remaining_names = copy.deepcopy(names)
        assigned_names = {}
        print("retry")
        continue
    index = random.randint(0, len(remaining_names)-1)
    selected_name = remaining_names[index]
    while selected_name == name:
        index = random.randint(0, len(remaining_names)-1)
        selected_name = remaining_names[index]
    remaining_names.pop(index)
    assigned_names[name] = selected_name
while True:
    name = None
    while name not in names:
        name = input("Enter your name to see who you drew: ")
    print("You drew: ", assigned_names[name])
    print("Press Enter to clear the screen")
    input()
    system('clear')
print(assigned_names)
