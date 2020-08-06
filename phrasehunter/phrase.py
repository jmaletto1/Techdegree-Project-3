# Create your Phrase class logic here.
from .character import Character

class Phrase:

    def __init__(self, phrase):
        self.phrase = phrase
        self.letters = []
        for i in phrase:
            self.letters.append(Character(i))

    def display_phrase(self):
        for x in self.letters:
            print(x.show_char(), end=" ")

    def filled_out(self):
        for i in self.letters:
            if i.was_guessed == False:
                return False
        return True

    def guess_check(self, guess):
        for i in self.letters:
            i.usr_guess(guess)

    def letter_check(self, guess):
        for letter in self.letters:
            if letter.char.lower() == guess.lower():
                return True
        return False

    def reveal_phrase(self):
        for x in self.letters:
            print(x.reveal_phrase(), end="")
