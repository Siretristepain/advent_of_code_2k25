# ==========================
# Read lines from input file
# ==========================

with open("DAY_1/input.txt", "r") as f:
    lines = [line.split('\n')[0] for line in f.readlines()]

# ========
# Function
# ========

def add_line(total: int, line: str):
    """
    add_line add the number of a ``line`` to the ``total``, depending of the letter (L --> rotate left, R --> rotate right).
    
    :param total: the current total.
    :type total: int
    :param line: the line to add.
    :type line: str
    """

    # Split the line content
    letter = line[0]
    number = int(line[1:])
    
    # The sign depends on the letter 'R' or 'L' ('L' means '-' and 'R' means '+')
    sign = 1 if letter == 'R' else -1

    # We add modulo 100 to make the 0-99 element cycle
    total = (total + sign * number) % 100

    return total

# ====
# Loop
# ====

dial = 50
nb_zeros = 0

for line in lines:
    dial = add_line(total=dial, line=line)

    if dial == 0:
        nb_zeros += 1

print(f"The code is {nb_zeros}.")
# --> 1059


if __name__ == '__main__':
    total = 0
    a = add_line(total=total, line='L1')
    print(a)