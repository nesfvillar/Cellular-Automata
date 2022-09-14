class Cell:
    def __init__(self, state, position):
        self.state = [state, None]
        self.position = position
        self.neighbours = []

    def add_neighbour(self, cell):
        if cell is not None:
            self.neighbours.append(cell)

    def count_neighbours(self, state):
        i = 0
        for neighbour in self.neighbours:
            if neighbour.get_state() == state:
                i += 1
        return i

    def get_state(self):
        return self.state[0]

    def new_state(self, new_state):
        self.state[1] = new_state

    def swap_state(self):
        if self.state[1] is not None:
            self.state[0] = self.state[1]

    def __repr__(self):
        return f"<Cell: State = {self.state}>"
