# ===============
# Read input file
# ===============

with open("DAY_7/input.txt", "r") as f:
    # We get each line as list inside a big list : [ [line1], [line1], ...]. To be more precise, its a list[list[str]]
    lines = [list(line.split('\n')[0]) for line in f.readlines()]

# =========
# Functions
# =========

def get_pipe_index(line: list[str]) -> list[int]:
    """
    Function that returns a list of indexes where '|' (or 'S' for the first line) are found in ``line``list.
    
    :param line: the line in which we search '|'.
    :type line: list[str]
    :return indexes (list[int]): list of indexes where '|' are found in ``line``.
    """
    indexes = []

    for i in range(len(line)):
        if line[i] in ['S', '|']:
            indexes.append(i)

    return indexes

def check_splitter_by_index(line: list[str], index: int) -> bool:
    """
    Function to check if the element at index ``index``in ``line`` list is a splitter ('^') or not.
    
    :param line: the line in which we want to look the indexed element.
    :type line: list[str]
    :param index: the index of the element we want to look for in the ``line``.
    :type index: int
    :return: True if the element is a splitter, False otherwise.
    :rtype: bool
    """
    return line[index] == '^'

def add_pipe(line: list[str], indexes: list[int], replace_by: str = '|') -> list[str]:
    """
    Function that replace all element in ``line`` list by ``replace_by`` caracter if element index is in ``indexes``.
    
    :param line: the line in which we want to replace elements by '|'.
    :type line: list[str]
    :param indexes: the list of indexes of element we want to transform.
    :type indexes: list[int]
    :param replace_by: the replacement caracter ('|' by default)
    :type replace_by: str
    :return line (list[str]): the line after modifications.
    """
    for index in indexes:
        line[index] = replace_by

    return line

def draw_output(lines: list[list[str]], file_path: str) -> bool:
    """
    Function to draw ``lines`` content in a file at ``file_path``.
    
    :param lines: the lines we want to write in file.
    :type lines: list[list[str]]
    :param file_path: path to the file to write in.
    :type file_path: str
    :return: True when finished.
    :rtype: bool
    """
    with open(file_path, "w") as f:
        for line in lines:
            f.write(f"{"".join(line)}\n")

    return True

# ====
# Loop
# ====

NB_LINES = len(lines)

# The number total of splitting
splitting_realized = 0

# We going to go trough all lines (except the last one, but no worry, there isn't splitter on it, so it doesn't matter)
for i in range(NB_LINES-1):

    # Get current line and next_line
    line = lines[i]
    next_line = lines[i+1]

    # This list will contains all the index where we want to draw '|' on next_line
    index_of_pipe_to_draw = []

    # We get all indexes of '|' in our current line
    indexes = get_pipe_index(line=line)

    for index in indexes:
        # For each index of '|' in current line, we check if its corresponding to a splitter ('^') in the next line
        is_splitter = check_splitter_by_index(line=next_line, index=index)

        # If its so --> splitting
        if is_splitter:
            index_of_pipe_to_draw.append(index-1)
            index_of_pipe_to_draw.append(index+1)
            splitting_realized += 1

        # If its not --> the '|' continue straight forward himself
        else:
            index_of_pipe_to_draw.append(index)
    
    # We replace all '.' at index in index_of_pipe_to_draw by '|' in the next line
    next_line = add_pipe(line=next_line, indexes=index_of_pipe_to_draw)


# for line in lines:
#     print(line)

# Draw in an output file.
draw_output(lines=lines, file_path="DAY_7/output_part1.txt")


print(f"The number of splitting is : {splitting_realized}.")
# --> 1573

# if __name__ == '__main__':
    # print(get_pipe_index(line=lines[4]))
    # print(check_splitter_by_index(line=lines[8], index=4))
    # print(lines[0])
    # print(add_pipe(line=lines[0], indexes=[0,1,2]))
