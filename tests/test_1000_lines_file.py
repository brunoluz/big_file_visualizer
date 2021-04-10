import unittest
from big_file_handler import BigFileHandler


class Test1000LinesFile(unittest.TestCase):

    def test_init__valid_file(self):
        with BigFileHandler("test_1000_lines_file.txt") as bfh:
            self.assertEqual("test_1000_lines_file.txt", bfh.get_file())

    def test_get__next_lines(self):
        with BigFileHandler("test_1000_lines_file.txt") as bfh:
            lines = bfh.get_lines()
        for i in range(1, 11):
            self.assertEqual(f"line {i}", lines[i])

    def test_up__bof__current_line_equals_one(self):
        with BigFileHandler("test_1000_lines_file.txt") as bfh:
            self.assertEqual(1, bfh.get_current_line())
            bfh.up()
            self.assertEqual(1, bfh.get_current_line())

    def test_up__second_line__current_line_equals_one(self):
        with BigFileHandler("test_1000_lines_file.txt") as bfh:
            bfh.goto(2)
            bfh.up()
            lines = bfh.get_lines()
            self.assertEqual(1, bfh.get_current_line())
            self.assertEqual("line 3", lines[3])

    def test_goto__line_999__validate_buffer(self):
        with BigFileHandler("test_1000_lines_file.txt") as bfh:
            bfh.goto(999)
            lines = bfh.get_lines()
            self.assertEqual(1000, bfh.get_total_lines())
            self.assertEqual(1000, bfh.get_buffer_max_value())
            self.assertEqual(950, bfh.get_buffer_min_value())
            self.assertEqual("line 999", lines[999])

    def test_goto__line_100__validate_buffer(self):
        with BigFileHandler("test_1000_lines_file.txt") as bfh:
            bfh.goto(100)
            bfh.get_lines()
            self.assertIsNone(bfh.get_total_lines())
            self.assertEqual(51, bfh.get_buffer_min_value())
            self.assertEqual(150, bfh.get_buffer_max_value())

    def test_goto__negative_line(self):
        with BigFileHandler("test_1000_lines_file.txt") as bfh:
            bfh.goto(-1)
            bfh.get_lines()
            self.assertEqual(1, bfh.get_current_line())

    def test_navigate_last_lines(self):
        with BigFileHandler("test_1000_lines_file.txt") as bfh:
            bfh.goto(995)
            lines = bfh.get_lines()
            self.assertEqual("line 1000", lines[1000])
            self.assertEqual("line 990", lines[990])
            self.assertEqual(11, len(lines))

    def test_buffer_reads(self):
        with BigFileHandler("test_1000_lines_file.txt") as bfh:
            lines_1 = bfh.get_lines()
            self.assertEqual("line 1", lines_1[1])
            self.assertEqual("line 11", lines_1[11])

            bfh.page_down()  # 12 position
            bfh.page_down()  # 23 position
            bfh.page_down()  # 34 position
            bfh.page_down()  # 45 position
            bfh.page_down()  # 56 position
            bfh.page_down()  # 67 position
            lines_2 = bfh.get_lines()
            self.assertEqual("line 67", lines_2[67])
            self.assertEqual("line 77", lines_2[77])

            bfh.goto(659)
            lines_3 = bfh.get_lines()
            self.assertEqual("line 659", lines_3[659])
            self.assertEqual("line 669", lines_3[669])

            self.assertEqual(3, bfh.get_buffer_reads())
