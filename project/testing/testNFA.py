import unittest
from project.finite_automata.NFA import NFA
from project.finite_automata import jsonToNFA
class TestNFA(unittest.TestCase):
	def setUp(self):

		self.json1 = '''
					{
						"states": ["q1", "q2"], 
						"alphabet": ["a","b"], 
						"startState": "q1", 
						"finalStates": ["q1"], 
						"moves" : 
							{
								"q1": {
									"a": ["q1"],
									"b": ["q2"]
									},
								"q2": {
									"a": ["q2"], 
									"b": ["q1"]
									}
							}
					}'''
		self.machine1 = jsonToNFA.createNFA(self.json1)
		
		self.json2 = '''
		{
			"states": ["q0", "q1", "q2", "q3", "q4", "q5"],
			"alphabet": ["a"],
			"startState": "q0",
			"finalStates": ["q4"],
			"moves":
				{
					"q0": {
							"a": "q1"
						},
					"q1": {
							"a": "q2"
						},
					"q2": {
							"a": "q3"
						},
					"q3": {
							"a": "q4"
						},
					"q4": {
							"a": "q5"
						},
					"q5": {
							"a": "q0"
						}
				}

		}
		'''
		self.machine2 = jsonToNFA.createNFA(self.json2)

	def test_accept_NFA1(self):
		self.assertTrue(self.machine1.isInLanguage('aaabbaaabb'))
	def test_deny_NFA1(self):
		self.assertFalse(self.machine1.isInLanguage('aabbb'))
	def test_empty_NFA1(self):
		self.assertTrue(self.machine1.isInLanguage(''))
	def test_raises_NFA1(self):
		self.assertRaises(AssertionError, self.machine1.isInLanguage,'c')
	def test_JSON_parser(self):
		# Note, we are just calling the function here. That is to test to see that the function doesn't fail
		jsonToNFA.createNFA(self.json1)
	
	def test_accept_NFA2(self):
		self.assertTrue(self.machine2.isInLanguage('aaaaaaaaaa'))
	def test_deny_NFA2(self):
		self.assertFalse(self.machine2.isInLanguage('aaaaa'))
	def test_empty_NFA2(self):
		self.assertFalse(self.machine2.isInLanguage(''))
	def test_raises_NFA2(self):
		self.assertRaises(AssertionError, self.machine2.isInLanguage, 'aaaaaaaaaaaab')
	def test_JSON_parser2(self):
		jsonToNFA.createNFA(self.json2)
