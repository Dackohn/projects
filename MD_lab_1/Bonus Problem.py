import random
from colorama import Fore

def apply_rule110(left, center, right):
    if left == 1 and center == 1 and right == 1:
        return 0
    elif left == 1 and center == 1 and right == 0:
        return 1
    elif left == 1 and center == 0 and right == 1:
        return 1
    elif left == 1 and center == 0 and right == 0:
        return 0
    elif left == 0 and center == 1 and right == 1:
        return 1
    elif left == 0 and center == 1 and right == 0:
        return 1
    elif left == 0 and center == 0 and right == 1:
        return 1
    elif left == 0 and center == 0 and right == 0:
        return 0

def generate_rule110(initial_state, generations):
    current_state = initial_state
    for _ in range(generations):
        row = ""
        for cell in current_state:
            if cell == 1:
                row += Fore.RED + chr(0x2588)
            else:
                row += Fore.LIGHTWHITE_EX + chr(0x2588)
        print(row)
        new_state = [0] * len(current_state)
        for i in range(len(current_state)):
            left = current_state[i - 1]
            center = current_state[i]
            right = current_state[(i + 1) % len(current_state)]
            new_state[i] = apply_rule110(left, center, right)
        current_state = new_state

initial_state = [random.choice([0, 1]) for _ in range(150)]

generations = int(input("The number of generations:"))
generate_rule110(initial_state, generations)
