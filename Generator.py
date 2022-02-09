import random


'''Word generator class takes a random word from a list of possible words and passes the word along. '''



class Generator():
    def __init__(self):
        self.word = str


    def generate_word(self):
        """
        This will go into a words.txt and gather 1 random word from the list and 
        create a set a dashes into the hidden word list to represent missing letters
        for the player.

        Could be replaced by a list of words contained in-code. 
        """
        words = ["apple","blueberry","banana","cheese","sugar","pie"]

        self.word = words[random.randint(0,len(words) - 1)]
        return self.word