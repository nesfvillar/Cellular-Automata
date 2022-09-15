import enum
import random

from cell import *
from position import *


class GridAutomata:
    def __init__(self, width, height, default_state=None):
        self.cells = [[Cell(default_state, Position(i, j)) for j in range(height)] for i in range(width)]
        self.width, self.height = width, height
        for i, row in enumerate(self.cells):
            for j, cell in enumerate(row):
                for direction in GridAutomata.Direction:
                    cell.add_neighbour(self.get_cell_at(i, j, direction))

    @staticmethod
    class Direction(enum.Enum):
        E = 0
        NE = 1
        N = 2
        NW = 3
        W = 4
        SW = 5
        S = 6
        SE = 7

    def get_cell_at(self, i, j, direction=None):
        match direction:
            case None:
                i, j = self.get_index_by_wrap(i, j)
                if i is None or j is None:
                    return
                else:
                    return self.cells[i][j]
            case self.Direction.E:
                return self.get_cell_at(i + 1, j)
            case self.Direction.NE:
                return self.get_cell_at(i + 1, j + 1)
            case self.Direction.N:
                return self.get_cell_at(i, j + 1)
            case self.Direction.NW:
                return self.get_cell_at(i - 1, j + 1)
            case self.Direction.W:
                return self.get_cell_at(i - 1, j)
            case self.Direction.SW:
                return self.get_cell_at(i - 1, j - 1)
            case self.Direction.S:
                return self.get_cell_at(i, j - 1)
            case self.Direction.SE:
                return self.get_cell_at(i + 1, j - 1)

    def get_index_by_wrap(self, i, j, wrapping=True):
        if wrapping:
            if i < 0:
                i += self.width
            elif i >= self.width:
                i -= self.width
            if j < 0:
                j += self.height
            elif j >= self.height:
                j -= self.height
            return i, j
        else:
            if i < 0 or i >= self.width or j < 0 or j >= self.height:
                return None, None
            else:
                return i, j

    def randomize_state(self, possible_states):
        for row in self.cells:
            for cell in row:
                if cell is not None:
                    cell.new_state(random.choice(possible_states))
                    cell.swap_state()

    def update(self, func):
        for row in self.cells:
            for cell in row:
                if cell is not None:
                    func(cell)
        for row in self.cells:
            for cell in row:
                if cell is not None:
                    cell.swap_state()

    def __repr__(self):
        return f"<GridAutomata: {self.cells}>"
