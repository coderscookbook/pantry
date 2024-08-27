'''
To run the test run: python -m unittest test_bracket_matcher.py
'''

import unittest
from bracket_matcher import BracketMatcher

class TestBracketMatcher(unittest.TestCase):

    def test_balanced_brackets(self):
        self.assertEqual(BracketMatcher("(a + b) * (c - d)"), 1)
        self.assertEqual(BracketMatcher("((a + b) * (c - d))"), 1)
        self.assertEqual(BracketMatcher("a + (b + c) - d"), 1)

    def test_unbalanced_brackets(self):
        self.assertEqual(BracketMatcher("(a + b))"), 0)
        self.assertEqual(BracketMatcher("((a + b)"), 0)
        self.assertEqual(BracketMatcher(")a + b("), 0)

    def test_no_brackets(self):
        self.assertEqual(BracketMatcher("abc"), 1)
        self.assertEqual(BracketMatcher(""), 1)

    def test_starts_with_closing_bracket(self):
        self.assertEqual(BracketMatcher(")a + b("), 0)

    def test_ends_with_opening_bracket(self):
        self.assertEqual(BracketMatcher("a + b("), 0)

if __name__ == "__main__":
    unittest.main()



