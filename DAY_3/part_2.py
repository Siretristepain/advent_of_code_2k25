# ===============
# Read input file
# ===============

with open("DAY_3/input.txt", "r") as f:
    lines = [line.split('\n')[0] for line in f.readlines()]

# =========
# Functions
# =========
"""
Here's my logic for part 2 :
Example :

Sequence =  " 9   8   7   6   5   4   3   2   1   1   1   1   1   1   1"
Index =       0   1   2   3   4   5   6   7   8   9   10  11  12  13  14
ReverseIndex  -15 -14 -13 -12 -11 -10 -9  -8  -7  -6  -5  -4  -3  -2  -1

The first digit to find have to be in the [9, 8, 7, 6] interval because we need at least 11 digits remaining at his right.
So, we have to search for the first digit in the [:-11] sequence interval.

The second one have to be search in the [index_first+1: -10].

The third : [index_second+1: -9].

etc...

-> So for the n digit search, we have to search in [index_of_previous_n +1, -11 + iteration]
"""

def search_max_value_and_get_index(sequence: str, val_to_find: str = '9', digits_to_skip_from_end: int = 11, iteration: int = 0, start_from: int = -1):
    """
    Docstring pour search_max_value_and_get_index
    
    :param sequence: Description
    :type sequence: str
    :param val_to_find: Description
    :type val_to_find: str
    :param digits_to_skip_from_end: Description
    :type digits_to_skip_from_end: int
    :param iteration: Description
    :type iteration: int
    :param start_from: Description
    :type start_from: int
    """

    # Case of the last turn of loop (when iteration=11, it makes 11-11=0). --> no need to put right limit for the last digit to find (unit digit).
    if iteration == digits_to_skip_from_end:
        interval_for_search = sequence[start_from+1:]
    else:
        interval_for_search = sequence[start_from+1: -digits_to_skip_from_end+iteration]

    # We search for the max value on the good interval.
    position = interval_for_search.find(val_to_find)

    # Case in which the val_to_find is not in the sequence (-> so recall the function and search the value below with the same parameters to keep the same interval)
    if position == -1:
        return search_max_value_and_get_index(sequence=sequence, val_to_find=str(int(val_to_find)-1), iteration=iteration, start_from=start_from)
    
    # Keep in mind that your search is on a sub-interval of the entier sequence. So the index find is not mandatory the real index in the sequence.
    # To get the good index, we sum the index found for n (+1 because Python start count to 0) with the index of the previous digit found (n-1).
    position = start_from + position + 1

    # When we have the correct max value, we return it's value and it's position
    return val_to_find, position

# ====
# Loop
# ====

all_joltages = []

for line in lines:
    # This list will contains all digit found step by step. Something like : ['9', '7', '9', '5', ...]
    joltage_of_line = []

    # We initiate the first pos to -1 (because I have to put the 'start_from' parameter in the search_max_value_and_get_index() call and the first time I want it to -1 (like the default value)).
    pos = -1
    for i in range(12): # -> We know that all joltage has composed of 12 digits
        val, pos = search_max_value_and_get_index(
            sequence=line,
            iteration=i,
            start_from=pos,
        )

        # We put the digit found in the list.
        joltage_of_line.append(val)
    
    # We combine all the digits found for this line into one big 12-digit number and we put it into the list of all joltages
    all_joltages.append(int(''.join(joltage_of_line)))


print(f"The sum of all max joltage of each line is : {sum(all_joltages)}.")
# --> 167384358365132
    
# if __name__ == '__main__':
    # for line in lines:
        # print(search_max_value_and_get_index(sequence=line))
        # print(search_max_value_and_get_index(sequence=line, val_to_find='9', skip_last_position=False))