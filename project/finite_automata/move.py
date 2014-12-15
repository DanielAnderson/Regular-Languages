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
