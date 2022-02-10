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
        self.jumper.generate_grid(holder)

        #self.jumper.health = 10





        '''Checks whether to continue game loop'''

        while self.keep_playing == True:
            '''call functions required for game mechanics'''


    def get_inputs(self):
        letter =  self.Jumper.player_input()


    def do_updates():
        pass
