import unittest

from size import *


class SizeTest(unittest.TestCase):
    def test_size_mebibytes(self):
        size = Size('10 MiB')
        print(size.mebibytes)

        size = Size('123123121')
        print(round(size.mebibytes))
