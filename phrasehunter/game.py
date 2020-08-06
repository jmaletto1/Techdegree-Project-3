import random
from .phrase import Phrase


class Game:

    def __init__(self, phrases):
        # Select the phrases at random
        self.phrases = []
        for i in phrases:
            self.phrases.append(Phrase(i))
        self.phrase = random.choice(self.phrases)
        self.lives = 5

    def the_game(self):
        welcome = """\nWelcome to the Phrase Hunters Challenge. Basically hangman, but fancier.
        \nPlease make your first selection. Here is your phrase:
        """
        print(welcome)

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
                    print("\n\nWell done, you completed the game!\n")
                    continue_playing = input(
                        "Would you like to play again? y/n: ")
                    if continue_playing.lower() == 'y':
                        # Re-launch the game
                        self.phrase = random.choice(self.phrases)
                        self.lives = 5
                        print("Welcome to the game! Here is your phrase:")
                        continue
                    else:
                        print("Thanks for playing. Ciao!")

        # Game over section. Would you like to play again?
                elif self.lives <= 0:
                    print("\nGame over! The correct phrase was: \n")
                    self.phrase.reveal_phrase()
                    relaunch = input(
                        "\n\nWould you like to play again? y/n: \n\n")
                    if relaunch.lower() == 'n':
                        print("\nThanks for playing!")
                    elif relaunch.lower() == 'y':
                       # Re-launch the game
                        self.phrase = random.choice(self.phrases)
                        self.lives = 5
                        print("Welcome to the game! Here is your phrase:")
                        continue
                    else:
                        print("I'm afraid your input was invalid. Have a good day!")
            except ValueError:
                print("Noooooz that was invalid.")
