import unittest

from bfv_error import BigFileVisualizerFatalError
from big_file_handler import BigFileHandler


class TestBigFileHandler(unittest.TestCase):

    def test_init__invalid_file(self):
        with self.assertRaises(BigFileVisualizerFatalError):
            BigFileHandler("non_existent_file.txt")

    def test_init__empty_file(self):
        with self.assertRaises(BigFileVisualizerFatalError):
            BigFileHandler("empty_file.txt")
