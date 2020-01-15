from Miner.cell import Cell
from Miner.field import Field


class View:

    def __init__(self,field:Field):
        self.field=field # type: Miner.field.Field

    def display_field(self):
        for row in self.field.data:
            for cell in row:
                if cell.is_open:
                    if cell.mines_count==Cell.MINE:
                        print('* ',end='')
                    else:
                        print(str(cell.mines_count),end=' ')
                else:
                    print('_ ',end='')
            print()

    def get_user_turn(self):
        try:
            x=int(input('x: '))
            y=int(input('y: '))
            if x<0 or x>=self.field.size:
                return None
            if y<0 or y>=self.field.size:
                return None
        except:
            return None

        return x,y
