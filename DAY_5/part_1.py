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

# =========
# Functions
# =========

def compare_intervals(intervals: list[str]) -> list:
    """
    Function that takes a list of ``intervals`` in input and return a new list of intervals, rearanged by their potential unions.
    
    :param intervals: list of intervals (each interval is a str, for example '3-5')
    :type intervals: list[str]
    :return rearange_intervals (list[int]): list of rearanged intervals (each interval is now a list, for example [3, 5])
    """

    intervals_into_list = [] # List used to convert input intervals list[str] to list[list]
    rearange_intervals = []

    for interval in intervals:
        intervals_into_list.append((int(interval.split('-')[0]), int(interval.split('-')[1])))

    # Fist, we sort the intervals.
    # Then, in the first turn of the loop, we put the first interval into rearange_intervals.
    # Start from the second interval, we compare it's lower limit to the upper limit of the last interval added to rearange_intervals.
    # -> If it's lower limit is lower, it means current interval and last added interval overlap, so the upper limit is the maximum value between upper limit of current interval and upper limit of last added interval.
    # -> If it's upper limit is greater, it means there's no overlap between current interval and last added interval, so we can just added the current interval to the rearange_intervals.
    for begin, end in sorted(intervals_into_list):
        if rearange_intervals and rearange_intervals[-1][1] >= begin - 1:
            rearange_intervals[-1][1] = max(rearange_intervals[-1][1], end)
        else:
            rearange_intervals.append([begin, end])

    return rearange_intervals

def check_number_is_in_interval(number: int, interval: list[int]) -> bool:
    """
    Check if a given input ``number`` is in a given input ``interval``.
    Both interval's limits (lower and upper) are include.
    
    :param number: the number we would check for the presence in the interval.
    :type number: int
    :param interval: the interval in which we would search for the number.
    :type interval: list[int]
    :return: True if ``number`` in ``interval``, False otherwise.
    :rtype: bool
    """

    if number >= interval[0] and number <= interval[1]:
        return True
    return False

# ====
# Loop
# ====

nb_fresh_ingredient = 0

# First we need our corrects intervals
intervals = compare_intervals(intervals=intervals)

# For each ingredient, we check if it's ID is in one interval
for number in numbers:
    number = int(number)

    for interval in intervals:
        if check_number_is_in_interval(number=number, interval=interval):
            nb_fresh_ingredient += 1
            continue

print(f"The number of fresh ingredients is : {nb_fresh_ingredient}.")
# --> 640

# if __name__ == '__main__':
    # print(compare_intervals(intervals=intervals))
    # print(check_number_is_in_interval(number=3, interval=[7,5]))