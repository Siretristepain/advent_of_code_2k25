import math

# ===============
# Read input file
# ===============

with open("DAY_8/input_test.txt", "r") as f:
    lines = [line.split("\n")[0] for line in f.readlines()]


# ======================================
# Create dict : {'point n°' : (X, Y, Z)}
# ======================================

points = {k: tuple(v.split(',')) for k, v in enumerate(lines)}

# =========
# Functions
# =========

def compute_distance(point_1: tuple[str], point_2: tuple[str]) -> float:
    """
    Function to compute the euclidian distance between two points ``point_1`` and ``point_2`` in a 3D space.
    
    :param point_1: tuple of X, Y and Z coordinates of the first point.
    :type point_1: tuple[str]
    :param point_2: tuple of X, Y and Z coordinates of the second point.
    :type point_2: tuple[str]
    :return: the euclidian distance between ``point_1`` and ``point_2``.
    :rtype: float
    """
    return round(math.sqrt( ((int(point_1[0]) - int(point_2[0]))**2) + ((int(point_1[1]) - int(point_2[1]))**2) + ((int(point_1[2]) - int(point_2[2]))**2) ), 2)

def transform_list_of_str_to_list_of_list(mylist: list[str]) -> list[list[int]]:
    """
    Function to transform a list[str] into list[list[int]].

    Example:
        transform_list_of_str_to_list_of_list(mylist= ['0-19', '0-7', '2-13', '7-19', '17-18', '9-12', '11-16', '2-8', '14-19', '2-18'] )

        --> [[0, 19], [0, 7], [2, 13], [7, 19], [17, 18], [9, 12], [11, 16], [2, 8], [14, 19], [2, 18]]
    
    :param mylist: the list we want to transform.
    :type mylist: list[str]
    :return closest_points_tolist (list[list[int]]): the transformed list.
    """
    closest_points_tolist = []
    for couple in mylist:
        left = couple.split('-')[0]
        right = couple.split('-')[1]
        closest_points_tolist.append([int(left), int(right)])

    return closest_points_tolist

# ====
# Loop
# ====

distances = []


for i in range(len(points)-1):
    for j in range(i+1, len(points)):
        distances.append((f"{i}-{j}", compute_distance(point_1=points[i], point_2=points[j])))

"""
At this point, we got a list of tuples named 'distances'.

distance = [('0-1', 787.81), ('0-2', 908.78), ('0-3', 561.72), ('0-4', 723.79), ('0-5', 736.43), ('0-6', 1047.43), ... ]
"""

# We sort distances list by the distances computed (to get the smaller distances at the beginning of the list)
distances.sort(key=lambda x: x[1])

# We get only the 10 first smallest distances (! --> Change to [:1000] for real input.txt file !)
shortest_distances = distances[:10]

# Now the computed distance doesn't matter, we only focus on the point, so we get all the 'tag' points (-> their n° of line in the file)
closest_points = [distance[0] for distance in shortest_distances]

closest_points = transform_list_of_str_to_list_of_list(mylist=closest_points)

"""
At this point, closest_points looks like : [[0, 19], [0, 7], [2, 13], [7, 19], [17, 18], [9, 12], [11, 16], [2, 8], [14, 19], [2, 18]]

--> This is the list of pairs of points with smaller distances.
"""


links = []
"""
links will contains list of each points group. For example :

[[0, 19, 7, 14], [2, 13, 8, 17, 18], [9, 12], [11, 16]]

--> Means there's is 4 groups of points linked, the first have a length of 4, the second 5, and the third and the last one 2.
"""

# We loop over each couple of point in closest_point
for i in range(len(closest_points)):
    couple = closest_points[i]
    left = couple[0]
    right = couple[1]

    left_found = -999
    right_found = -999

    # For each couple of point, we search if it's left/right value is already in links. 
    # And we apply differents strategies in regards of the result.
    for j in range(len(links)):
        if left in links[j]:
            left_found = j
        if right in links[j]:
            right_found = j

    # First Case : left and right are both not found. -> So we just add this couple as a list in our links list.
    if left_found == -999 and right_found == -999:
        links.append(couple)

    # Second Case : left is found but right not. --> So we add right on the list where we found left.
    elif left_found != -999 and right_found == -999:
        links[left_found].append(right)
    
    # Third Case : left is not found but right is found. --> So we add left on the list where we found right.
    elif left_found == -999 and right_found != -999:
        links[right_found].append(left)

    # Fourth Case : Both left and right are found. --> It could means 2 things : both are found in the same list or not.
    elif left_found != -999 and right_found != -999:
        # If both are found in the same list, no need to add them again.
        if left_found == right_found:
            continue
        # If both are found in different list, we combine (fusion) these two lists.
        else:
            links[left_found] = links[left_found] + links[right_found] # --> Combine the two lists
            links.pop(right_found) # --> Remove the duplicate (You know what I means, hard to explain easily)

# print(links)

# Now, links contains a list for each group of points. We sort links to get the longest groups first.
links.sort(key=lambda x: -len(x))

# print(links)

# We times the length of the three first groups of points (-> The 3 longest groups).
result = 1
for link in links[:3]:
    result = result * len(link)

print(f"The result of times length of the 3 longer links is : {result}.")
# --> 42315


# if __name__ == '__main__':
#     print(compute_distance(point_1=('4', '36', '2'), point_2=('10', '23', '12')))
