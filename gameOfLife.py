from automata import *
import tkinter


class GameOfLife(GridAutomata):
    def __init__(self, width, heigth, colours={"alive": "green", "dead": "red"}, defaultState="dead"):
        super().__init__(width, heigth, defaultState)
        self.colours = colours

    def randomizeState(self):
        return super().randomizeState(("alive", "dead"))

    def update(self):
        super().update(self.rules)

    @staticmethod
    def rules(cell):
        if cell.state == "alive" and (
            cell.countNeighbours("alive") < 2 or
            cell.countNeighbours("alive") > 3
        ):
            cell.newState = "dead"
        elif cell.state == "dead" and cell.countNeighbours("alive") == 3:
            cell.newState = "alive"


def main():
    CANVAS_WIDTH, CANVAS_HEIGTH = 640, 640
    AUTOMATA_WIDTH, AUTOMATA_HEIGTH = 10, 10

    root = tkinter.Tk()
    root.title("Conway's Game of Life")

    canvas = tkinter.Canvas(
        root, bg="white", width=CANVAS_WIDTH, height=CANVAS_HEIGTH)
    canvas.pack()

    gameOfLife = GameOfLife(AUTOMATA_WIDTH, AUTOMATA_HEIGTH)
    gameOfLife.randomizeState()

    def updateCanvas():
        for cell in gameOfLife.cells:
            x1 = cell.id[0] * CANVAS_WIDTH / AUTOMATA_WIDTH
            y1 = cell.id[1] * CANVAS_HEIGTH / AUTOMATA_HEIGTH
            x2 = (cell.id[0] + 1) * CANVAS_WIDTH / AUTOMATA_WIDTH
            y2 = (cell.id[1] + 1) * CANVAS_HEIGTH / AUTOMATA_HEIGTH
            canvas.create_rectangle(
                x1, y1, x2, y2, fill=gameOfLife.colours[cell.state])
        gameOfLife.update()
        canvas.after(500, updateCanvas)

    updateCanvas()
    root.mainloop()


if __name__ == "__main__":
    main()
