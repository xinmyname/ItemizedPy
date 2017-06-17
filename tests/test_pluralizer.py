"""Test pluralizer"""

import unittest
from src import pluralizer

class PluralizerTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_basic_pluralizing(self):
        """test basic pluralizing"""
        self.assertEqual(pluralizer.plural_of("cat"), "cats")

if __name__ == '__main__':
    unittest.main()
