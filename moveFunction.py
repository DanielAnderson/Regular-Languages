from collections import defaultdict
from move import Move
from deltaStar import DeltaStar
class MoveFunction:
	"""This class is used to keep track of and map the moves that a NFA has"""
	def __init__(self):
		# Using DeltaStar, which inherits from defaultdict rather than the base dictionary so that False is returned rather than throwing an exception when a non existant key is used
		self.moves = DeltaStar()

	def addMove(self, move, results):
		previousResult = self.moves[move]

		if(previousResult):
			self.moves[move] = previousResult | set(results)
		else:
			self.moves[move] = set(results);

	def getResults(self, move):
		return self.moves[move]

	def __str__(self):
		return str(self.moves)

a = Move('q1', 'a')
