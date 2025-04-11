from graphics import Window, Cell


def main():
    win = Window(800, 600)
    cell = Cell(200, 250, 400, 300, win)
    cell2 = Cell(500, 300, 600, 400, win)
    cell.draw()
    cell2.draw()
    cell.draw_move(cell2)
    win.wait_for_close()


if __name__ == "__main__":
    main()
