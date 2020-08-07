import random
from .phrase import Phrase


class Game:

    def __init__(self, phrases):
        self.phrases = [Phrase(i) for i in phrases]
        self.phrase = random.choice(self.phrases)
        self.lives = 5

    def relaunch(self):
        continue_playing = input("\n\nWould you like to play again? y/n: ")
        if continue_playing.lower() == 'y' and len(self.phrases) > 0:
            # Re-launch the game
            self.phrase = random.choice(self.phrases)
            self.lives = 5
            self.welcome()
        elif continue_playing.lower() != 'n':
            print(
                "\nI'm afraid that value was invalid, so we've ended your game. Have a nice day!")
        else:
            print("Thanks for playing. Ciao!")

    def remove_phrase(self):
        self.phrases.remove(self.phrase)

    def welcome(self):
        welcome = """\nWelcome to the Phrase Hunters Challenge. Basically hangman, but fancier.
        \nPlease make your first selection. Here is your phrase:
        """
        print(welcome)

    def the_game(self):
        self.welcome()

        # Run the game (in play, so with 1-5 lives)
        while self.lives > 0 and self.phrase.filled_out() == False:
            self.phrase.display_phrase()
            try:
                guess = input(
                    "\n\nEnter a Letter. You currently have {} live(s).\n".format(self.lives))
                if self.lives > 1 and (len(guess) != 1 or not guess.isalpha()):
                    self.lives -= 1
                    print("\nPlease only enter 1 letter. Due to this unncessary silliness, you now have {} lives. Sad.".format(
                        self.lives))
                    continue

                self.phrase.letter_check(guess)
                self.phrase.guess_check(guess)

                if self.phrase.letter_check(guess) == False:
                    self.lives -= 1
                    print("\nYou are down to {} lives.".format(self.lives))

    # Congratulations area if successful. Relaunch the game
                if self.lives > 0 and self.phrase.filled_out() == True:
                    self.phrase.reveal_phrase()
                    print("\n\nWell done, you completed the game!")
                    self.remove_phrase()
                    if len(self.phrases) < 1:
                        print(
                            "Oh wow, there are no more phrases! You are the hangman champion!")
                        break
                    self.relaunch()

        # Game over section. Would you like to play again?
                elif self.lives <= 0:
                    print("\nGame over! The correct phrase was: \n")
                    self.phrase.reveal_phrase()
                    self.remove_phrase()
                    if len(self.phrases) < 1:
                        print(
                            "\n\nOh wow, there are no phrases left! Thanks for playing. Have a somewhat pleasurable day.")
                        break
                    self.relaunch()
            except ValueError:
                print("Noooooz that was invalid.")
