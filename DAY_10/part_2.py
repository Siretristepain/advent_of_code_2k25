import random

# Ouvrir le fichier et récupérer chaque ligne
# Récupérer les données "boutons" et "joltages" proprement, dans des listes.

# Fonction qui créer un dictionnaire qui permet de de regrouper les boutons en fonction des jolt qu'ils touchent.
# Fonction qui permet de savoir si tous les joltages touchés par un bouton sont ok, en fonction d'un état actuel des joltages et d'un état souhaité.
# Fonction qui permet d'appuyer sur un bouton

# =======
# Buttons
# =======

class Button:

    # created_buttons = []

    def __init__(self, name: int, joltages: list[int], remaining: int = 99):
        self.name = name
        self.joltages = joltages
        self.remaining = remaining

        # Button.created_buttons.append(self)

    def __repr__(self):
        return f"{self.name}"

    def press(self, current_joltages: list[int]):
        """
        Method used to press the Button.
        When we press a Button, each jolf of its joltages is increased by 1.
        Before press the Button, verify that there is 'remaining' (self.remaining) left.

        In all the case, return the joltage (with no modification if remaining == 0).
        
        :param self: the Button.
        :param current_joltages: the current state of the joltages (ex: [0,0,0,0] for beginning with 4 jolts).
        :type current_joltages: list[int]
        :return current_joltages (list[int]):
        """
        if self.remaining > 0:
            for i in self.joltages:
                current_joltages[i] += 1
            self.remaining -= 1
        return current_joltages
    
    def compute_correct_remaining(self, organized_buttons: dict, joltages: list[int]):
        """
        Method used to compute the correct ``remaining`` value of the current Button (self).
        This ``remaining`` value corresponds to the number of push we still have before go ahead of the thresold value for jolts impact by this Button.
        
        :param self: current Button instance.
        :param organized_buttons: dictionnary of sorted Buttons, in regards of which index jolt they have impact on.
        :type organized_buttons: dict
        :param joltages: the final joltage schema we want.
        :type joltages: list[int]
        """
        min_remaining = self.remaining
        for key, value in organized_buttons.items():
            if self in value:
                if min_remaining > joltages[key]:
                    min_remaining = joltages[key]
        self.remaining = min_remaining
        return True

    @classmethod
    def set_correct_remaining_for_all_buttons(self, buttons_to_set: list, organized_buttons: dict, joltages: list[int]):
        for button in buttons_to_set:
            button.compute_correct_remaining(organized_buttons=organized_buttons, joltages=joltages)
        return True
    
    # @classmethod
    # def get_random_button(self):
    #     return Button.created_buttons[random.randint(0, len(Button.created_buttons)-1)]

# =============================
# Functions to preprocess datas
# =============================

with open("DAY_10/input_test.txt", "r") as f:
    content = [line.split('\n')[0].split(" ") for line in f.readlines()]

def process_single_line(line: list[str]):
    """
    Docstring pour process_single_line

    Example:
    process_single_line(line= ['[.###.#]', '(0,1,2,3,4)', '(0,3,4)', '(0,1,2,4,5)', '(1,2)', '{10,11,11,5,10,5}'])

    >>> ([[0, 1, 2, 3, 4], [0, 3, 4], [0, 1, 2, 4, 5], [1, 2]], [10, 11, 11, 5, 10, 5])
    
    :param line: Description
    :type line: list[str]
    """
    buttons_raw_datas = line[1:-1]
    joltages_raw_datas = line[-1]

    buttons_data = []

    for but in buttons_raw_datas:
        jolt = [int(car) for car in but if car.isdigit()]
        buttons_data.append(jolt)

    joltages_raw_datas = joltages_raw_datas.replace('{', '')
    joltages_raw_datas = joltages_raw_datas.replace('}', '')

    joltages_data = [int(i) for i in joltages_raw_datas.split(',')]

    return buttons_data, joltages_data

# ==========================
# Functions to solve problem
# ==========================

