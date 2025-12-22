# ===============
# Read input file
# ===============

with open("DAY_9/input_test.txt", "r") as f:
    lines = [line.split('\n')[0] for line in f.readlines()]

# Create a dictionary to represent all points.
# Each key is the point's name (-> it's index in the file) and each value is a dictionnary which contains informations about the point.

points = {k : {
        "X_coordinate": int(v.split(',')[0]),
        "Y_coordinate": int(v.split(',')[1]),
        "largest_area": 0,
        "opposite": None,
        "name": k,
    } for k, v in enumerate(lines)
}

"""
For better comprehension, points looks like (for test file) :

(0, {'X_coordinate': 7, 'Y_coordinate': 1, 'largest_area': 0, 'opposite': None, 'name': 0})
(1, {'X_coordinate': 11, 'Y_coordinate': 1, 'largest_area': 0, 'opposite': None, 'name': 1})
(2, {'X_coordinate': 11, 'Y_coordinate': 7, 'largest_area': 0, 'opposite': None, 'name': 2})
(3, {'X_coordinate': 9, 'Y_coordinate': 7, 'largest_area': 0, 'opposite': None, 'name': 3})
(4, {'X_coordinate': 9, 'Y_coordinate': 5, 'largest_area': 0, 'opposite': None, 'name': 4})
(5, {'X_coordinate': 2, 'Y_coordinate': 5, 'largest_area': 0, 'opposite': None, 'name': 5})
(6, {'X_coordinate': 2, 'Y_coordinate': 3, 'largest_area': 0, 'opposite': None, 'name': 6})
(7, {'X_coordinate': 7, 'Y_coordinate': 3, 'largest_area': 0, 'opposite': None, 'name': 7})

"""

# ========
# Function
# ========

def compute_area(point_1: dict, point_2: dict) -> int:
    """
    Compute the area of the Rectangle formed by the ``point_1`` and ``point_2``.
    Notes : we have to add +1 in the delta_y and delta_x compute because Python start to count to 0. So the first row is 0 and the first column is 0 too.
    
    :param point_1: dictionary of informations about ``point_1``.
    :type point_1: dict
    :param point_2: dictionary of informations about ``point_2``.
    :type point_2: dict
    :return: the area of the Rectangle.
    :rtype: int
    """

    # Delta row
    delta_y = abs(point_1.get("Y_coordinate") - point_2.get("Y_coordinate")) +1

    # Delta column
    delta_x = abs(point_1.get("X_coordinate") - point_2.get("X_coordinate")) +1

    return delta_y * delta_x


# ====
# Loop
# ====

# Go through all points and compute the area formed with all other point and keep the largest one
for i in range(len(points)-1):

    # Get the current point
    current_point = points[i]

    # Go through all other points
    for j in range(i+1, len(points)):

        # Get the current opposite point
        opposite_point = points[j]
        
        # Compute the area of the rect formed by current_point and opposite_point
        area = compute_area(point_1=current_point, point_2=opposite_point)
        
        # If the new area computed is larger than the previous one for our current_point, we set it's "largest_area" to the new area value, and set it's opposite point.
        if area > current_point["largest_area"]:
            current_point["largest_area"] = area
            current_point["opposite"] = opposite_point["name"]
        
        # As for the current_point just above, if the new area computed is larger than the previous one for the opposite_point, we set its "largest_area" to the new area value, and set it's opposite point.
        if area > opposite_point["largest_area"]:
            opposite_point["largest_area"] = area
            opposite_point["opposite"] = current_point["name"]

"""
Just to have a good comprehension, at this step, if we do :

for point in points.items():
    print(point)


We have (for the test file):

(0, {'X_coordinate': 7, 'Y_coordinate': 1, 'largest_area': 35, 'opposite': 2, 'name': 0})
(1, {'X_coordinate': 11, 'Y_coordinate': 1, 'largest_area': 50, 'opposite': 5, 'name': 1})
(2, {'X_coordinate': 11, 'Y_coordinate': 7, 'largest_area': 50, 'opposite': 6, 'name': 2})
(3, {'X_coordinate': 9, 'Y_coordinate': 7, 'largest_area': 40, 'opposite': 6, 'name': 3})
(4, {'X_coordinate': 9, 'Y_coordinate': 5, 'largest_area': 24, 'opposite': 6, 'name': 4})
(5, {'X_coordinate': 2, 'Y_coordinate': 5, 'largest_area': 50, 'opposite': 1, 'name': 5})
(6, {'X_coordinate': 2, 'Y_coordinate': 3, 'largest_area': 50, 'opposite': 2, 'name': 6})
(7, {'X_coordinate': 7, 'Y_coordinate': 3, 'largest_area': 25, 'opposite': 2, 'name': 7})

"""

# We sort our dict (-> points) by the "largest_area" value.
# Careful : sorted return a list ! (not a dict)
points = sorted(points.items(), key=lambda x: x[1]["largest_area"], reverse=True)


# Now, points is a list !
print(f"The max area is : {points[0][1]["largest_area"]} composed by points at line {points[0][0]} and at line {points[0][1]["opposite"]}.")
# --> The max area is : 4786902990 composed by points at line 59 and at line 311.

# if __name__ == '__main__':
#     print(compute_area(
#         point_1=points[2],
#         point_2=points[4],
#     ))
