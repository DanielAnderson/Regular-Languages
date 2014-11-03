from collections import defaultdict
class DeltaStar(defaultdict):
	"""Almost functionally identical to a defaultdict, except:
	This has a default value of False and
	The dict prints the key.__str__() rather than just the key"""
	def __init__(self):
		defaultdict.__init__(self, lambda: set(), {})

	def __str__(self):
		answer = "{"
		iterator = iter(self)
		comma = False
		for key in iterator:
			if comma:
				answer = answer + ', '
			else:
				comma = True

			answer = answer + key.__str__() +": " + self[key].__str__()
		answer = answer + "}"
		return answer

