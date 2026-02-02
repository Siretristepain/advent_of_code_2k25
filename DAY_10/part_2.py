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

    created_buttons = []

    def __init__(self, name: int, joltages: list[int], remaining: int = 99):
        self.name = name
        self.joltages = joltages
        self.remaining = remaining

        Button.created_buttons.append(self)

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
    
    @classmethod
    def get_random_button(self):
        return Button.created_buttons[random.randint(0, len(Button.created_buttons)-1)]


# =========
# Functions
# =========

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


if __name__ == '__main__':
    
    # buttons = create_buttons_for_current_line(input_buttons=[[1, 2], [3]])
    # for button in buttons:
    #     print(f"{button.name} --> {button.joltages}")

    buttons = create_buttons_for_current_line(input_buttons=[[3], [1,3], [2], [2,3], [0,2], [0,1]])
    print(buttons)
    dic = sort_buttons_by_jolt_index(joltages=[3, 5, 4, 7], buttons=buttons)
    print(dic)

    Button.set_correct_remaining_for_all_buttons(buttons_to_set=buttons, organized_buttons=dic, joltages=[3, 5, 4, 7])

    for but in buttons:
        print(f"{but} --> {but.remaining}")


