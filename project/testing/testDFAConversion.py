import unittest
from project.finite_automata.DFA import DFA
from project.finite_automata.NFA import NFA
from project.finite_automata import jsonToNFA

class TestDFAConversion(unittest.TestCase):
    def setUp(self):
        # Page 58 in An Introduction to Formal Languages and Automata 5th edition
        theNFA = """
        {
            "states": ["q0", "q1", "q2"],
            "alphabet": ["a", "b"],
            "startState": "q0",
            "finalStates": "q1",
            "moves" :
            {
                "q0": {
                    "a": "q1"
                },
                "q1": {
                    "a": "q1",
                    "lambda": "q2"
                },
                "q2": {
                    "b": "q0"
                }
            }
        }"""
        self.theNFA = jsonToNFA.createNFA(theNFA)

        # Page 60, 61
        NFA2 = """
        {
            "states": ["q0", "q1", "q2"],
            "alphabet": ["0", "1"],
            "startState": "q0",
            "finalStates": "q1",
            "moves" :
            {
                "q0": {
                    "0": ["q0", "q1"],
                    "1": "q1"
                },
                "q1": {
                    "0": "q2",
                    "1": "q2"
                },
                "q2": {
                    "1": "q2"
                }
            }
        }"""
        self.NFA2 = jsonToNFA.createNFA(NFA2)

    def testStateGeneration1(self):
        theDFA = DFA(self.theNFA)
        self.assertEqual(theDFA.states, {'q0','q1','q2'})
            
    def testStateGeneration2(self):
        theDFA = DFA(self.NFA2)
        self.assertEqual(theDFA.states, {'q0','q1','q2','q3','q4','q5','q6'})