def create_buttons_for_current_line(input_buttons: list[list]) -> list[Button]:
    """
    Function which create Button instance for each button of the ``input_buttons`` list.
    
    :param input_buttons: list of each buttons of the current line.
    :type input_buttons: list[list]
    :return output_buttons (list[Button]): Button's instances for the current line. 
    """
    ouput_buttons = []
    for i, but in enumerate(input_buttons):
        ouput_buttons.append(Button(name=i, joltages=but))
    return ouput_buttons

def sort_buttons_by_jolt_index(joltages: list[int], buttons: list[Button]):
    """
    Function used to sort ``buttons`` by the jolt's index they impact on.

    Example:
    sort_buttons_by_jolt_index(joltages= [3, 5, 4, 7], buttons= [0, 1, 2, 3, 4, 5]) --> Assume that 0, 1, 2, 3, 4, 5 are Button instances.
    
    >>> {0: [4, 5], 1: [1, 5], 2: [2, 3, 4], 3: [0, 1, 3]}

    It means that buttons 4 and 5 impact jolt at index 0,
    buttons 1 and 5 impact jolt at index 1, ...

    
    :param joltages: Description
    :type joltages: list[int]
    :param buttons: Description
    :type buttons: list[Button]
    """
    sorted_buttons = {k: [] for k in range(len(joltages))}

    for button in buttons:
        for i in range(len(joltages)):
            if i in button.joltages:
                sorted_buttons[i].append(button)

    return sorted_buttons

def get_all_buttons_links_to_current_one(button: Button, sorted_buttons: dict[Button]):
    """
    Function used to get all Buttons links to the current one by joltage impacted.

    Example :
    get_all_buttons_links_to_current_one(button= b1, sorted_buttons= { 0 : [b1, b2], 1 : [b2, b3], 2 : [b1, b2, b4] }):

    >>> [b2, b4]

    The output of the example is [b2, b4] because b2 is link to b1 by the joltage "0" and b4 is link to b1 by joltage "2".

    Note : b1 is not in the output + b2 is not count twice.

    Goals : After call this function, the objective is to decrease by -1 the remaining of each Buttons of the output.
            (the remaining of b1 is already decreased by the "press" method itself, that's why we doens't add b1 to the output).
    
    :param button: the current Button (we pressed on).
    :type button: Button
    :param sorted_buttons: dictionnary of sorted Buttons, by the joltage they have impact on.
    :type sorted_buttons: dict[Button]
    :return linked_buttons list[Button]: list of all the Buttons linked to the input ``button``.
    """
    linked_buttons = []

    for key, value in sorted_buttons.items():
        if button in value:
            for but in value:
                if but != button and but not in linked_buttons:
                    linked_buttons.append(but)

    return linked_buttons

def decrease_remaining_for_given_button(buttons: list[Button]):
    """
    This function allows to decrease by -1 all the remaining properties of each Button instance in the ``buttons`` input list.
    
    :param buttons: list of all the Buttons we want to decrease their remaining value.
    :type buttons: list[Button]
    :return (bool): True
    """
    for button in buttons:
        button.remaining -= 1
        if button.remaining < 0:
            print(f"LOG: Button {button} have a negative remaining !")
    return True

def get_random_button(buttons: list[Button]) -> Button:
    copy_buttons = buttons.copy()
    selected_button = copy_buttons[random.randint(0, len(copy_buttons)-1)]

    # We arbitrary suppose that there is no Button with a correct remaining value
    at_least_one_button_possible = False

    # We go through all Buttons, check it's remaining. If it's greater than 0, we turn our 'at_least_one_button_possible' to True.
    for but in buttons:
        if but.remaining > 0:
            at_least_one_button_possible = True
            break

    if not at_least_one_button_possible:
        return False

    while selected_button.remaining <= 0:
        copy_buttons.remove(selected_button)
        selected_button = copy_buttons[random.randint(0, len(copy_buttons)-1)]

    return selected_button

def delete_all_given_button(buttons: list[Button]):
    buttons.clear()
    return True

def does_we_can_press_a_button(buttons: list[Button]) -> bool:
    response = False

    for but in buttons:
        if but.remaining > 0:
            response = True
            break

    return response

# ==========
# Resolution
# ==========

NB_TRY = 30
SHOW_LOG = True

