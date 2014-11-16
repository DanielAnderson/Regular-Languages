import unittest
from project.finite_automata.NFA import NFA
from project.finite_automata import jsonToNFA
class TestNFAVerifier(unittest.TestCase):
    def setUp(self):
        self.illegal_start_state = '''
        {
            "states": ["q0", "q1"],
            "alphabet": ["a"],
            "startState": "q2",
            "finalState": "q1",
            "moves":
                {
                    "q0": {
                        "a": "q1"
                    },
                    "q1": {
                        "a": "q0"
                    }
                }
        }
        '''
        self.illegal_alphabet = '''
        {
            "states": ["q0", "q1"],
            "alphabet": ["lambda", "a"],
            "startState": "q0",
            "finalState": "q1",
            "moves":
                {
                    "q0": {
                        "a": "q1"
                    },
                    "q1": {
                        "a": "q0"
                    }
                }
        }
        '''

        self.illegal_move_state = '''
        {
            "states": ["q0", "q1"],
            "alphabet": ["a"],
            "startState": "q0",
            "finalState": "q1",
            "moves":
                {
                    "foo_bar": {
                        "a": "q1"
                    },
                    "q1": {
                        "a": "q0"
                    }
                }
        }
        '''

        self.illegal_move_alphabet = '''
        {
            "states": ["q0", "q1"],
            "alphabet": ["a"],
            "startState": "q0",
            "finalState": "q1",
            "moves":
                {
                    "q0": {
                        "foo_bar": "q1"
                    },
                    "q1": {
                        "a": "q0"
                    }
                }
        }
        '''
        
        self.illegal_move_end_state = '''
        {
            "states": ["q0", "q1"],
            "alphabet": ["a"],
            "startState": "q0",
            "finalState": "q1",
            "moves":
                {
                    "q0": {
                        "a": "foo_bar"
                    },
                    "q1": {
                        "a": "q0"
                    }
                }
        }
        '''


    def test_verify_start_state(self):
        self.assertRaises(AssertionError, jsonToNFA.createNFA, self.illegal_start_state)

    def test_verify_illegal_alphabet(self):
        self.assertRaises(AssertionError, jsonToNFA.createNFA, self.illegal_alphabet)

    def test_verify_illegal_move_state(self):
        self.assertRaises(AssertionError, jsonToNFA.createNFA, self.illegal_move_state)

    def test_verify_illegal_move_alphabet(self):
        self.assertRaises(AssertionError, jsonToNFA.createNFA, self.illegal_move_alphabet)

    def test_verify_illegal_move_end_state(self):
        self.assertRaises(AssertionError, jsonToNFA.createNFA, self.illegal_move_end_state)


