from project.finite_automata.moveFunction import MoveFunction
import project.finite_automata.constants as constants
from project.finite_automata.DFA import DFA
"""Converts a string, list or set into a set"""
def convertToSet(stringListOrSet):
	if type(stringListOrSet) is set or type(stringListOrSet) is list:
		return set(stringListOrSet)
	else:
		answer = set()
		answer.add(stringListOrSet)
		return answer

class NFA:
	"""This class represents an NFA, and once constructed, can tell whether a given string is an element of the language generated by this NFA"""
	
	"""states, alphabet should be sets, startState, finalStates should be elements of states"""
	def __init__(self, states, alphabet, startState, finalStates):
		self.states = states
		self.alphabet = alphabet 
		self.startState = startState
		self.finalStates = convertToSet(finalStates)
		self.deltaFunction = MoveFunction()

	"""Extension of __init__. Should be finished before testing strings"""
	def addMove(self, initialState, inputSymbol, results):
		# Checks if the state is a valid state, if the input symbol is a valid input symbol, and that the resultant states are valid states
		results = convertToSet(results)
		assert initialState in self.states 
		assert inputSymbol in self.alphabet or inputSymbol == constants.LAMBDA
		assert results <= self.states 
		if inputSymbol == constants.LAMBDA:
			self.deltaFunction.addLambdaMove(initialState, results)
		else:
			self.deltaFunction.addMove(initialState, inputSymbol, results)

	"""Determines whether or not a string is in the language generated by this machine"""
	def isInLanguage(self, string):
		currentStates = convertToSet(self.startState)

		for character in string:
			assert character in self.alphabet
			currentStates = self.applyTransition(currentStates, character)
		return len(currentStates & self.finalStates) > 0

	"""Takes a set of states and determines the set of states that can be reached by repeatedly applying lambda moves to that set
	Does not mutate passed states"""
	def applyLambdaMoves(self, states):
		states = states.copy()
		originalSize = len(states)
		nextStates = self.applyLambdaOnce(states)
		states |= nextStates
		nextSize = len(states)
		while nextSize > originalSize:
			originalSize = nextSize
			nextStates = self.applyLambdaOnce(states)
			states |= nextStates
			nextSize = len(states)
		return states



	"""Applys all lambda moves one time. Does not mutate state"""
	def applyLambdaOnce(self, states):
		nextStates = set()
		for state in states:
			nextStates |= self.deltaFunction.getLambdaResults(state)
		return nextStates

	def toDFA(self):
		return DFA(self)

	"""Given a set of states and an input symbol, returns the set of states after the symbol has been read. 
	Takes care of all lambda moves (before and after the input symbol is read)"""
	def applyTransition(self, states, inputSymbol):
		lambdaApplied = self.applyLambdaMoves(states)
		characterRead = self.readCharacter(lambdaApplied, inputSymbol)
		answer = self.applyLambdaMoves(characterRead)
		return answer

	""""Returns the result of reading a character. Does not apply lambda moves"""
	def readCharacter(self, states, character):
		answer = set()
		for state in states:
			answer |= self.deltaFunction.getResults(state, character)
		return answer


	"""Converts this to a string"""
	def __str__(self):
		return "{\n\t" + "Q: " + self.states.__str__() + "\n\t" + "Σ: " + self.alphabet.__str__() + "\n\t" + "δ: " + self.deltaFunction.__str__() + "\n\t" + "q0: " + self.startState.__str__() + "\n\tF: " +self.finalStates.__str__() + "\n}"


