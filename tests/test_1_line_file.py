import unittest
from big_file_handler import BigFileHandler


class Test1LineFile(unittest.TestCase):
    with BigFileHandler("1_line_file.txt") as bfh:
        bfh.get_lines()
        bfh.down()
        bfh.get_lines()