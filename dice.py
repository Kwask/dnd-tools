import re

def calc_avg(num_rolls, num_faces, roll_mod):
    return roll_mod + ((num_faces+1)/2)*num_rolls

def calc_max(num_rolls, num_faces, roll_mod):
    return roll_mod + num_faces*num_rolls 

def calc_min(num_rolls, roll_mod):
    return roll_mod + num_rolls

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

def display(str):
    words = str.split(' ')
    for word in words:
        dice_roll = parse(word)
        
        if len(dice_roll) == 4:
            roll = dice_roll[0]
            num_rolls = dice_roll[1]
            num_faces = dice_roll[2]
            roll_mod = dice_roll[3] 

            min_roll = calc_min(num_rolls, roll_mod)
            max_roll = calc_max(num_rolls, num_faces, roll_mod)
            avg_roll = calc_avg(num_rolls, num_faces, roll_mod)

            print_str = "- {} -\nAverage: {}\nMax: {}\nMin: {}\n"
            print(print_str.format(roll, avg_roll, max_roll, min_roll))
        else:
            print("Invalid string " + word + "\n") 

