import unittest
from big_file_handler import BigFileHandler


class Test1000LinesFile(unittest.TestCase):

    def test_init__valid_file(self):
        with BigFileHandler("1000_lines_file.txt") as bfh:
            self.assertEqual("1000_lines_file.txt", bfh.get_file())

    def test_get__next_lines(self):
        with BigFileHandler("1000_lines_file.txt") as bfh:
            lines = bfh.get_lines()
        for i in range(1, 11):
            self.assertEqual(f"line {i}", lines[i])

    def test_up__bof__current_line_equals_one(self):
        with BigFileHandler("1000_lines_file.txt") as bfh:
            self.assertEqual(1, bfh.get_current_line())
            bfh.up()
            self.assertEqual(1, bfh.get_current_line())

    def test_up__second_line__current_line_equals_one(self):
        with BigFileHandler("1000_lines_file.txt") as bfh:
            bfh.goto(2)
            bfh.up()
            self.assertEqual(1, bfh.get_current_line())

    def test_goto__line_999__validate_buffer(self):
        with BigFileHandler("1000_lines_file.txt") as bfh:
            bfh.goto(999)
            bfh.get_lines()
            self.assertEqual(1000, bfh.get_total_lines())
            self.assertEqual(1000, bfh.get_buffer_max_value())
            self.assertEqual(950, bfh.get_buffer_min_value())

    def test_goto__line_100__validate_buffer(self):
        with BigFileHandler("1000_lines_file.txt") as bfh:
            bfh.goto(100)
            bfh.get_lines()
            self.assertIsNone(bfh.get_total_lines())
            self.assertEqual(51, bfh.get_buffer_min_value())
            self.assertEqual(150, bfh.get_buffer_max_value())

    def test_goto__negative_line(self):
        with BigFileHandler("1000_lines_file.txt") as bfh:
            bfh.goto(-1)
            self.assertEqual(1, bfh.get_current_line())


if __name__ == '__main__':
    unittest.main()
