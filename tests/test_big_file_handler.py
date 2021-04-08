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
            lines = item.get_next_lines(3)

        # self.assertEqual("line 1", lines[0])
        # self.assertEqual("line 2", lines[1])
        # self.assertEqual("line 3", lines[2])


if __name__ == '__main__':
    unittest.main()
