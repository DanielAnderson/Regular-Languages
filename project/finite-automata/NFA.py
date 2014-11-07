from moveFunction import MoveFunction

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

	def addMove(self, initialState, inputSymbol, results):
		# Checks if the state is a valid state, if the input symbol is a valid input symbol, and that the resultant states are valid states
		results = convertToSet(results)
		assert initialState in self.states 
		assert inputSymbol in self.alphabet 
		assert results <= self.states 
		self.deltaFunction.addMove(initialState, inputSymbol, results)

	def isInLanguage(self, string):
		currentStates = convertToSet(self.startState)

		for character in string:
			nextStates = set()
			for state in currentStates: 
				nextStates |= self.deltaFunction.getResults(state,character)
			currentStates = nextStates
		return len(currentStates & self.finalStates) > 0


	def __str__(self):
		return "{\n\t" + "Q: " + self.states.__str__() + "\n\t" + "Σ: " + self.alphabet.__str__() + "\n\t" + "δ: " + self.deltaFunction.__str__() + "\n\t" + "q0: " + self.startState.__str__() + "\n\tF: " +self.finalStates.__str__() + "\n}"


nfa = NFA(states={"q1","q2"}, alphabet={"a","b"}, startState="q1", finalStates="q1")
nfa.addMove("q1", "a", "q1")
nfa.addMove("q2", "a", "q2")
nfa.addMove("q2", "b", "q1")
nfa.addMove("q1", "b", "q2")

print(nfa.isInLanguage("bbbabaaabbb"))
