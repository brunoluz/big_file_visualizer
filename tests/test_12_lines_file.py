import unittest
from big_file_handler import BigFileHandler


class Test5LinesFile(unittest.TestCase):

    def test_navigate_12_lines_file(self):
        with BigFileHandler("test_12_lines_file.txt") as bfh:
            lines_1 = bfh.get_lines()
            self.assertEqual("line 1", lines_1[1])
            self.assertEqual("line 11", lines_1[11])

            bfh.down()
            lines_2 = bfh.get_lines()
            self.assertEqual("line 2", lines_2[2])
            self.assertEqual("line 12", lines_2[12])

            bfh.page_down()
            lines_3 = bfh.get_lines()
            self.assertEqual("line 2", lines_3[2])
            self.assertEqual("line 12", lines_3[12])

            bfh.page_up()
            lines_4 = bfh.get_lines()
            self.assertEqual("line 1", lines_4[1])
            self.assertEqual("line 11", lines_4[11])

            bfh.goto(2)
            lines_5 = bfh.get_lines()
            self.assertEqual("line 2", lines_5[2])
            self.assertEqual("line 12", lines_5[12])

            bfh.up()
            lines_6 = bfh.get_lines()
            self.assertEqual("line 1", lines_6[1])
            self.assertEqual("line 11", lines_6[11])

