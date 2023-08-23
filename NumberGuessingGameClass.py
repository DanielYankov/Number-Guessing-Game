import random

# NumberGuessingGame class realises a game where the computer
# generates random number and a player can guess it in given
# number of attempts. Player can select from 3 dificulties
# changing the number of attempts that are available

class NumberGuessingGame:

    def __init__(self):
        self.attempts = 0
        self.playerWon = False
        self.attemptsLeft = 0
        self.numberToGuess = random.randint(0, 100)

    # selecting dificulty of the game, which changes the number of available attempts
    def choose_dificulty(self, dificulty):
        self.attempts = 10 - (dificulty * 2 + 1)
        self.attemptsLeft = self.attempts
        return self.attempts

    # recieving a number as a guess and returning if the number
    # must be higher or lower then the computer generated one
    # or if the player guesses the number correctly
    def make_guess(self, number):
        result = ''
        if number > self.numberToGuess:
            result = 'lower'
            self.attemptsLeft -= 1
        elif number < self.numberToGuess:
            result = 'higher'
            self.attemptsLeft -= 1
        elif number == self.numberToGuess:
            result = 'correct'
            self.attemptsLeft -= 1
        if self.attemptsLeft == 0 and result != 'correct':
            result = ''
        return result

