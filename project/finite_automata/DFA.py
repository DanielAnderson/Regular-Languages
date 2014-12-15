from project.finite_automata.move import Move

class DFA:
    def __init__(self, equivNFA):
        self.myNFA = equivNFA
        startState = set()
        startState.add(equivNFA.startState)
        
        self.startState = frozenset(startState)
        self.states = set()

        self.moves = dict()

        self.generateStates()
        
        self.convertStates()
        
    """Converts from having each state as a frozenset to having normal states, determines final states"""
    def convertStates(self):
        newStates = dict()
        newMoves = dict()
        self.finalStates = set()
        
        for index, state in enumerate(self.states):
            newStates[state] = index
            if(state & self.myNFA.finalStates):
                self.finalStates.add(index)
            if(self.startState == state):
                self.startState = index
        
        for move in self.moves:
            previousMove = move
            previousStartState = move.state()
            previousResult = self.moves[move]
            
            nextMove = Move(newStates[previousStartState], move.inputSymbol())
            newMoves[nextMove] = newStates[previousResult]
        
        self.moves = newMoves
        
    def generateStates(self):
        toAdd = list()
        toAdd.append(self.startState)

        while(len(toAdd) > 0):
            state = toAdd.pop()
            if(state not in self.states):
                self.states.add(state)
                for character in self.myNFA.alphabet:
                    result = frozenset(self.myNFA.applyTransition(state, character))
                    self.addMove(state, character, result)
                    toAdd.append(result)

    def addMove(self, state, character, result):
        move = Move(state, character)
        self.moves[move] = result

    def isInLanguage(self, string):
        currentState = self.startState
        for character in string:
            move = Move(currentState, character)
            currentState = self.moves[move]

        return currentState in self.finalStates
    
    """Returns a new DFA for this language that is minimized"""    
    """def minimize(self):
        association = dict()
        for(state in self.states):
            if state in """
