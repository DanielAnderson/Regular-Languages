import json
from project.finite_automata.NFA import NFA
def createNFA(theJSON):
	theJSON = json.loads(theJSON)
	# todo
	# valid = verifyNFA(theJSON)
	states = set(theJSON['states'])
	alphabet = set(theJSON['alphabet'])
	startState = theJSON['startState']
	finalStates = theJSON['finalStates']
	theNFA = NFA(states, alphabet, startState, finalStates)
	addMovesFromJSON(theJSON, theNFA)
	return theNFA

def addMovesFromJSON(theJSON, theNFA):
	moves = theJSON['moves']
	for state in moves:
		for inputSymbol in moves[state]:
			#Converts string to an array including only that string
			#leaves arrays alone
			results = convertToList(moves[state][inputSymbol])
			for result in results:
				theNFA.addMove(state, inputSymbol, result)

def verifyNFA(theJSON):
	# todo
	return true

def convertToList(stringOrList):
	if type(stringOrList) is list:
		return stringOrList
	else:
		return [stringOrList]

