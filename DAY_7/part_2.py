# ===============
# Read input file
# ===============

with open("DAY_7/input.txt", "r") as f:
    lines = [list(line.split('\n')[0]) for line in f.readlines()]


# ====
# Loop
# ====

"""
Logic :

When beam reach a splitter, it splits both left and right.
So, if there is 2 posibilities for beam to reach a splitter there's 2 posibilities left and 2 posibilities right.
And so on,...

The idea is to add a new line at the bottom of the file (-> imagine) and go on all the caracter of each line.
When we reach a splitter, lets assume that there is no any splitters under.
So, when we reach a splitter, the beam can't reach bottom on the same column of splitter, but it goes left and right, so we increment +1 for these column.

Ex:

--- Step 1 ---

. . . S . . .
. . . . . . .
. . . . . . .

0 0 0 1 0 0 0


--- Step 2 ---

. . . . . . .
. . . ^ . . .
. . . . . . .

0 0 1 0 1 0 0    --> before it was 0 0 0 1 0 0 0, but we remove the '1' because it's on the same column than the splitter. This '1' possibilitie goes both left and right.


.
.
.

--- Step n ---

. . . | . . .
. . . | . . .
. . . | . . .
. . . | . . .
. . . ^ . . .
. . . . . . .
. . . . . . .

0 0 0 7 0 0 0

--> Lets assume this configuration.
It means that there's 7 possibilities for the beam to reach that splitter.
We change our final line by removing the 7 both at left and right column regards the splitter's column.

So we get:
0 0 7 0 7 0 0

"""

# Initialize our final line, full of zeros
final_line = [0 for i in range(len(lines[0]))]

# We loop over each line
for line in lines:

    # On each line we loop over each caracter
    for i in range(len(line)):
        
        # If the caracter is 'S', this is the beam's source, so we increment +1 in this column
        if line[i] == 'S':
            final_line[i] = 1

        # If the caracter is a splitter, we add it's column value to both left and right columns and put his value to 0
        if line[i] == '^':
            current_value = final_line[i]
            final_line[i-1] = final_line[i-1] + current_value
            final_line[i+1] = final_line[i+1] +current_value
            final_line[i] = 0

print(f"The total number of timelines is : {sum(final_line)}.")
# --> 15093663987272
