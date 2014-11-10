from project.finite_automata.deltaStar import DeltaStar

class Move:
	"""Represents a move- with a state (string) and input symbol (string)"""
	def __init__(self, state, inputSymbol):
		self.myState = state
		self.myInputSymbol = inputSymbol

	def state(self):
		return self.myState

	def inputSymbol(self):
		return self.myInputSymbol

	def __eq__(self, other):
		return self.myState == other.myState and self.myInputSymbol == other.myInputSymbol

	def __hash__(self):
		return self.myState.__hash__() ^ self.myInputSymbol.__hash__()

	def __str__(self):
		return "(" + self.myState.__str__() + ", " + self.myInputSymbol.__str__() +")"



class MoveFunction:
	"""This class is used to keep track of and map the moves that a NFA has"""
	def __init__(self):
		# Using DeltaStar, which inherits from defaultdict rather than the base dictionary so that False is returned rather than throwing an exception when a non existant key is used
		self.moves = DeltaStar()

	def addMove(self, initialState, inputSymbol, results):
		move = Move(initialState, inputSymbol)
		previousResult = self.moves[move]

		if(previousResult):
			self.moves[move] = previousResult | set(results)
		else:
			self.moves[move] = set(results);

	def getResults(self, initialState, inputSymbol):
		return self.moves[Move(initialState, inputSymbol)]

	def __str__(self):
		return str(self.moves)

a = Move('q1', 'a')





