# ===========================
# Pre-treatment of input file
# ===========================

"""
With my logic, I have to make distinction between space between columns and space inside number.
To do so, I want to add '|' symbol in place of space between columns.
"""

def change_at_index(text: str, index: int, replace_by: str) -> str:
    text_list = list(text)
    text_list[index] = replace_by
    new_text = "".join(text_list)
    return new_text


with open("DAY_6/input.txt", "r") as f:
    symbol_line = [line for line in f.readlines()][-1]

index_need_pipe = []

for i in range(len(symbol_line)):
    if i == 0:
        continue

    if symbol_line[i] != ' ':
        index_need_pipe.append(i-1)

with open("DAY_6/input.txt", "r") as f:
    lines = [line for line in f.readlines()]

with open("DAY_6/input.txt", "w") as f:
    for line in lines:
        for index in index_need_pipe:
            line = change_at_index(text=line, index=index, replace_by='|')
        line = line.replace(' ', 'x')
        f.write(line)

"""
If the input file is:

123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  


Now its:

123|328|x51|64x
x45|64x|387|23x
xx6|98x|215|314
*xx|+xx|*xx|+xx

"""

# ===============
# Read input file
# ===============

with open("DAY_6/input.txt", "r") as f:
    lines = [line.split('|') for line in f.readlines()]


# =========
# Functions
# =========

def remove_all_spaces(line: list) -> list:
    """
    Function to remove all '' element in the given input ``line``.
    
    :param line: the line in which we want to remove all '' element.
    :type line: list
    :returns line (list): the list without ''.
    """

    security = 0
    while '' in line and security < 5000:
        security += 1
        line.remove('')

    return line

def remove_all_line_break(line: list):
    """
    Function to remove all '\n' independant in the given input ``line``.
    
    :param line: the line in which we want to remove all '\n' element.
    :type line: list
    :returns line (list): the list without '\n'.
    """

    security = 0
    while '\n' in line and security < 5000:
        security += 1
        line.remove('\n')

    return line

def check_line_break_on_last_element(line: list):
    """
    Function used to remove the '\n' into the last element on the list ``line``.

    Example:
        check_line_break_on_last_element(line=['abc', 'abc\n'])
        --> ['abc', 'abc']
    
    :param line: the list in which we want to remove the '\n' into the last element.
    :type line: list
    """

    line[-1] = line[-1].split('\n')[0]
    return line

def calculator(nb_1: int, nb_2: int, operator: str):
    """
    Function which makes an operation between ``nb_1`` and ``nb_2``, regards to ``operator``.
    
    :param nb_1: the first number in the calcul.
    :type nb_1: int
    :param nb_2: the second number in the calcul.
    :type nb_2: int
    :param operator: the operator symbol : '+' or '*', otherwise ValueError.
    :type operator: str
    """

    if operator == '+':
        return nb_1 + nb_2
    elif operator == '*':
        return nb_1 * nb_2
    else:
        print(operator)
        raise ValueError
    
# ====================
# Functions for part 2
# ====================

"""
Here's my logic for part 2 :

Considering the following list of number : [123, 45, 6].

To get the desired calcul, we can see 2 steps :

- first, reverse all numbers, which makes : [321, 54, 6]
- then, write each number in "column" format, which makes something like :

3 5 6
2 4
1

So the new list is [356, 24, 1].

Now that we have the good numbers, the compute logic still the same as part 1.
"""
    
def reverse_numbers(numbers: list[str]) -> list[str]:
    """
    Function that reverse all number in ``numbers`` input list.

    Example:
        reverse_numbers([123, 45, 6])
        --> [321, 54, 6]
    
    :param numbers: the list in which we want to reverse numbers.
    :type numbers: list[int]
    :returns reversed_numbers (list[int]): the list with reversed numbers.
    """

    reversed_numbers = []

    for num in numbers:
        # num = str(num)

        reversed_numbers.append(num[::-1])
    
    return reversed_numbers

    
def rearange_numbers(numbers: list[str]) -> list[str]:
    """
    Function that create the new numbers by "writing" the number of ``numbers`` in "column" format.

    Example:
        rearange_numbers(numbers=['123', '45', '6'])
        --> ['146', '25', '3']

        because:
        1 4 6
        2 5
        3
    
    :param numbers: the list of numbers we want to transform by "column" format.
    :type numbers: list[int]
    :returns rearanged_numbers (list[int]): the output list of rearanged numbers.
    """

    rearanged_numbers = ['' for i in range(len(numbers))]

    for num in numbers:
        # num = str(num)

        for i in range(len(num)):
            digit = num[i]

            rearanged_numbers[i] = rearanged_numbers[i] + digit


    # for i in range(len(rearanged_numbers)):
    #     rearanged_numbers[i] = int(rearanged_numbers[i])
    
    return rearanged_numbers

def times_all_element_in_list(my_list: list[int]):
    res = 1

    for elem in my_list:
        res = res * elem

    return res

def search_symbol(text: str) -> str:
    for car in text:
        if car != 'x':
            return car

# Clear the input lists
for line in lines:
    # remove_all_spaces(line)
    remove_all_line_break(line)
    check_line_break_on_last_element(line)


# =========
# Constants
# =========

NB_ROW = len(lines)
NB_COLUMN = len(lines[0])

# ====
# Loop
# ====

# This list will contains the result of the calculation of each column (-> so his length will be equal to the number of column)
results_by_column = []

# # We loop over all the column one by one (so 'i' refers to column)
for i in range(NB_COLUMN):
#     # We get the operator symbol by taking the element 'i' of the last row
    operator = search_symbol(text=lines[NB_ROW-1][i])

    each_number_of_the_column = []

#     # For each column (i), we loop over all the line (so 'j' refers to line)
    for j in range(NB_ROW-1):
        each_number_of_the_column.append(lines[j][i])

#     # First : Reverse all numbers of the column
    each_number_of_the_column = reverse_numbers(numbers=each_number_of_the_column)

#     # Second : Rearange all numbers of the column ("column" format)
    each_number_of_the_column = rearange_numbers(numbers=each_number_of_the_column)

    number_for_calculator = []

    for number in each_number_of_the_column:
        number = number.replace('x', '')

        if number:
            number = int(number)
            number_for_calculator.append(number)

    if operator == '+':
        result_column = sum(number_for_calculator)
    elif operator == '*':
        result_column = times_all_element_in_list(number_for_calculator)

    results_by_column.append(result_column)


print(f"Adding all the column's results give : {sum(results_by_column)}.")
# --> 9608327000261

# if __name__ == '__main__':
#     print(remove_all_spaces(line=lines[0]))
#     print(remove_all_line_break(lines[0]))
