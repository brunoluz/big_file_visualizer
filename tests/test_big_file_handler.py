import unittest

from bfv_error import BigFileVisualizerFatalError
from big_file_handler import BigFileHandler


class TestStringMethods(unittest.TestCase):

    def test_init_invalid_file(self):
        with self.assertRaises(BigFileVisualizerFatalError):
            BigFileHandler("non_existent_file.txt")

    def test_init_valid_file(self):
        with BigFileHandler("1000_lines_file.txt") as bfh:
            self.assertEqual("1000_lines_file.txt", bfh.get_file())

    def test_get_next_lines(self):
        with BigFileHandler("1000_lines_file.txt") as bfh:
            lines = bfh.get_lines()

        for i in range(1, 11):
            self.assertEqual(f"line {i}", lines[i])

    def test_up_current_line_equals_one(self):
        with BigFileHandler("1000_lines_file.txt") as bfh:
            self.assertEqual(1, bfh.get_current_line())
            bfh.up()
            self.assertEqual(1, bfh.get_current_line())

    def test_up_current_line_equals_one(self):
        with BigFileHandler("1000_lines_file.txt") as bfh:
            self.assertEqual(1, bfh.get_current_line())
            bfh.down()
            self.assertEqual(2, bfh.get_current_line())
            bfh.up()
            self.assertEqual(1, bfh.get_current_line())




if __name__ == '__main__':
    unittest.main()
