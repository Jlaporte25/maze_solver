from graphics import Window, Cell


def main():
    win = Window(800, 600)
    cell = Cell(200, 250, 400, 300, win)
    cell.draw()
    win.wait_for_close()


if __name__ == "__main__":
    main()