for line, i in zip(content, range(len(content))):
    # Extract buttons/joltages datas from the current line
    buttons_data, joltages_data = process_single_line(line=line)

    if SHOW_LOG:
        print('^'*15)
        print(f"LOG: ligne n°{i},\nButtons: {buttons_data},\nJoltages: {joltages_data}.\n")

    # Create the Buttons instances for the current line
    buttons = create_buttons_for_current_line(input_buttons=buttons_data)

    if SHOW_LOG:
        print(f"LOG: Created Buttons : {buttons}.")

    # Sort all buttons for the current line by the jolt they have impact on
    sorted_buttons = sort_buttons_by_jolt_index(joltages=joltages_data, buttons=buttons)

    if SHOW_LOG:
        print(f"LOG: sorted Buttons : {sorted_buttons}.")

    # TRY LOOP
    for _try in range(NB_TRY):

        if SHOW_LOG:
            print(f"LOG: --> try n°{_try}.")

        if _try > 0:
            for but in buttons:
                but.remaining = 99

        # Set correct "remaining" for each Button
        Button.set_correct_remaining_for_all_buttons(buttons_to_set=buttons, organized_buttons=sorted_buttons, joltages=joltages_data)

        if SHOW_LOG:
            for but in buttons:
                print(f"LOG: Button {but} --> remaining : {but.remaining}.")

        # Create a start joltages position pattern
        current_joltages = [0 for i in range(len(joltages_data))]

        if SHOW_LOG:
            print(f"LOG: Initialize joltages to : {current_joltages}.")

        # WHILE LOOP
        security = 0
        while does_we_can_press_a_button(buttons=buttons) and security < 100:

            # Get a random Button to press on
            selected_button = get_random_button(buttons=buttons)

            if SHOW_LOG:
                print(f"LOG: the selected Button is {selected_button}, its joltages are : {selected_button.joltages}, its remaining is : {selected_button.remaining}.")

            # Press the Button (it automatically decrease its remaining value)
            current_joltages = selected_button.press(current_joltages=current_joltages)

            if SHOW_LOG:
                print(f"LOG: after press the Button, our current joltages are : {current_joltages}.")

            # Get all Buttons links to the pressed one
            linked_buttons = get_all_buttons_links_to_current_one(button=selected_button, sorted_buttons=sorted_buttons)

            if SHOW_LOG:
                print(f"LOG: we will decrease remaining value for these Buttons : {linked_buttons}")

            # Decrease the remaining value for each of these linked buttons
            decrease_remaining_for_given_button(buttons=linked_buttons)

            if SHOW_LOG:
                print(f"LOG: Decrease DONE.")

            # Check if our current_joltages corresponds to the final joltages pattern desired
            if current_joltages == joltages_data:
                print(security)

                if SHOW_LOG:
                    print(f"=== LOG: We get into the final position in {security+1} press ! ===")
            
            security += 1

        if SHOW_LOG:
            print('v'*15)




if __name__ == '__main__':
    
    # buttons = create_buttons_for_current_line(input_buttons=[[1, 2], [3]])
    # for button in buttons:
    #     print(f"{button.name} --> {button.joltages}")

    # buttons = create_buttons_for_current_line(input_buttons=[[3], [1,3], [2], [2,3], [0,2], [0,1]])
    # print(buttons)
    # dic = sort_buttons_by_jolt_index(joltages=[3, 5, 4, 7], buttons=buttons)
    # print(dic)

    # Button.set_correct_remaining_for_all_buttons(buttons_to_set=buttons, organized_buttons=dic, joltages=[3, 5, 4, 7])

    # for but in buttons:
    #     print(f"{but} --> {but.remaining}")
    # delete_all_given_button(buttons=buttons)
    # print(buttons)
    
    # b1 = Button(name=0, joltages=[1,2])
    # b2 = Button(name=1, joltages=[2,3], remaining=0)

    # print(get_random_button(buttons=[b1, b2]))

    pass


    # [...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
    # [.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}


