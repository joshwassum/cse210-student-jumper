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

        self.guesser (Guesser()): An instance of the class of objects known as Guesser
    '''
    def __init__(self):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self.console = Console()
        self.parachute = Parachute()
        self.keep_playing = True
        self.guesser = Guesser()
        self.letter = ""

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


        self.guesser.get_secret_word()
        
        if self.letter not in self.guesser.secret_word:
            self.parachute.cut_line()
        else:
            self.guesser.reveal_letter(self.letter)
        
        


    def do_outputs(self):
        '''Outputs the important game information for each round of play.
        '''
        
        #self.console.write(self.parachute.get_parachute()) 

        #self.console.write(self.guesser.get_secret_word())
        if self.parachute.parachute[-1].strip() == "x":
            self.keep_playing = False
            self.console.write(self.parachute.get_parachute())
           

    def get_inputs(self):
        """Gets the inputs at the beginning of each round of play. 

        Args:
            self (Director): An instance of Director.
        """
        
        self.console.write(self.parachute.get_parachute()) 

        self.console.write(self.guesser.get_secret_word())
        self.letter = self.console.read(self.guesser.user_guess())
        
