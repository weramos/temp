"""
Unit tests.
"""
import unittest
from tests import MODULES


class Test(unittest.TestCase):
    """
    Run all tests.
    """
    for module in MODULES:
        suite = unittest.TestLoader().loadTestsFromTestCase(module)
        unittest.TextTestRunner(verbosity=2).run(suite)
