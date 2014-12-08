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

        return currentState & self.myNFA.finalStates
