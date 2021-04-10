import unittest
from big_file_handler import BigFileHandler


class Test5LinesFile(unittest.TestCase):

    def test_navigate_12_lines_file(self):
        with BigFileHandler("test_12_lines_file.txt") as bfh:
            lines_1 = bfh.get_lines()
            bfh.down()
            lines_2 = bfh.get_lines()
            bfh.page_down()
            lines_3 = bfh.get_lines()
            bfh.page_up()
            lines_4 = bfh.get_lines()
            bfh.goto(2)
            lines_5 = bfh.get_lines()
            bfh.up()
            lines_6 = bfh.get_lines()
            self.assertEqual(11, len(lines_1))
