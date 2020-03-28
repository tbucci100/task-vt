import unittest
from .data_utils import *


class TestLoadCord(unittest.TestCase):

	def test_load_preprocessed_cord_from_dir(self):
		cord_dir = "../data"
		out = load_preprocessed_cord_from_dir(cord_dir)
		self.assertEqual(out, True)


if __name__ == '__main__':
	unittest.main()
