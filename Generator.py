import random

'''Word generator class takes a random word from a list of possible words and passes the word along. '''

class Generator():
    def __init__(self):
        self.word = str


    def generate_word(self):
        """
        Generates 1 random word from an internal list and 
        creates a set a dashes into the hidden word list to 
        represent missing letters for the player.
        """
        words = ["apple","blueberry","banana","cheese","sugar","pie","dough","batter","chocolate","cookies","cake"]

        self.word = words[random.randint(0,len(words) - 1)]
        return self.word

    def random_letter(self, word):
        return word[random.randint(0,len(word) - 1)]
