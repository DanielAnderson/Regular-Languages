import unittest
from project.regular_grammar.Grammar import Grammar
from project.regular_grammar import jsonToGrammar
class TestGrammarVerifier(unittest.TestCase):
	def setUp(self):
		self.illegal_start_Variable = '''
        {
    			"Variables": ["S", "A"],
    			"alphabet": [ "a" ],
    			"startVariable": "B",
    			"Productions": 
    				{
        				"S": {
            			"a": [ "A" ]
        				},
        				"A": {
            			"a": [ "lambda"]
        				}
    				}
			}
        '''
		self.illegal_alphabet = '''
        {
            "Variables": ["S", "A"],
            "alphabet": ["lambda", "a"],
            "startVariable": "S",
            "Productions":
                {
                    "S": {
                        "a": ["A"]
                    },
                    "A": {
                        "a": ["lambda"]
                    }
                }
        }
        '''

		self.illegal_move_Variables = '''
        {
            "Variables": ["S", "A"],
            "alphabet": ["a"],
            "startVariable": "S",
            "Productions":
                {
                    "foo_bar": {
                        "a": ["A"]
                    },
                    "A": {
                        "a": ["lambda"]
                    }
                }
        }
        '''

		self.illegal_move_alphabet = '''
        {
            "Variables": ["S", "A"],
            "alphabet": ["a"],
            "startVariable": "S",
            "Productions":
                {
                    "S": {
                        "foo_bar": ["A"]
                    },
                    "A": {
                        "a": ["lambda"]
                    }
                }
        }
        '''
        
		self.illegal_move_Variables = '''
        {
            "Variables": ["S", "A"],
            "alphabet": ["a"],
            "startVariable": "S",
             "Productions":
                {
                    "S": {
                        "a": ["A","A"]
                    },
                    "A": {
                        "a": ["lambda"]
                    }
                }
        }
        '''


		self.illegal_no_end_Variables = '''
        {
            "Variables": ["S", "A"],
            "alphabet": ["a"],
            "startVariable": "S",
             "Productions":
                {
                    "S": {
                        "a": ["A"]
                    },
                    "A": {
                        "a": ["S"]
                    }
                }
        }
        '''



	def test_verify_start_Variable(self):
		self.assertRaises(AssertionError, jsonToGrammar.createGrammar, self.illegal_start_Variable)

	def test_verify_illegal_alphabet(self):
		self.assertRaises(AssertionError, jsonToGrammar.createGrammar, self.illegal_alphabet)

	def test_verify_illegal_move_Variables(self):
		self.assertRaises(AssertionError, jsonToGrammar.createGrammar, self.illegal_move_Variable)

	def test_verify_illegal_move_alphabet(self):
		self.assertRaises(AssertionError, jsonToGrammar.createGrammar, self.illegal_move_alphabet)

	def test_verify_illegal_move_end_Variables(self):
		self.assertRaises(AssertionError, jsonToGrammar.createGrammar, self.illegal_move_Variable)

	def test_verify_illegal_move_end_Variables(self):
		self.assertRaises(AssertionError, jsonToGrammar.createGrammar, self.illegal_no_end_Variable)
