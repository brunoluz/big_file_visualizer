import unittest

from bfv_error import BigFileVisualizerFatalError
from big_file_handler import BigFileHandler


class TestStringMethods(unittest.TestCase):

    def test_init__invalid_file(self):
        with self.assertRaises(BigFileVisualizerFatalError):
            BigFileHandler("non_existent_file.txt")

    def test_init__valid_file(self):
        with BigFileHandler("1000_lines_file.txt") as bfh:
            self.assertEqual("1000_lines_file.txt", bfh.get_file())

    def test_get__next_lines(self):
        with BigFileHandler("1000_lines_file.txt") as bfh:
            lines = bfh.get_lines()

        for i in range(1, 11):
            self.assertEqual(f"line {i}", lines[i])

    def test_up__current_line_equals_one(self):
        with BigFileHandler("1000_lines_file.txt") as bfh:
            self.assertEqual(1, bfh.get_current_line())
            bfh.up()
            self.assertEqual(1, bfh.get_current_line())

    def test_down__current_line_equals_one(self):
        with BigFileHandler("1000_lines_file.txt") as bfh:
            bfh.goto(2)
            bfh.up()
            self.assertEqual(1, bfh.get_current_line())
    
    def test_goto__line_999__validate_buffer(self):
        with BigFileHandler("1000_lines_file.txt") as bfh:
            bfh.goto(999)
            self.assertEqual(900, bfh.get_buffer_min_value())
            self.assertEqual(1000, bfh.get_buffer_max_value())


if __name__ == '__main__':
    unittest.main()
