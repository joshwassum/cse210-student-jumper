from game.guesser import Guesser
from game.parachute import Parachute
from game.console import Console

class Director():

    '''A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.

    Stereotype:
        Controller

    Attributes:
        self.console (Console()): An instance of the class of objects known as Console.

        self.parachute (Parachute()): An instance of the class of objects known as Parachute

        self.keep_playing (boolean): Checks to see if the game continues

        self.guesser (Guesser()): An instance of the class of objects known as Seeker
    '''

    def start_game(self):
        """Starts the game loop to control the sequence of play.

        Args:
            self (Director): an instance of Director.
        """

        while self.keep_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def do_updates(self):
        """gets the updates for the game.

        Args:
            self (Director): an instance of Director.
        """

        self.get_inputs()
        self.do_outputs()
        

    def do_outputs(self):
        '''Outputs the important game information for each round of play.
        '''
        reveal = self.guesser.reveal_letter(self.get_inputs)
        self.console.write(reveal)
        if self.parachute.parachute[-1] == "x":
            self.keep_playing = False   
