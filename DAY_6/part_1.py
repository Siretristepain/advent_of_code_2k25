# ===============
# Read input file
# ===============

with open("DAY_6/input.txt", "r") as f:
    lines = [line.split(' ') for line in f.readlines()]


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


# Clear the input lists
for line in lines:
    remove_all_spaces(line)
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

# We loop over all the column one by one (so 'i' refers to column)
for i in range(NB_COLUMN):
    # We get the operator symbol by taking the element 'i' of the last row
    operator = lines[NB_ROW-1][i]

    # If operator is '+', we initialize the result to 0. If the operator is '*', we initialize the result to 1.
    result_column = 0 if operator == '+' else 1

    # For each column (i), we loop over all the line (so 'j' refers to line)
    for j in range(NB_ROW-1):
        result_column = calculator(result_column, int(lines[j][i]), operator=operator)

    results_by_column.append(result_column)


print(f"Adding all the column's results give : {sum(results_by_column)}.")
# --> 4719804927602

# if __name__ == '__main__':
#     print(remove_all_spaces(line=lines[0]))
#     print(remove_all_line_break(lines[0]))
