import unittest
from app.database import get_random_quote

class TestQuotes(unittest.TestCase):
    def test_get_random_quote(self):
        quote = get_random_quote()
        self.assertIsInstance(quote, str)
        self.assertGreater(len(quote), 0)

if __name__ == '__main__':
    unittest.main()
