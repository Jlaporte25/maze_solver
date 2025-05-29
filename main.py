from graphics import Window
from maze import Maze


def main():
    num_cols = 8
    num_rows = 8
    margin = 50
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    win = Window(screen_x, screen_y)

    maze = Maze(margin, margin, num_cols, num_rows, cell_size_x, cell_size_y, win, 10)
    if maze._solve():
        print("True")
    else:
        print("False")

    win.wait_for_close()


if __name__ == "__main__":
    main()
