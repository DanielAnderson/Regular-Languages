import json
from project.finite_automata.NFA import NFA
import project.finite_automata.constants as constants

"""Creates a NFA based on a JSON"""
def createNFA(theJSON):
	theJSON = json.loads(theJSON)
	verifyNFA(theJSON)
	states = set(theJSON['states'])
	alphabet = set(theJSON['alphabet'])
	startState = theJSON['startState']
	finalStates = theJSON['finalStates']
	theNFA = NFA(states, alphabet, startState, finalStates)
	addMovesFromJSON(theJSON, theNFA)
	return theNFA

"""Goes thruogh all of the moves in the JSON and and adds the appropriate moves to it"""
def addMovesFromJSON(theJSON, theNFA):
	moves = theJSON['moves']

	for state in moves:
		for inputSymbol in moves[state]:
			#Converts string to an array including only that string
			#leaves arrays alone
			results = convertToList(moves[state][inputSymbol])
			for result in results:
				theNFA.addMove(state, inputSymbol, result)

"""Verifies that the NFA is valid"""
def verifyNFA(theJSON):
	assert theJSON['startState'] in theJSON['states']
	assert 'lambda' not in theJSON['alphabet']
	moves = theJSON['moves']
	for state in moves:
		assert state in theJSON['states']
		for alphabetMember in moves[state]:
			assert alphabetMember in theJSON['alphabet'] or alphabetMember == constants.LAMBDA
			for nextState in convertToList(moves[state][alphabetMember]):
				assert nextState in theJSON['states']


"""Converts a string or list into a list"""
def convertToList(stringOrList):
	if type(stringOrList) is list:
		return stringOrList
	else:
		return [stringOrList]

