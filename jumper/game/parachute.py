class Parachute():
    """A code template for a the parachute which indicates how many guesses are left. 
    This classes responsibility is to keep track of how many strings are left
    before the guesser plumits to the ground. 

    Stereotype:
        Information Holder

    Attributes:
        parachute (list): a list of the parachutes strings.
    """

    def __init__(self):
        """Class constructor. Declares and initializes instance attributes.

        Args:
            self (Parachute): An instance of Parachute.
        """

        self.parachute = [" / \\"," /|\\","  o", " \ /","\\   /","/___\\"," ___"]

    def get_parachute(self):
        """Creates a string of the parachute for display.

        Args:
            self (Parachute): An instance of Parachute.
        """
        current_parachute = ''
        for item in range(len(self.parachute) -1, -1, -1):
            current_parachute += "\n" + self.parachute[item]
        return current_parachute


    def cut_line(self):
        """Cutes a line in the parachute using the pop method. 
        Checks to see if the player has hit the ground.

        Args:
            self (Parachute): An instance of Parachute.
        """

        if self.parachute[-1].strip() != 'o':
            self.parachute.pop()
        else:
            self.parachute[-1] = self.parachute[-1].replace('o', 'x')
