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

    def testParser1(self):
        string1 = 'leftmost(innerLeft(middle(more middle) left middle))end'
        self.assertEqual(parser.parenthesesParser(string1), ['leftmost', ['innerLeft', ['middle', ['more middle'], ' left middle']], 'end'])
    def testParser2(self):
        self.assertEqual(parser.parenthesesParser('a((b)(c))'), ['a',[['b'],['c']]])
    def testParser3(self):
        self.assertEqual(parser.parenthesesParser('(c)'), ['c'])

    def testBindUnaryString(self):
        self.assertEqual(parser.bindUnaryInString('abc*abc+ab?'), ['ab',parser.UnaryOperation('c', '*'), 'ab',parser.UnaryOperation('c','+'), 'a', parser.UnaryOperation('b', '?')])

    def testMergeStrings(self):
        self.assertEqual(parser.mergeStrings(['a','b','c', 5, 'a', ['a','b'], 'x','y']), ['abc', 5, 'a', ['a', 'b'], 'xy'])

    def testParenParseThenBind(self):
        parenParsed = parser.parenthesesParser("ab|aab|(a | b(a | b)*)?")
        self.assertEqual(parser.bindUnaryOperators(parenParsed), ['ab|aab|', parser.UnaryOperation(['a | b', parser.UnaryOperation(['a | b'], '*')], '?')])

    def testUnpack(self):
        self.assertEqual(parser.unpack(['a','b','c', ['a',['b'], 'c'], ['a'], ['x', 'y']], [3, 5]), ['a','b','c', 'a', ['b'], 'c', ['a'], 'x', 'y'])