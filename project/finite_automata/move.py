class Move:
    """Represents a move- with a state (string) and input symbol (string)"""
    def __init__(self, state, inputSymbol):
        self.myState = state
        self.myInputSymbol = inputSymbol

    """Getter"""
    def state(self):
        return self.myState

    """Getter"""
    def inputSymbol(self):
        return self.myInputSymbol

    """This move is equal to another iff the states are the same and the input symbols are the same"""
    def __eq__(self, other):
        return self.myState == other.myState and self.myInputSymbol == other.myInputSymbol

    """The hash of this is the xor of the hash of the state and the symbol"""
    def __hash__(self):
        return self.myState.__hash__() ^ self.myInputSymbol.__hash__()

    """Returns string representation of this object"""
    def __str__(self):
        return "(" + self.myState.__str__() + ", " + self.myInputSymbol.__str__() +")"
