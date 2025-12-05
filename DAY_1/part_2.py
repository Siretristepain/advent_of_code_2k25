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
    start = total
    
    # The sign depends on the letter 'R' or 'L' ('L' means '-' and 'R' means '+')
    sign = 1 if letter == 'R' else -1

    # We add modulo 100 to make the 0-99 element cycle
    next = (total + sign * number) % 100

    # CASE 1: start = 0 and next != 0
    if start == 0 and next != 0:
        return next, number // 100
    
    # CASE 2: start == 0 and next == 0
    if start == 0 and next == 0:
        return next, number // 100
    
    # CASE 3: start != 0 and next == 0
    if start != 0 and next == 0:
        return next, (number // 100) + 1
    
    # CASE 4: start != 0 and next != 0
    if start != 0 and next != 0:
        # We begin by measure the leftover to finish the circle (by left if 'L', right if 'R')
        if letter == 'L':
            leftover = start
        elif letter == 'R':
            leftover = 100 - start

        # If number is greater than the leftover, we know that we pass zero at least one time
        if number > leftover:
            # We can remove the leftover of the value of the number because it is the necessary part to finish the circle.
            # Next, if the number still greater than 100, it means that we can go all around the circle for every 100 units.
            number = number - leftover
            return next, (number // 100) + 1
        
        # If number is lower than the leftover, we know that we cannot finish the circle, so we pass 0 time the zero
        else:
            return next, 0

# ====
# Loop
# ====

dial = 50
nb_zeros = 0

for line in lines:
    dial, zero_to_add = add_line(total=dial, line=line)

    nb_zeros += zero_to_add


print(f"The code is {nb_zeros}.")
# --> not 5108
# --> not 5645
# --> not 5765
# --> not 2981
# --> not 6504
# --> 6305 YEEEES


# if __name__ == '__main__':
#     total = 99
#     a = add_line(total=total, line='R1')
#     print(a)

    # print(pass_by_zero(start=10, number=-110))