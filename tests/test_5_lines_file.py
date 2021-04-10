import unittest
from big_file_handler import BigFileHandler


class Test5LinesFile(unittest.TestCase):

    def test_navigate_5_lines_file(self):
        with BigFileHandler("test_5_lines_file.txt") as bfh:
            lines_1 = bfh.get_lines()
            self.assertEqual("line 1", lines_1[1])
            self.assertEqual("line 5", lines_1[5])
            self.assertEqual(5, len(lines_1))

            bfh.down()
            lines_2 = bfh.get_lines()
            self.assertEqual("line 1", lines_2[1])
            self.assertEqual("line 5", lines_2[5])
            self.assertEqual(5, len(lines_2))

            bfh.page_down()
            lines_3 = bfh.get_lines()
            self.assertEqual("line 1", lines_3[1])
            self.assertEqual("line 5", lines_3[5])
            self.assertEqual(5, len(lines_3))

            bfh.page_up()
            lines_4 = bfh.get_lines()
            self.assertEqual("line 1", lines_4[1])
            self.assertEqual("line 5", lines_4[5])
            self.assertEqual(5, len(lines_4))

            bfh.goto(2)
            lines_5 = bfh.get_lines()
            self.assertEqual("line 1", lines_5[1])
            self.assertEqual("line 5", lines_5[5])
            self.assertEqual(5, len(lines_5))

            bfh.up()
            lines_6 = bfh.get_lines()
            self.assertEqual("line 1", lines_6[1])
            self.assertEqual("line 5", lines_6[5])
            self.assertEqual(5, len(lines_6))
