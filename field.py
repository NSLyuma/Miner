from Miner.cell import Cell
import random


class Field:

    def __init__(self,size=7):
        self.data=[[Cell() for i in range(size)] for j in range(size)]
        self.size=7

    def generate_field(self):
        # x=random.randint(0,self.size)
        mines_count = random.randint(self.size, self.size * 2)

        pairs = set()
        while len(pairs) < mines_count:
            x = random.randint(0, self.size-1)
            y = random.randint(0, self.size-1)
            pairs.add((x, y))
            # print(pairs)

        for pair in pairs:
            x=pair[0]
            y=pair[1]
            self.data[x][y].mines_count=Cell.MINE

        for i in range(self.size):
            for j in range(self.size):
                self.calculate_mines_count(i,j)

    def calculate_mines_count(self,i,j):
        current_cell = self.data[i][j]
        count = 0
        if current_cell.mines_count != Cell.MINE:
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    x = i + dx
                    y = j + dy
                    if 0 <= x < self.size and 0 <= y < self.size and self.data[x][y].mines_count == Cell.MINE:
                        count += 1

            current_cell.mines_count = count

    def get_value(self, x, y):
        pass

    def open_cell(self, x, y):
        if self.data[x][y].mines_count==Cell.MINE:
            return Cell.MINE
        self.walk(x,y)

        return 1

    def walk(self,x,y):
        if self.data[x][y].is_open:
            return
        if self.data[x][y].mines_count>0:
            return
        self.data[x][y].is_open = True

        if x-1>=0:
            self.walk(x-1,y)
            if y+1<self.size:
                self.walk(x-1,y+1)
            if y-1>=0:
                self.walk(x-1,y-1)
        if x+1<self.size:
            self.walk(x+1,y)
            if y+1<self.size:
                self.walk(x+1,y+1)
            if y-1>=0:
                self.walk(x+1,y-1)
        if y+1<self.walk(x,y+1):
            self.walk(x,y+1)
        if y-1>=0:
            self.walk(x,y-1)



field = Field()
field.generate_field()