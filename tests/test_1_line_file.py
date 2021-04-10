import unittest
from big_file_handler import BigFileHandler


class Test1LineFile(unittest.TestCase):

    def test_navigate_1_line_file(self):
        with BigFileHandler("test_1_line_file.txt") as bfh:
            lines_1 = bfh.get_lines()
            self.assertEqual(1, len(lines_1))

            bfh.down()
            lines_2 = bfh.get_lines()
            self.assertEqual(1, len(lines_2))

            bfh.page_down()
            lines_3 = bfh.get_lines()
            self.assertEqual(1, len(lines_3))

            bfh.page_down()
            lines_4 = bfh.get_lines()
            self.assertEqual(1, len(lines_4))

            bfh.goto(2)
            lines_5 = bfh.get_lines()
            self.assertEqual(1, len(lines_5))


