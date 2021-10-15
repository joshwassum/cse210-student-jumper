import random

# Opens and reads data from text file
with open('jumper/game/words.txt', "r") as file:
    data_text = file.readlines()
    file.close()

class Guesser():
    """A code template for a the guesser which indicates what the state of the hidden word is. 
    This classes responsibility is to keep track of how user guesses and reveal the appropriate leters.

    Stereotype:
        Information Holder

    Attributes:
        word_list (list): a list of words used to generate the secret word.
        secret_word (str): the randomly selected word to be used in the guessing game.
        guessed_word (list): a list that shows what letters have been guessed.
    """

    def __init__(self):
        """Class constructor. Declares and initializes instance attributes.

        Args:
            self (Guesser): An instance of Guesser.
        """

        self. word_list = []
        for i in data_text:
            self.word_list.append(i.replace('\n', ''))

        self.secret_word = self.word_list[random.randint(0, len(self.word_list) -1)]

        self.guessed_word = []
        for str in self.secret_word:
            self.guessed_word.append('_ ')

        print(self.secret_word)

    def get_secret_word(self):
        """Creates a string of the hidden word for display.

        Args:
            self (Guesser): An instance of Guesser.
        """
        hint =''
        for i in self.guessed_word:
            hint += i

        return hint


    def user_guess(self):
        '''Ask the user to guess a letter that the director will send to the console to print.
        
        Returns text to prompt user to guess a letter.
        '''
        guess = "Guess a letter: "
        return guess

    def letter_check(self, letter):
        '''Checks the users letter guess a letter with a true or false then return
        
        Returns text to prompt user to guess a letter.
        Args:
            self (Guesser): An instance of Guesser.
            letter: The letter the Guesser guesses.
        '''
        if letter in self.secret_word:
            return True
        else:
            return False
        

    def reveal_letter(self, letter):
        
        word = list(self.secret_word)
        count = 0

        for i in range(len(word)):
            if word[i] == letter:
                self.guessed_word[i] = letter + " "
                count += 1
            
        message = (f"There are {count} {letter}'s")

        return message
        
         
