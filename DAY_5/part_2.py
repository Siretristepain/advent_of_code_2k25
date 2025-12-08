from part_1 import compare_intervals

# ===============
# Read input file
# ===============

with open("DAY_5/input.txt", "r") as f:
    lines = [line.split('\n')[0] for line in f.readlines()]

# We've got a list for the intervals and a list for all ID of ingredients to test
intervals = []
numbers = []

for line in lines:
    if '-' in line:
        intervals.append(line)
    elif line != '':
        numbers.append(line)

# ====
# Loop
# ====

nb_total_of_fresh_ingredients = 0

intervals = compare_intervals(intervals=intervals)

for interval in intervals:
    # The +1 is mandatory because without it, we doen't count the last "slot" of the interval.
    # For example : considering the [10, 20] interval. This interval doesn't have 10 slots (20-10=10) but 11. Indeed : the 10th, the 11th, ... the 20ty.
    nb_total_of_fresh_ingredients += interval[1] - interval[0] + 1

print(f"The number total of potential fresh ingredients is : {nb_total_of_fresh_ingredients}.")
# --> 365804144481581
