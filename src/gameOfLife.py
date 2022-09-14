from gridAutomata import *
import tkinter


class GameOfLife(GridAutomata):
    def __init__(self, width, height, colours={"alive": "green", "dead": "red"}, default_state="dead"):
        super().__init__(width, height, default_state)
        self.colours = colours

    def randomize_state(self):
        return super().randomize_state(tuple(self.colours.keys()))

    def update(self):
        super().update(GameOfLife.rules)

    @staticmethod
    def rules(cell):
        if cell.get_state() == "alive" and (cell.count_neighbours("alive") < 2 or cell.count_neighbours("alive") > 3):
            cell.new_state("dead")
        elif cell.get_state() == "dead" and cell.count_neighbours("alive") == 3:
            cell.new_state("alive")


def main():
    CANVAS_WIDTH, CANVAS_HEIGTH = 640, 640
    AUTOMATA_WIDTH, AUTOMATA_HEIGTH = 10, 10

    root = tkinter.Tk()
    root.title("Conway's Game of Life")

    canvas = tkinter.Canvas(root, bg="white", width=CANVAS_WIDTH, height=CANVAS_HEIGTH)
    canvas.pack()

    game_of_life = GameOfLife(AUTOMATA_WIDTH, AUTOMATA_HEIGTH)
    game_of_life.randomize_state()

    def update_canvas():
        for row in game_of_life.cells:
            for cell in row:
                x1 = cell.position.x * CANVAS_WIDTH / AUTOMATA_WIDTH
                y1 = cell.position.y * CANVAS_HEIGTH / AUTOMATA_HEIGTH
                x2 = (cell.position.x + 1) * CANVAS_WIDTH / AUTOMATA_WIDTH
                y2 = (cell.position.y + 1) * CANVAS_HEIGTH / AUTOMATA_HEIGTH
                canvas.create_rectangle(x1, y1, x2, y2, fill=game_of_life.colours[cell.get_state()])
        game_of_life.update()
        canvas.after(500, update_canvas)

    update_canvas()
    root.mainloop()


if __name__ == "__main__":
    main()
