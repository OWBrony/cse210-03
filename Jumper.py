
'''Jumper class holds the status of the jumper and handles the removal of parachute parts. 
Contains code for checking guessed letters and stores the word. Passes to director whether the games is over.'''

class Jumper():
    def __init__(self, word):
        self.word = word
        self.health = 4
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

    def generate_grid(self):
        self._make_parachute()
        self._make_jumper()
        print()
        print("^^^^^^^^^^")
        print()

    def check_letters(self, letter = None):
        if len(letter) == 0:
            pass
        else:
            letter = letter[0].lower()
            if letter in self.word:
                self.correct_guesses.append(letter)
            else:
                self.wrong_guesses.append(letter)
                self.health -= 1

    def print_word(self):
        for letter in self.word:
            if letter in self.correct_guesses:
                print(f" {letter}", end = " ")
            else:
                print("_", end = " ")
        print()

    def check_word_guessed(self):
        for char in self.word:
            if char.lower() not in self.correct_guesses:
                return False
        return True

    def check_alive(self):
        return self.health > 0

    def check_active(self):
        if self.check_word_guessed():
            return False
        else:
            return self.check_alive()
