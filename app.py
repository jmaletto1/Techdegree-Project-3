from phrasehunter.game import Game

phrases = [
    "One more mile",
    "Top of the morning",
    "Breakfast in bed",
    "Dare to dream",
    "Quitters gonna quit",
    "Live Laugh Vomit"
]


def start():
    game = Game(phrases)
    game.the_game()


if __name__ == "__main__":
    start()
