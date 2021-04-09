import unittest

from bfv_error import BigFileVisualizerFatalError
from big_file_handler import BigFileHandler


class TestStringMethods(unittest.TestCase):

    def test_init_invalid_file(self):
        with self.assertRaises(BigFileVisualizerFatalError):
            BigFileHandler("non_existent_file.txt")

    def test_init_valid_file(self):
        with BigFileHandler("1000_lines_file.txt") as item:
            self.assertEqual("1000_lines_file.txt", item.get_file())

    def test_get_next_lines(self):
        with BigFileHandler("1000_lines_file.txt") as item:
            lines = item.get_lines()

        for i in range(1, 11):
            self.assertEqual(f"line {i}", lines[i])


if __name__ == '__main__':
    unittest.main()
