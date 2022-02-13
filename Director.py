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
        print(holder)

        '''Checks whether to continue game loop'''
        while self.keep_playing == True:
            '''call functions required for game mechanics'''
            self.jumper.generate_grid(holder)
            print()
            self.jumper.check_letters(holder,self.guesser.player_input())
            self.jumper.print_word(holder)
            self.keep_playing = self.jumper.check_health()
        self.jumper.generate_grid(holder)
        self.end_game_bad(holder)

    def get_inputs(self):
        letter =  self.Jumper.player_input()
        return letter


    def end_game_bad(self,word):
        print(f"\nYou have ran out of lives the word was {word}")
        print("Thanks for playing!")
