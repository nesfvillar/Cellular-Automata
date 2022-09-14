import random
from cell import *
from position import *


class GridAutomata:
    def __init__(self, width, height, default_state=None):
        self.cells = [[Cell(default_state, Position(i, j)) for j in range(height)] for i in range(width)]

        # def get_cell_at(i, j):
        #     if i < 0 or j < 0 or i >= width or j >= height:
        #         return
        #     else:
        #         return self.cells[i][j]

        def get_cell_at(i, j):
            if i < 0:
                i += width
            if i >= width:
                i -= width
            if j < 0:
                j += height
            if j >= height:
                j -= height
            return self.cells[i][j]

        for i in range(width):
            for j in range(height):
                self.cells[i][j].add_neighbour(get_cell_at(i - 1, j + 1))
                self.cells[i][j].add_neighbour(get_cell_at(i - 1, j))
                self.cells[i][j].add_neighbour(get_cell_at(i - 1, j - 1))
                self.cells[i][j].add_neighbour(get_cell_at(i, j + 1))
                self.cells[i][j].add_neighbour(get_cell_at(i, j - 1))
                self.cells[i][j].add_neighbour(get_cell_at(i + 1, j + 1))
                self.cells[i][j].add_neighbour(get_cell_at(i + 1, j))
                self.cells[i][j].add_neighbour(get_cell_at(i + 1, j - 1))

    def randomize_state(self, possible_states):
        for row in self.cells:
            for cell in row:
                cell.state[0] = random.choice(possible_states)

    def update(self, func):
        for row in self.cells:
            for cell in row:
                func(cell)
        for row in self.cells:
            for cell in row:
                cell.swap_state()

    def __repr__(self):
        return f"<GridAutomata: {self.cells}>"
