
'''Jumper class holds the status of the jumper and handles the removal of parachute parts. recieves "wrong" flags and deletes part of parachute. Passes to director whether the games is over.'''

class Jumper():
    def __init__(self):
        self.health = 4
        self.word = str
        self.parachute = [" ___ ", "/   \ " , " --- " ," \ / "]
        self.jumper = ["  O  "," /|\ "," / \ "]
        self.correct_guesses = []
        self.wrong_guesses = []

    def _make_parachute(self):
        if self.parachute == None:
            print()
        elif self.health == 4:
            for item in self.parachute:
                print(item)
        elif self.health == 3 and len(self.parachute) == 3:
            for item in self.parachute:
                print(item)
        elif self.health == 3:
            self.parachute.pop(0)
            for item in self.parachute:
                print(item)
        elif self.health == 2 and len(self.parachute) == 2:
            for item in self.parachute:
                print(item)
        elif self.health == 2:
            self.parachute.pop(0)
            for item in self.parachute:
                print(item)
        elif self.health == 1 and len(self.parachute) == 1:
            for item in self.parachute:
                print(item)
        elif self.health == 1:
            self.parachute.pop(0)
            for item in self.parachute:
                print(item)

    def _make_jumper(self):
        if self.health == 0:
            self.jumper[0] = "  X  "
            for item in self.jumper:
                print(item)
        else:
            for item in self.jumper:
                print(item)

    def generate_grid(self,word):
        self._make_parachute()
        self._make_jumper()
        print()
        print("^^^^^^^^^^")
        print()

    def check_letters(self, word, letter = None):
        if letter == None:
            pass
        else:
            if letter.lower() in word:
                self.correct_guesses.append(letter.lower())
            else:
                self.wrong_guesses.append(letter.lower())
                self.health -= 1

    def print_word(self, word):
        for letter in word:
            if letter in self.correct_guesses:
                print(f" {letter}", end = " ")
            else:
                print("_", end = " ")
        print()

    def check_health(self):
        if self.health == 0:
            return False
        else:
            return True
        # elif self.correct_guesses in word:
        #     print("You Won!")
        #     return self.keep_Playing == False
