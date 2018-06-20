"""
Hello unit tests.
"""
import unittest
from hello import greeting


class TestHello(unittest.TestCase):
    """
    Tests for Hello.
    """

    def test_greeting(self):
        """
        Test greeting.
        """
        # Should produce something if name isn't given or is blank.
        self.assertIsNotNone(greeting())
        self.assertIsNotNone(greeting(""))

        # Greeting should contain name.
        name = "foo"
        self.assertTrue(name in greeting(name))


if __name__ == "__main__":
    unittest.main()
