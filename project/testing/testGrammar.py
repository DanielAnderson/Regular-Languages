import unittest
from project.regular_grammar.Grammar import Grammar
from project.regular_grammar import jsonToGrammar
class TestGrammar(unittest.TestCase):
	def setUp(self):
		self.json1= '''
        {
            "Variables": ["S", "B"],
            "alphabet": ["a"],
            "startVariable": "S",
            "Productions":
                {
                    "S": {
                        "a": ["B"]
                    },
                    "B": {
                        "a": ["lambda"]
                    }
                }
        }
        '''
		self.json2= '''
        {
    "Variables": [
        "S",
        "A"
    ],
    "alphabet": [
        "a"
    ],
    "startVariable": "S",
    "Productions": {
        "S": {
            "aa": "A"
        },
        "A": {
            "a": [
                "lambda"
            ]
        }
    }
}
        '''
		self.json3= '''
        {
            "Variables": ["S", "A"],
            "alphabet": ["a"],
            "startVariable": "S",
            "Productions":
                {
                    "S": {
                        "A":["a"]
                    },
                    "A": {
                        "lambda":["a"]
                    }
                }
        }
        '''
        
		self.json4= '''
        {
            "Variables": ["S", "A"],
            "alphabet": ["a"],
            "startVariable": "S",
            "Productions":
                {
                    "S": {
                        "A":["aa"]
                    },
                    "A": {
                        "lambda":["a"]
                    }
                }
        }
        '''

	def test_verify_json1(self):
		jsonToGrammar.createGrammar(self.json1)

	def test_verify_json2(self):
		jsonToGrammar.createGrammar(self.json2)

	def test_verify_json3(self):
		jsonToGrammar.createGrammar(self.json3)

	def test_verify_json4(self):
		jsonToGrammar.createGrammar(self.json4)



	
        



