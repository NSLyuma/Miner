class Cell:
    MINE = -1

    def __init__(self):
        self.is_open=False
        self.mines_count=0

print(Cell.MINE)