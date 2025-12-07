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

def count_occurrence_in_file(file_path: str, car_to_count: str) -> int:
    """
    Count the number of occurrence of the ``car_to_count``caracter into the file at the ``file_path`` path.
    
    :param file_path: path of the file in which we want to count.
    :type file_path: str
    :param car_to_count: the caracter we want to know the number of occurrence.
    :type car_to_count: str
    :return: the number of occurrence of ``car_to_count`` into the file.
    :rtype: int
    """
    with open(file_path, "r") as f:
        lines = [line.split('\n')[0] for line in f.readlines()]

    combined_lines = ''.join(lines)

    return combined_lines.count(car_to_count)

def convert_all_occurrence_in_file(file_path: str, car_to_convert: str, replace_by: str):
    """
    Function that replace all the occurrence of ``car_to_convert`` by the ``replace_by`` caracter in the ``file_path``file.
    
    :param file_path: path to the file in which we want to do the modifications.
    :type file_path: str
    :param car_to_convert: the target caracter we want to replace.
    :type car_to_convert: str
    :param replace_by: the replacement caracter.
    :type replace_by: str
    """

    with open(file_path, "r") as f:
        lines = [line.split('\n')[0] for line in f.readlines()]

    modified_lines = []

    for line in lines:
        line_copy = line.replace(car_to_convert, replace_by)
        modified_lines.append(line_copy)

    with open(file_path, "w") as f:
        for line in modified_lines:
            f.write(f"{line}\n")

def change_car_by_index(text: str, index: int, replace_by: str) -> str:
    """
    Function to change a caracter represented by its ``index`` in a ``text`` by a ``replace_by``caracter.
    
    :param text: the string in which we want to change a caracter.
    :type text: str
    :param index: the index of the caracter we want to change in the ``text``.
    :type index: int
    :param replace_by: the replacement caracter.
    :type replace_by: str
    :return: the ``text`` with the correction.
    :rtype: str
    """

    text_to_list = list(text)

    text_to_list[index] = replace_by

    return ''.join(text_to_list)

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
    Function that verifies if the point at the ``position`` if an '@' OR an 'x'.
    
    :param position: coordinates of the point to verify.
    :type position: tuple[int, int]
    :return: True if the point at the given ``position`` is '@' or 'x', False otherwise.
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
    
    return lines[y][x] == '@' or lines[y][x] == 'x'

# ====
# Loop
# ====

# We get the number total of rolls in the file at the very begining (-> We will compare it with the number of rolls at the end)
nb_rolls_begin = count_occurrence_in_file(file_path="DAY_4/input.txt", car_to_count="@")

# roll_to_remove_this_turn is a boolean that allows us to know when stop the while loop.
# We initialize it to True to start the while loop but just after we turn it to False.
# It goes to True again only if removing of at least one roll this turn is possible. (otherwise its still at False and the while loop stops).
roll_to_remove_this_turn = True
security = 0 # security is just a counter to avoid infinity while loop
number_total_of_rolls_removed = 0 # --> doesn't work well but not necessary

while roll_to_remove_this_turn and security < 100:
    roll_to_remove_this_turn = False
    security += 1

    # lines_modified is a list that will contains ALL lines (without any change if no possibility to remove any roll in the line, but with 'x' instead of '@' for rolls which wan be remove this turn).
    lines_modified = []
    number_of_rolls_to_remove = 0

    # Read input file
    with open("DAY_4/input.txt", "r") as f:
        lines = [line.split('\n')[0] for line in f.readlines()]

    # We initialize 'y' as the 'line counter' (0 because we start by the first line obviously)
    y = 0

    for line in lines:
        # line_modified is just a copy of the currrent line (We use this to be able to convert '@' to 'x' without damage)
        line_modified = line

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
                    # As the current roll could be remove, we change its representation in the line by 'x'
                    line_modified = change_car_by_index(text=line_modified, index=x, replace_by='x')
                    roll_to_remove_this_turn = True

            x += 1

        lines_modified.append(line_modified)
        # print(number_of_rolls_to_remove)
        # number_total_of_rolls_removed += number_of_rolls_to_remove
        y += 1

    # We rewrite the file line by line with all our modifications (--> all possibles removing rolls are represented by an 'x')
    with open("DAY_4/input.txt", "w") as f:
        for line in lines_modified:
            f.write(f"{line}\n")

    # We call the convert_all_occurrence_in_file() function that convert all 'x' in the file by a '.' in order to do the next iteration of the loop.
    convert_all_occurrence_in_file(file_path="DAY_4/input.txt", car_to_convert="x", replace_by=".")


# print(f"The number total of rolls to remove after all executions is : {number_total_of_rolls_removed}.")

# We get the number total of rolls at the end of the process.
nb_rolls_end = count_occurrence_in_file(file_path="DAY_4/input.txt", car_to_count="@")
print(f"The number total of rolls to remove after all executions is : {nb_rolls_begin - nb_rolls_end}.")
# --> 9280

# if __name__ == '__main__':
#     positions = get_positions_to_check(position=(0, 0))
#     print(positions)
#     for position in positions:
#         print(check_is_roll(position=position))
