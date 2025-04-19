import dice

def display(str):
    words = str.split(' ')
    for word in words:
        dice_roll = dice.parse(word)
        
        if len(dice_roll) == 4:
            roll = dice_roll[0]
            num_rolls = dice_roll[1]
            num_faces = dice_roll[2]
            roll_mod = dice_roll[3] 

            min_roll = dice.calc_min(num_rolls, roll_mod)
            max_roll = dice.calc_max(num_rolls, num_faces, roll_mod)
            avg_roll = dice.calc_avg(num_rolls, num_faces, roll_mod)

            print_str = "- {} -\nAverage: {}\nMax: {}\nMin: {}\n"
            print(print_str.format(roll, avg_roll, max_roll, min_roll))
        else:
            print("Invalid string " + word + "\n") 

display(input("Please input the die combo: "))

