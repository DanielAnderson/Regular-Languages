import unittest
from project.regular_grammar.Grammar import Grammar
from project.regular_grammar import jsonToGrammar
class TestGrammar(unittest.TestCase):
	def setUp(self):
	#terminals infront and only one of them 
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
        #terminals in the front of but a string
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
        #termials in the rear
		self.json3= '''
        {
            "Variables": ["S", "A"],
            "alphabet": ["a"],
            "startVariable": "S",
            "Productions":
                {
                    "S": {
                        "A":"a"
                    },
                    "A": {
                        "lambda":"a"
                    }
                }
        }
        '''
        #terminals in the rear and a string
		self.json4= '''
        {

            "Variables": ["S", "A"],
            "alphabet": ["a"],
            "startVariable": "S",
            "Productions":
                {
                    "S": {
                        "A":"aa"
                    },
                    "A": {
                        "lambda":"a"
                    }
                }
        }
        '''
        #multiple letters
		self.json5= '''
        {
            "Variables": ["S", "A"],
            "alphabet": ["a", "b"],
            "startVariable": "S",
            "Productions":
                {
                    "S": {
                        "aa":"A"
                    },
                    "A": {
                        "b":"lambda"
                    }
                }
        }
        '''
        #multiple moves
		self.json6= '''
        {
            "Variables": ["S", "A"],
            "alphabet": ["a", "b"],
            "startVariable": "S",
            "Productions":
                {
                    "S": {
                        "A":"aa",
                        "S":"b"
                    },
                    "A": {
                        "lambda":"b"
                    }
                }
        }
        '''	
        #multiple moves with the 	
		self.json7= '''
        {
            "Variables": ["S", "A"],
            "alphabet": ["a", "b"],
            "startVariable": "S",
            "Productions":
                {
                    "S": {
                        "aa":"A",
                        "a":"S"
                    },
                    "A": {
                        "b":"lambda"
                    }
                }
        }
        '''

	def test_verify_grammar1(self):
		jsonToGrammar.createGrammar(self.json1)

	def test_verify_grammar2(self):
		jsonToGrammar.createGrammar(self.json2)

	def test_verify_grammar3(self):
		jsonToGrammar.createGrammar(self.json3)

	def test_verify_grammar4(self):
		jsonToGrammar.createGrammar(self.json4)

	def test_verify_grammar5(self):
		jsonToGrammar.createGrammar(self.json5)

	def test_verify_grammar6(self):
		jsonToGrammar.createGrammar(self.json6)
	
	def test_verify_grammar7(self):	
		jsonToGrammar.createGrammar(self.json7)
	
	def test_string_grammar1(self):
		self.assertTrue(jsonToGrammar.createGrammar(self.json1).isInLanguage("aa"))

	def test_string_grammar2(self):
		self.assertTrue(jsonToGrammar.createGrammar(self.json2).isInLanguage("aaa"))

	def test_string_grammar3(self):
		self.assertTrue(jsonToGrammar.createGrammar(self.json3).isInLanguage("aa"))

	def test_string_grammar4(self):
		self.assertTrue(jsonToGrammar.createGrammar(self.json4).isInLanguage("aaa"))

	def test_string_grammar5(self):
		self.assertTrue(jsonToGrammar.createGrammar(self.json5).isInLanguage("aab"))

	def test_string_json6(self):
		self.assertTrue(jsonToGrammar.createGrammar(self.json6).isInLanguage("baab"))

	def test_string_json7(self):
		self.assertTrue(jsonToGrammar.createGrammar(self.json7).isInLanguage("aaab"))

	def test_stringThatDontWork_grammar1(self):
		self.assertFalse(jsonToGrammar.createGrammar(self.json1).isInLanguage("aaa"))

	def test_stringThatDontWork_grammar2(self):
		self.assertFalse(jsonToGrammar.createGrammar(self.json2).isInLanguage("aaaa"))

	def test_stringThatDontWork_grammar3(self):
		self.assertFalse(jsonToGrammar.createGrammar(self.json3).isInLanguage("aaa"))

	def test_stringThatDontWork_grammar4(self):
		self.assertFalse(jsonToGrammar.createGrammar(self.json4).isInLanguage("aaaa"))

	def test_stringThatDontWork_grammar5(self):
		self.assertFalse(jsonToGrammar.createGrammar(self.json5).isInLanguage("aaaa"))
 
	def test_stringThatDontWork_grammar6(self):
		self.assertFalse(jsonToGrammar.createGrammar(self.json6).isInLanguage("aaaa"))

	def test_stringThatDontWork_grammar7(self):
		self.assertFalse(jsonToGrammar.createGrammar(self.json7).isInLanguage("aaaa"))

