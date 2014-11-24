import unittest
import project.regular_expression.parser as parser

class TestParenParser(unittest.TestCase):
    def setUp(self):
        self.string1 = 'asdf(qwer)(jioi))'

    def testLeftOf(self):
        self.assertEqual(parser.__leftOfParen__(self.string1),('asdf', 4))

    def testMatchLeadingParen(self):
        string1 = '(()(asdf()))remainder'
        string2 = '()()()'
        self.assertEqual(parser.__matchLeadingParen__(string1), ('()(asdf())', 'remainder'))
        self.assertEqual(parser.__matchLeadingParen__(string2), ('', '()()'))

    def testParser(self):
        string1 = 'leftmost(innerLeft(middle(more middle) left middle))end'
        self.assertEqual(parser.parenthesesParser(string1), ['leftmost', ['innerLeft', ['middle', ['more middle'], ' left middle']], 'end'])