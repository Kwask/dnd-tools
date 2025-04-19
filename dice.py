import re
import random

def calc_avg(num_rolls, num_faces, roll_mod):
    return roll_mod + ((num_faces+1)/2)*num_rolls

def calc_max(num_rolls, num_faces, roll_mod):
    return roll_mod + num_faces*num_rolls 

def calc_min(num_rolls, roll_mod):
    return roll_mod + num_rolls

def roll(num_rolls, num_faces, roll_mod):
    sum = 0
    for _ in range(num_rolls):
        sum += random.randint(1, num_faces)
    return sum+roll_mod 

# returns array of tuples with form (roll, num_rolls, num_faces, roll_mod)
def parse(str):
    roll = ()
    pattern = r"(^(\d+)d(100|20|12|10|8|6|4)(?:\+(\d+))?$)"

    match = re.findall(pattern, str)
    if len(match) == 1:
        groups = list(match[0])
        if len(groups[3]) == 0:
            groups[3] = "0" 
        roll = (groups[0], int(groups[1]), int(groups[2]), int(groups[3]))

    return roll

