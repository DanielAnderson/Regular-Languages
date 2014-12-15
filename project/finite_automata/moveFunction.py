from project.finite_automata.deltaStar import DeltaStar
import project.finite_automata.constants as constants
from project.finite_automata.move import Move
class LambdaMove(Move):
	def __init__(self, state):
		super().__init__(state, constants.LAMBDA)



class MoveFunction:
	"""This class is used to keep track of and map the moves that a NFA has"""
	def __init__(self):
		# Using DeltaStar, which inherits from defaultdict rather than the base dictionary so that False is returned rather than throwing an exception when a non existant key is used
		self.moves = DeltaStar()
		self.lambdaMoves = DeltaStar()

	def addMove(self, initialState, inputSymbol, results):
		move = Move(initialState, inputSymbol)
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


	def getResults(self, initialState, inputSymbol):
		return self.moves[Move(initialState, inputSymbol)]

	def getLambdaResults(self, initialState):
		return self.lambdaMoves[LambdaMove(initialState)]

	def __str__(self):
		return str(self.moves)






