import math

# ===============
# Read input file
# ===============

with open("DAY_2/input.txt", "r") as f:
    intervals = [interval for interval in f.read().split(',')]

# =========
# Functions
# =========

def create_number_good_size(pattern: str, size: int):
    """
    This method returns a integer created from repetition of the input ``pattern`` until his size is equal to the desired input ``size``.

    The method use a security integer to prevent infinity loop during the while loop.

    --> Function used for part2.
    
    :param pattern: the pattern that should compose the number output.
    :type pattern: str
    :param size: the size of the desired output number.
    :type size: int
    :return number (int): the desired number.
    """
    number = pattern
    security = 0

    while len(number) < size and security < 50:
        number += pattern
        security += 1

    return int(number)

def create_number_pattern_twice(pattern: str):
    """
    Function which create a number by repeating twice the given input ``pattern``.

    Function used for part1.
    
    :param pattern: the pattern we want to repeat twice.
    :type pattern: str
    :return number (int): the ouput number compose of repeating the pattern twice.
    """
    number = pattern * 2

    return int(number)

def check_pattern(number: int):
    """
    This method check if a given input ``number`` is compose of repetition of pattern.

    :param number: the given number to check composition.
    :type number: int
    :return True or False (bool): True if pattern in number, False otherwise.
    """

    # The min pattern size is 1 digit.
    # A pattern could not be longer than the half of number size, so the max pattern size is the half longer of number size (round at lower integer for odd number).
    size_number = len(str(number))
    min_size_pattern = 1
    max_size_pattern = math.floor(size_number/2)
    

    for j in range(min_size_pattern, max_size_pattern+1):
        pattern = str(number)[:j]
        
        # === Part 1 ===
        # number_created_by_pattern_twice = create_number_pattern_twice(pattern=pattern)
        # if number_created_by_pattern_twice == number:
        #     return True
        # ==============

        # === Part 2 ===
        number_created_by_pattern = create_number_good_size(pattern=pattern, size=size_number)
        if number_created_by_pattern == number:
            return True
        # ==============
        
    return False

# ====
# Loop
# ====

patterned_numbers = []

for interval in intervals:
    inferior = int(interval.split('-')[0])
    superior = int(interval.split('-')[1])

    print(f"Interval = {inferior} - {superior}")

    for i in range(inferior, superior+1):
        if check_pattern(i):
            patterned_numbers.append(i)


print(f"The sum of all invalid IDs is : {sum(patterned_numbers)}")
# For part 1 : 18595663903
# For part 2 : not 19340547895 (too high)
# For part 2 : 19058204438

# ====
# Test
# ====

if __name__ == '__main__':
    # print(create_number_good_size(pattern="123", size=10))
    print(check_pattern(number=10101))