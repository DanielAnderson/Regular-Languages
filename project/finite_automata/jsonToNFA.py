import json
from project.finite_automata.NFA import NFA
def createNFA(theJSON):
	theJSON = json.loads(theJSON)
	# todo
	# valid = verifyNFA(theJSON)
	theNFA = NFA(set(theJSON['states']), set(theJSON['alphabet']), theJSON['startState'], theJSON['finalStates'])
	addMovesFromJSON(theJSON, theNFA)
	return theNFA

def addMovesFromJSON(theJSON, theNFA):
	moves = theJSON['moves']
	for state in moves:
		for inputSymbol in moves[state]:
			for result in moves[state][inputSymbol]:
				theNFA.addMove(state, inputSymbol, result)

def verifyNFA(theJSON):
	# todo
	return true

theJSON = '{"states": ["q1", "q2"], "alphabet": ["a","b"], "startState": "q1", "finalStates": ["q1"], "moves" : {"q1": {"a": ["q1"], "b": ["q2"]}, "q2": {"a": ["q2"], "b": ["q1"]}}}'
theNFA = createNFA(theJSON)
print(theNFA)