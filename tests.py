import unittest
from maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_create_cells_2(self):
        num_cols = 9
        num_rows = 5
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(m1._cells), num_cols)
        self.assertEqual(len(m1._cells[0]), num_rows)

    def test_maze_create_cells_3(self):
        num_cols = 20
        num_rows = 15
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(m1._cells), num_cols)
        self.assertEqual(len(m1._cells[0]), num_rows)

    def test_break_entrance_exit_cells(self):
        num_cols = 9
        num_rows = 5
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m1._break_entrance_and_exit()
        entrance_cell = m1._cells[0][0]
        exit_cell = m1._cells[(num_cols - 1)][(num_rows - 1)]
        self.assertEqual(entrance_cell.has_top_wall, False)
        self.assertEqual(exit_cell.has_bottom_wall, False)

    def test_reset_visited(self):
        num_cols = 9
        num_rows = 5
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m1._reset_visted()
        for i in range(m1._num_cols):
            for j in range(m1._num_rows):
                cell = m1._cells[i][j]
                self.assertEqual(cell.visited, False)


if __name__ == "__main__":
    unittest.main()
