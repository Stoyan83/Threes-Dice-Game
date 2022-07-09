import random


def roll():
    roll_result = []
    for i in range(5):
        roll = random.randint(1, 6)
        roll_result.append(roll)
    return roll_result


# def computer_roll(): 
#     roll_result = []
#     for i in range(5):
#         roll = random.randint(1,4)
#         roll_result.append(roll)
#     return roll_result

def next_roll(dice):
    roll_result = []
    for _ in range(dice):
        roll = random.randint(1, 6)
        roll_result.append(roll)
    return roll_result


def sum_roll_result(roll):
    roll = [x for x in roll if x != 3]
    result = sum(roll)
    return result
