



'''Jumper class holds the status of the jumper and handles the removal of parachute parts. recieves "wrong" flags and deletes part of parachute. Passes to director whether the games is over.'''

class Jumper():
    def __init__(self):
        self.health = 10
        self.word = str

    def generate_grid(self):
        pass

    

    def check_letter(self, letter):
        pass

    



    def check_health(self):


        if self.health == 0:
            print(f"\nYou have ran out of lives the word was {self.word}")
            print("Thanks for playing")
            return self.keep_Playing == False
        pass