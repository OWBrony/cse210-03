from Jumper import Jumper
from Guesser import Guesser
from Generator import Generator

class Director():

    def __init__(self):
        self.jumper = Jumper()
        self.guesser = Guesser()
        self.generator = Generator()

        self.keep_playing = True

    def start_game(self):
        '''Generates the start of the game'''
        holder = self.generator.generate_word()
        self.jumper.print_word(holder)
        print()

        '''Checks whether to continue game loop'''
        while self.keep_playing == True:
            '''Call functions required for game mechanics'''
            self.jumper.generate_grid(holder)
            print()
            self.jumper.check_letters(holder,self.guesser.player_input())
            print()
            self.jumper.print_word(holder)
            print()
            self.keep_playing = self.jumper.check_active(holder)
        self.jumper.generate_grid(holder)
        if self.jumper.check_alive():
            self.end_game_good()
        else:
            self.end_game_bad(holder)

    def get_inputs(self):
        letter =  self.Jumper.player_input()
        return letter

    def end_game_bad(self,word):
        print(f"\nYour jumper's parachute failed! The word was {word}.")
        print("Thanks for playing!")

    def end_game_good(self):
        print("\nYou have guessed the word and saved your jumper!")
        print("Thanks for playing!")
