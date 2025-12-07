# ===============
# Read input file
# ===============

with open("DAY_4/input.txt", "r") as f:
    lines = [line.split('\n')[0] for line in f.readlines()]

# =========
# Constants
# =========

# All lines are supposed to have the same length
NB_LINES = len(lines)
NB_CAR = len(lines[0])

# =========
# Functions
# =========

def get_positions_to_check(position: tuple[int, int]) -> list[tuple]:
    """
    This function takes a ``position`` tuple in input and return a list of all the tuples corresponding to the adjacent point of the original ``position``.
    
    :param position: the coordinates of input point (row, column).
    :type position: tuple[int, int]
    :return positions: list of coordinates of all 8 adjacents points.
    :rtype: list[tuple]
    """

    y = position[0]
    x = position[1]

    positions = [
        (y-1, x-1), (y-1, x), (y-1, x+1),
        (y, x-1), (y, x+1),
        (y+1, x-1), (y+1, x), (y+1, x+1),
    ]

    return positions

def check_is_roll(position: tuple[int, int]) -> bool:
    """
    Function that verifies if the point at the ``position`` if an '@'.
    
    :param position: coordinates of the point to verify.
    :type position: tuple[int, int]
    :return: True if the point at the given ``position`` is '@', False otherwise.
    :rtype: bool
    """

    y = position[0]
    x = position[1]

    # Case of line doesn't exists
    if y < 0 or y > NB_LINES-1:
        return False
    
    # Case of element out of range of the line (first/last element)
    if x < 0 or x > NB_CAR-1:
        return False
    
    return lines[y][x] == '@'

# ====
# Loop
# ====

number_of_rolls_to_remove = 0

# We initialize 'y' as the 'line counter' (0 because we start by the first line obviously)
y = 0

for line in lines:

    # We initialize 'x' as the 'caracter counter' into the line (0 because we start by the first caracter of the line obviously)
    x = 0

    for car in line:
        if car == '@':

            # We initialize a counter of adjacents rolls
            rolls_adjacents = 0

            # We get the coordinates of all the adjacents points thanks to get_positions_to_check() function
            positions = get_positions_to_check(position=(y, x))

            for position in positions:
                # For each position, we check if the corresponding point is a roll (@), if so, we increment (+1) the number of adjacent roll.
                is_roll = check_is_roll(position=position)

                if is_roll:
                    rolls_adjacents += 1
            
            # If the number of adjacent roll is below 4, the current roll could be remove
            if rolls_adjacents < 4:
                number_of_rolls_to_remove += 1

        x += 1
    
    y += 1

print(f"The number of rolls that could be remove is : {number_of_rolls_to_remove}.")
# --> 1569

# if __name__ == '__main__':
#     positions = get_positions_to_check(position=(0, 0))
#     print(positions)
#     for position in positions:
#         print(check_is_roll(position=position))
