import random


class Cell:
    def __init__(self, state):
        self.state = state
        self.newState = None
        self.neighbours = []

    def addNeighbour(self, cell):
        if cell != None:
            self.neighbours.append(cell)

    def countNeighbours(self, state):
        i = 0
        for neighbour in self.neighbours:
            if neighbour.state == state:
                i += 1
        return i

    def swapState(self):
        if self.newState != None:
            self.state = self.newState

    def __repr__(self):
        return f"<Cell: State = {self.state}>"


class CellId(Cell):
    def __init__(self, state, id):
        super().__init__(state)
        self.id = id

    def __repr__(self):
        return f"<CellId: Id = {self.id}, State = {self.state}>"


class Automata:
    def __init__(self, cells):
        self.cells = cells

    def update(self, func):
        for cell in self.cells:
            func(cell)
        for cell in self.cells:
            cell.swapState()

    def randomizeState(self, possibleStates):
        for cell in self.cells:
            cell.state = random.choice(possibleStates)

    def __repr__(self):
        return f"<Automata: {self.cells}>"


class GridAutomata(Automata):
    def __init__(self, width, heigth, defaultState=None):
        self.width = width
        self.heigth = heigth

        cells = {}
        for i in range(self.width):
            for j in range(self.heigth):
                cells[(i, j)] = CellId(defaultState, (i, j))

        for i in range(self.width):
            for j in range(self.heigth):
                cells[(i, j)].addNeighbour(cells.get((i - 1, j + 1)))
                cells[(i, j)].addNeighbour(cells.get((i - 1, j)))
                cells[(i, j)].addNeighbour(cells.get((i - 1, j - 1)))
                cells[(i, j)].addNeighbour(cells.get((i, j + 1)))
                cells[(i, j)].addNeighbour(cells.get((i, j - 1)))
                cells[(i, j)].addNeighbour(cells.get((i + 1, j + 1)))
                cells[(i, j)].addNeighbour(cells.get((i + 1, j)))
                cells[(i, j)].addNeighbour(cells.get((i + 1, j - 1)))

        super().__init__(list(cells.values()))
