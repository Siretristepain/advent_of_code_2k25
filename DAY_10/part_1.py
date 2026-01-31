# Ouverture du fichier
with open("DAY_10/input.txt", "r") as f:
	content = [line.split(" {")[0].split(" ") for line in f.readlines()]

"""
At this point, content is a list[list] looking like this :
[['[.##.]', '(3)', '(1,3)', '(2)', '(2,3)', '(0,2)', '(0,1)'], ['[...#.]', '(0,2,3,4)', '(2,3)', '(0,4)', '(0,1,2)', '(1,2,3,4)'], ['[.###.#]', '(0,1,2,3,4)', '(0,3,4)', '(0,1,2,4,5)', '(1,2)']]

Each line of the file is in a list, but we can see that every element are strings.
We want to convert each one into list.
To do this, we use our preprocess_data funtion.

After calling preprocess_data, we have :
[[['.', '#', '#', '.'], [3], [1, 3], [2], [2, 3], [0, 2], [0, 1]], [['.', '.', '.', '#', '.'], [0, 2, 3, 4], [2, 3], [0, 4], [0, 1, 2], [1, 2, 3, 4]], [['.', '#', '#', '#', '.', '#'], [0, 1, 2, 3, 4], [0, 3, 4], [0, 1, 2, 4, 5], [1, 2]]]
"""

def preprocess_data(datas: list[list]):
	for data in datas:
		data[0] = list(data[0][1:-1])
		for i in range(1, len(data)):
			data[i] = convert_to_list(data[i])

	return datas

def convert_to_list(chaine: str) -> list[int]:
	"""
    Function qui prends une chaîne de caractère en entrée et retourne une liste de tous les chiffres qui la compose.
    
    :param chaine: chaîne de caractère de laquelle on souhaite extraire les digits.
    :type chaine: str
    :return my_list (list[int]): liste des entier qui sont compris dans la chaîne.
	
	Ex:
        convert_to_list(chaine='(2,1)')
		--> [2, 1]
    """
	my_list = []

	for car in chaine:
		if car.isdigit():
			my_list.append(int(car))
	return my_list


def toggle(light: str):
	"""
    Function qui permet de switch l'état d'une ``light``.
    Si la ``light`` d'entrée est '.', retourne '#' et inversement.
	    
    :param light: l'état de la ``light`` en entrée (allumé '#' ou éteinte '.').
    :type light: str
	:return type: str
    """
	return '.' if light == '#' else '#'

def press_button(lights: list, button: list[int]):
	"""
    Function qui simule l'appui sur un bouton.
	Lorsque l'on appuie sur un bouton, on change l'état de toute les lampe reliées à ce bouton.
    
    :param lights: Description
    :type lights: list
    :param button: Description
    :type button: tuple[int]
	
	Ex:
	press_button(['.', '#', '#', '.'], [1,2])
	--> ['.', '.', '.', '.']
    """
	for i in button:
		lights[i] = toggle(lights[i])
	return lights

# ==========
# BRUT FORCE
# ==========
import random

def get_random_button(all_buttons: list[list], previous_index_pick: int = -99) -> list:
	"""
	Fonction qui permet de choisir un bouton aléatoire parmi une liste de bouton ``all_buttons``.
	Fait en sorte de ne pas pouvoir sélectionner le bouton à l'index ``previous_index_pick``.
	
	:param all_buttons: liste de tous les boutons disponibles.
	:type all_buttons: list[list]
	:param previous_index_pick: index du bouton "interdit".
	:type previous_index_pick: int
	:return: le bouton choisi aléatoirement et son index
	:rtype: list, int
	"""
	index = previous_index_pick
	while index == previous_index_pick:
		index = random.randint(0, len(all_buttons)-1)

	return all_buttons[index], index

# Call preprocess_data to have good format of datas to work on.
lines = preprocess_data(content)
NB_ATTEMPT = 50000 # Number of attempt per line.
NB_TRY = 10 # Number max of button we want to press by line per attempt (so we suppose the min number of button is always lower than this value).
tot = [] # This list will contains the minimum number of pressed buttons for each line.

for line in lines:
	# Get the final desired position and the list of all available buttons for this line.
	final_position = line[0]
	buttons_line = line[1:]

	min_pressed_button = 99 # Initialize a minimum of button pressed for this line (Arbitrary huge value).
	start_position = ['.'] * len(final_position) # Build a start position, full of '.', long as the final position

	# We will do "NB_ATTEMPT" attempts for this line.
	for attempt_index in range(NB_ATTEMPT):
		# We will work on a start_position copy.
		current_lights = start_position.copy()

		# For each attempt, we will press a maximum of "NB_TRY" button.
		for pressed_iteration in range(NB_TRY):
			# Select a random button and press it.
			if pressed_iteration == 0:
				selected_button, index = get_random_button(all_buttons=buttons_line)
			else:
				selected_button, index = get_random_button(all_buttons=buttons_line, previous_index_pick=index)

			current_lights = press_button(lights=current_lights, button=selected_button)

			# Check if our current_lights after pressed button is equal to our final desired position.
			# If so, we compare the number of pressed button to reach this point with the previous one, if it's lower, we define this value to the new min_pressed_button.
			if current_lights == final_position:
				if pressed_iteration+1 < min_pressed_button:
					min_pressed_button = pressed_iteration+1
					break

	# After all the attempts for each line, we add the min_pressed_button value find to the tot list.
	tot.append(min_pressed_button)

print(tot)
print(f"The sum of each minimum pressed buttons for each line is : {sum(tot)}.")

"""
Here is my output for :
- NB_ATTEMPT = 50000
- NB_TRY = 10

[3, 1, 1, 4, 3, 3, 1, 1, 2, 2, 1, 3, 2, 2, 1, 4, 3, 2, 1, 1, 2, 3, 2, 1, 2, 1, 5, 1, 2, 1, 5, 2, 3, 2, 3, 4, 1, 1, 1, 3, 6, 4, 2, 2, 2, 5, 4, 1, 1, 2, 2, 4, 2, 1, 1, 3, 2, 2, 3, 2, 2, 2, 3, 7, 5, 5, 1, 5, 2, 8, 4, 7, 1, 4, 2, 4, 1, 3, 5, 6, 6, 1, 3, 2, 2, 5, 4, 4, 4, 2, 3, 4, 3, 2, 5, 1, 2, 1, 3, 1, 2, 2, 2, 5, 1, 1, 2, 3, 4, 1, 2, 2, 2, 4, 4, 1, 4, 3, 2, 2, 2, 3, 1, 2, 1, 2, 2, 1, 3, 6, 2, 1, 4, 5, 4, 7, 1, 1, 2, 2, 4, 1, 2, 5, 3, 3, 6, 5, 1, 1, 1, 3, 3, 2, 1, 3, 3, 1, 6, 3, 3, 1, 3, 3, 1, 1, 6, 5, 3, 2, 1]
The sum of each minimum pressed buttons for each line is : 459.
"""


def verification(lights : str, buttons: tuple[list]):
	light_init = ['.', '.', '.', '.']
	light_modif = light_init.copy()
	
	compteur = 0
	for button in buttons:
		compteur += 1
		light_modif = press_button(light_modif, button)	
		verificateur = light_modif == lights
		if verificateur:
			return compteur
		else: 
			continue
	return 'ok'
