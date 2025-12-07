# ===============
# Read input file
# ===============

with open("DAY_3/input.txt", "r") as f:
    lines = [line.split('\n')[0] for line in f.readlines()]

# =========
# Functions
# =========

def search_max_value_and_get_index(sequence: str, val_to_find: str = '9', skip_last_position: bool = True):
    """
    Recursive function to search the max value into the ``sequence`` given in input and return it's value and index.
    Important : skip_last_position is a boolean that allows us to "skip" the value of the last digit.
                If the position of the max value is the last digit of the sequence and skip_last_position=True, the function search for the value just below.
                Example : if the max value if '9' on the last digit, the method search for an 8, if there is no 8, the method search for
                a 7, etc... (--> The max value doesn't matter if it's in last position).
                If skip_last_position=False on the example, the function returns the '9' at the last position.
    
    :param sequence: the sequence of digit in which we want to search the max value and it's position.
    :type sequence: str
    :param val_to_find: First, the function looks for a '9', if it's not the max value, it's looks for an '8', etc... (--> recursivity).
    :type val_to_find: str
    :default val_to_find: '9'
    :param skip_last_position: if True, the function search on the [:-1] part of the sequence. If False, the function search on all the sequence.
    :type skip_last_position: bool
    :default skip_last_position: True

    :return val_to_find (str): the max value found in the sequence.
    :return position (int): the index of the max value found in the sequence.
    """
    sequence_length = len(sequence)
    position = sequence.find(val_to_find)

    # Case in which the val_to_find is not in the sequence (-> so recall the function and search the value below and keep the same skip_last_position value)
    if position == -1:
        return search_max_value_and_get_index(sequence=sequence, val_to_find=str(int(val_to_find)-1), skip_last_position=skip_last_position)

    # Case in which the max value found is on the last digit of the sequence (--> skip this value if skip_last_position=True, so recall the function to find value below and keep the same skip_last_position value)
    if skip_last_position:
        if position+1 == sequence_length:
            return search_max_value_and_get_index(sequence=sequence, val_to_find=str(int(val_to_find)-1), skip_last_position=True)
    
    # When we have the correct max value, we return it's value and it's position
    return val_to_find, position

# ====
# Loop
# ====

"""
For the part 1, I have chose this logic :
-> search first the tens digit of the joltage. To do so, I search the max value of the sequence but the trick is to skip this value
   if it's index is the last digit of the sequence. Because there would be no digit left on the right to be the unit digit.

-> Once I've got the tens digit, I search for the unit digit but not on all the sequence but only on the remaining digit at the right
   of the tens digit found previously. 
"""

all_joltages = []

for line in lines:
    # First we search for the max value of the sequence and skipping the last position
    tens_digit_value, tens_digit_index = search_max_value_and_get_index(sequence=line)

    # Then, we search for the max value of the sequence in the interval [tens_digit_value : end_of_sequence] (and this time it could be the last digit of the sequence)
    unit_digit_value, unit_digit_index = search_max_value_and_get_index(sequence=line[tens_digit_index+1:], skip_last_position=False)

    # To get the joltage of the line, we combine the tens_digit_value with the unit_digit_value
    joltage = tens_digit_value + unit_digit_value

    all_joltages.append(int(joltage))

print(f"The sum of all max joltage of each line is : {sum(all_joltages)}.")
# --> 16927

# if __name__ == '__main__':
    # for line in lines:
        # print(search_max_value_and_get_index(sequence=line))
        # print(search_max_value_and_get_index(sequence=line, val_to_find='9', skip_last_position=False))