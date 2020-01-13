from Miner.controller import Controller


class Game:

    def __init__(self):
        self.controller = Controller()

    def start(self):
        self.controller.start_game()


game=Game()
game.start()
