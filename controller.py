from Miner.cell import Cell
from Miner.field import Field
from Miner.view import View


class Controller:

    def __init__(self):
        self.field=Field()
        self.field.generate_field()
        self.view=View(self.field)

    def start_game(self):
        while True:
            self.view.display_field()
            coords=self.view.get_user_turn()
            if coords is None:
                print('Wrong input. Retry')
                continue
            open_result=self.field.open_cell(coords[0],coords[1])
            if open_result==Cell.MINE:
                print('GAME OVER')
                self.field.open_field()
                self.view.display_field()
                break
            else:
                if self.field.is_only_mines_left():
                    print('YOU WIN!')
                    self.field.open_field()
                    self.view.display_field()
                    break
