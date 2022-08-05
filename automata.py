import random


class Cell:
    def __init__(self, state):
        self.state = state
        self.newState = None
        self.neighbours = []

    def addNeighbour(self, cell):
        self.neighbours.append(cell)

    def countNeighbours(self, state):
        i = 0
        for neighbour in self.neighbours:
            if neighbour.state == state:
                i += 1
        return i

    def swapState(self):
        if self.newState != None:
            self.state, self.newState = self.newState, None

    def updateState(self, newState):
        self.newState = newState

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

        self.cells = [
            [CellId(defaultState, (i, j)) for i in range(self.width)]
            for j in range(self.heigth)
        ]

        for i in range(self.width):
            for j in range(self.heigth):
                if i > 0:
                    if j < self.heigth - 1:
                        self.cells[i][j].addNeighbour(self.cells[i - 1][j + 1])
                    self.cells[i][j].addNeighbour(self.cells[i - 1][j])
                    if j > 0:
                        self.cells[i][j].addNeighbour(self.cells[i - 1][j - 1])
                if i < self.width - 1:
                    if j < self.heigth - 1:
                        self.cells[i][j].addNeighbour(self.cells[i + 1][j + 1])
                    self.cells[i][j].addNeighbour(self.cells[i + 1][j])
                    if j > 0:
                        self.cells[i][j].addNeighbour(self.cells[i + 1][j - 1])
                if j > 0:
                    self.cells[i][j].addNeighbour(self.cells[i][j - 1])
                if j < self.heigth - 1:
                    self.cells[i][j].addNeighbour(self.cells[i][j + 1])

    def update(self, func):
        for row in self.cells:
            for cell in row:
                func(cell)
        for row in self.cells:
            for cell in row:
                cell.swapState()

    def randomizeState(self, possibleStates):
        for row in self.cells:
            for cell in row:
                cell.state = random.choice(possibleStates)

    def __str__(self):
        gridString = ""
        for i in range(self.width):
            for j in range(self.heigth):
                if self.cells[i][j].state == "alive":
                    gridString += "A"
                elif self.cells[i][j].state == "dead":
                    gridString += "D"
            gridString += "\n"
        return gridString
