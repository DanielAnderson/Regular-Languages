from project.regular_grammar.deltaStar import DeltaStar
import project.regular_grammar.constants as constants

class Move:
	"""Represents a move- with a state (string) and input symbol (string)"""
	def __init__(self, variable, inputSymbol):
		self.myVariable = variable
		self.myInputSymbol = inputSymbol
        	
	def state(self):
		return self.myVariable

	def inputSymbol(self):
		return self.myInputSymbol
        	
	def __eq__(self, other):
		return self.myVariable == other.myVariable and self.myInputSymbol == other.myInputSymbol

	def __hash__(self):
		return self.myVariable.__hash__() ^ self.myInputSymbol.__hash__()

	def __str__(self):
		return "(" + self.myVariable.__str__() + ", " + self.myInputSymbol.__str__() +")"

class LambdaMove(Move):
	def __init__(self, variable):
		super().__init__(variable, constants.LAMBDA)



class MoveFunction:
	"""This class is used to keep track of and map the moves that a NFA has"""
	def __init__(self):
		# Using DeltaStar, which inherits from defaultdict rather than the base dictionary so that False is returned rather than throwing an exception when a non existant key is used
		self.moves = DeltaStar()
		self.lambdaMoves = DeltaStar()

	def addMove(self, initialVariable, inputSymbol, results):
		move = Move(initialVariable, inputSymbol)
		previousResult = self.moves[move]

		if(previousResult):
			self.moves[move] = previousResult | set(results)
		else:
			self.moves[move] = set(results);

	def addLambdaMove(self, initialState, results):
		move = LambdaMove(initialState)
		previousResult = self.lambdaMoves[move]

		if(previousResult):
			self.lambdaMoves[move] = previousResult | set(results)
		else:
			self.lambdaMoves[move] = set(results)


	def getResults(self, initialVariable, inputSymbol):
		return self.moves[Move(initialVariable, inputSymbol)]

	def getLambdaResults(self, initialVariable):
		return self.lambdaMoves[LambdaMove(initialVariable)]

	def __str__(self):
		return str(self.moves)


