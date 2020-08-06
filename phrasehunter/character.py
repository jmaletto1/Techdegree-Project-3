# Create your Character class logic in here.

class Character:

    def __init__(self, char):
        if char == ' ':
            self.was_guessed = True
        else:
            self.was_guessed = False
        self.char = char

    def usr_guess(self, guess):
        if guess.lower() != self.char.lower():
            return self.was_guessed
        else:
            self.was_guessed = True
        return self.was_guessed

    def show_char(self):
        if self.was_guessed:
            return self.char.lower()
        return '_'

    def reveal_phrase(self):
        return self.char
