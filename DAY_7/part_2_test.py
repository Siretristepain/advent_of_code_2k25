# ========================================================
# Read input file (--> this is the output file of part 1!)
# ========================================================

with open("DAY_7/output_test.txt", "r") as f:
    lines = [list(line.split('\n')[0]) for line in f.readlines()]


"""
The idea is:

The problems looks complex but after reflexion, we just have to count number of '|' of each line with splitter inside.

Example:

.......S.......
.......|.......  
......|^|......  --> 2
......|.|......
.....|^|^|.....  --> 3
.....|.|.|.....
....|^|^|^|....  --> 4
....|.|.|.|....
...|^|^|||^|...  --> 6
...|.|.|||.|...
..|^|^|||^|^|..  --> 7
..|.|.|||.|.|..
.|^|||^||.||^|.  --> 9
.|.|||.||.||.|.
|^|^|^|^|^|||^|  --> 9
|.|.|.|.|.|||.|     ___
                     40
"""

# ====
# Loop
# ====

# total_timelines = 0

# for line in lines:
#     if '^' in line:
#         number_of_pipe_on_current_line = line.count('|')
#         total_timelines += number_of_pipe_on_current_line

# print(f"The number total of timelines is : {total_timelines}.")
# --> not 3108 (too low)

# --> I don't understand why it works for the given example but not for the real input file.


"""
Maybe a '|' count for two in the pattern '^|^' because the beam could pass in the '|' by splitting from left OR from right.
-> NO
"""

def count_possibility_for_line(line: list[list[str]]) -> int:

    nb_possibility = 0

    for i in range(len(line)):
        current_car = line[i]

        if current_car == '|':
            count_for = 1

            # If '|' on first or last digit, it counts for 1 (mandatory)
            if i > 0 and i < len(line)-1:
                previous_car = line[i-1]
                next_car = line[i+1]

                if previous_car == '^' and next_car == '^':
                    count_for = 2
            
            nb_possibility += count_for

    return nb_possibility

total_timelines = 0

for line in lines:
    if '^' in line:
        number_of_pipe_on_current_line = count_possibility_for_line(line=line)
        total_timelines += number_of_pipe_on_current_line

print(f"The number total of timelines is : {total_timelines}.")
# --> not 4204 (too low)