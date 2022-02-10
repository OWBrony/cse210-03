



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
        if self.health == 4:
            for i in self.parachute:
                print(f"{self.parachute[i]}")
        elif self.health == 3 and len(self.parachute) == 3:
            for i in self.parachute:
                print(f"{self.parachute[i]}")
        elif self.health == 3:
            self.parachute.pop(0)
            for i in self.parachute:
                print(f"{self.parachute[i]}")
        elif self.health == 2 and len(self.parachute) == 2:
            for i in self.parachute:
                print(f"{self.parachute[i]}")
        elif self.health == 2:
            self.parachute.pop(0)
            for i in self.parachute:
                print(f"{self.parachute[i]}")
        elif self.health == 1 and len(self.parachute) == 1:
            for i in self.parachute:
                print(f"{self.parachute[i]}")
        elif self.health == 1:
            self.parachute.pop(0)
            for i in self.parachute:
                print(f"{self.parachute[i]}")
        else:
            None

    def _make_jumper(self):
        if self.health == 0:
            self.jumper[0] = "  X  "
            for i in self.jumper:
                print(self.jumper[i])
        else:
            for i in self.jumper:
                print(self.jumper[i])

    def showWord(self,word,letter):
        check_letters(word, letter)

    def generate_grid(self,word):
        _make_parachute()
        _make_jumper()
        print("^^^^^^^^^^")

    def _check_letters(self, word, letter = None):
        if letter == None:
            pass
        else:
            if letter in word:
                self.correct_guesses.append(letter)
            else:
                self.wrong_guesses.append(letter)

    def check_health(self):
        if self.health == 0:
            print(f"\nYou have ran out of lives the word was {self.word}")
            print("Thanks for playing")
            return self.keep_Playing == False