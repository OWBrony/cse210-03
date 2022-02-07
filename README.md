# cse210-03
parachute game

game director is called from the main file.
game director calls word generator class, jumper class and guesser class. initialize jumper and guesser classes on game startup. Then, while keepPlaying is True:

Jumper class holds the status of the jumper and handles the removal of parachute parts. recieves "wrong" flags and deletes part of parachute. Passes to director whether the games is over.
Word generator class takes a random word from a list of possible words and passes the word along. 
Geusser takes guessed letters from users. takes in word from word generator. passes "right" or "wrong" flag to director that then passes flag to jumper.
