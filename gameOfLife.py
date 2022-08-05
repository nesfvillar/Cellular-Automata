from automata import *
import tkinter


def gameOfLife(cell):
    if cell.state == "alive" and (
        cell.countNeighbours("alive") < 2 or cell.countNeighbours("alive") > 3
    ):
        cell.updateState("dead")
    if cell.state == "dead" and cell.countNeighbours("alive") == 3:
        cell.updateState("alive")


def main():
    CANVAS_WIDTH, CANVAS_HEIGTH = 640, 640
    AUTOMATA_WIDTH, AUTOMATA_HEIGTH = 10, 10

    root = tkinter.Tk()
    canvas = tkinter.Canvas(root, bg="white", width=CANVAS_WIDTH, height=CANVAS_HEIGTH)

    automata = GridAutomata(AUTOMATA_WIDTH, AUTOMATA_HEIGTH)
    automata.randomizeState(("alive", "dead"))
    colors = {"alive": "green", "dead": "red"}

    def updateCanvas():
        automata.update(gameOfLife)

        for row in automata.cells:
            for cell in row:
                x1 = cell.id[0] * CANVAS_WIDTH / AUTOMATA_WIDTH
                y1 = cell.id[1] * CANVAS_HEIGTH / AUTOMATA_HEIGTH
                x2 = (cell.id[0] + 1) * CANVAS_WIDTH / AUTOMATA_WIDTH
                y2 = (cell.id[1] + 1) * CANVAS_HEIGTH / AUTOMATA_HEIGTH
                canvas.create_rectangle(x1, y1, x2, y2, fill=colors[cell.state])
        canvas.pack()
        canvas.after(1000, updateCanvas)

    updateCanvas()
    root.mainloop()


if __name__ == "__main__":
    main()