"""
vvvvvvvvvvvvvvv
LOG: --> try n°20.
LOG: Button 0 --> remaining : 7.
LOG: Button 1 --> remaining : 5.
LOG: Button 2 --> remaining : 4.
LOG: Button 3 --> remaining : 4.
LOG: Button 4 --> remaining : 3.
LOG: Button 5 --> remaining : 3.
LOG: Initialize joltages to : [0, 0, 0, 0].
LOG: the selected Button is 1, its joltages are : [1, 3], its remaining is : 5.
LOG: after press the Button, our current joltages are : [0, 1, 0, 1].
LOG: we will decrease remaining value for these Buttons : [5, 0, 3]
LOG: Decrease DONE.
LOG: the selected Button is 4, its joltages are : [0, 2], its remaining is : 3.
LOG: after press the Button, our current joltages are : [1, 1, 1, 1].
LOG: we will decrease remaining value for these Buttons : [5, 2, 3]
LOG: Decrease DONE.
LOG: the selected Button is 5, its joltages are : [0, 1], its remaining is : 1.
LOG: after press the Button, our current joltages are : [2, 2, 1, 1].
LOG: we will decrease remaining value for these Buttons : [4, 1]
LOG: Decrease DONE.
LOG: the selected Button is 1, its joltages are : [1, 3], its remaining is : 3.
LOG: after press the Button, our current joltages are : [2, 3, 1, 2].
LOG: we will decrease remaining value for these Buttons : [5, 0, 3]
LOG: Button 5 have a negative remaining !
LOG: Decrease DONE.
LOG: the selected Button is 1, its joltages are : [1, 3], its remaining is : 2.
LOG: after press the Button, our current joltages are : [2, 4, 1, 3].
LOG: we will decrease remaining value for these Buttons : [5, 0, 3]
LOG: Button 5 have a negative remaining !
LOG: Decrease DONE.
LOG: the selected Button is 4, its joltages are : [0, 2], its remaining is : 1.
LOG: after press the Button, our current joltages are : [3, 4, 2, 3].
LOG: we will decrease remaining value for these Buttons : [5, 2, 3]
LOG: Button 5 have a negative remaining !
LOG: Button 3 have a negative remaining !
LOG: Decrease DONE.
LOG: the selected Button is 2, its joltages are : [2], its remaining is : 2.
LOG: after press the Button, our current joltages are : [3, 4, 3, 3].
LOG: we will decrease remaining value for these Buttons : [3, 4]
LOG: Button 3 have a negative remaining !
LOG: Button 4 have a negative remaining !
LOG: Decrease DONE.
LOG: the selected Button is 1, its joltages are : [1, 3], its remaining is : 1.
LOG: after press the Button, our current joltages are : [3, 5, 3, 4].
LOG: we will decrease remaining value for these Buttons : [5, 0, 3]
LOG: Button 5 have a negative remaining !
LOG: Button 3 have a negative remaining !
LOG: Decrease DONE.
LOG: the selected Button is 0, its joltages are : [3], its remaining is : 3.
LOG: after press the Button, our current joltages are : [3, 5, 3, 5].
LOG: we will decrease remaining value for these Buttons : [1, 3]
LOG: Button 1 have a negative remaining !
LOG: Button 3 have a negative remaining !
LOG: Decrease DONE.
LOG: the selected Button is 0, its joltages are : [3], its remaining is : 2.
LOG: after press the Button, our current joltages are : [3, 5, 3, 6].
LOG: we will decrease remaining value for these Buttons : [1, 3]
LOG: Button 1 have a negative remaining !
LOG: Button 3 have a negative remaining !
LOG: Decrease DONE.
LOG: the selected Button is 2, its joltages are : [2], its remaining is : 1.
LOG: after press the Button, our current joltages are : [3, 5, 4, 6].
LOG: we will decrease remaining value for these Buttons : [3, 4]
LOG: Button 3 have a negative remaining !
LOG: Button 4 have a negative remaining !
LOG: Decrease DONE.
LOG: the selected Button is 0, its joltages are : [3], its remaining is : 1.
LOG: after press the Button, our current joltages are : [3, 5, 4, 7].
LOG: we will decrease remaining value for these Buttons : [1, 3]
LOG: Button 1 have a negative remaining !
LOG: Button 3 have a negative remaining !
LOG: Decrease DONE.
11
=== LOG: We get into the final position in 12 press ! ===
vvvvvvvvvvvvvvv"""
