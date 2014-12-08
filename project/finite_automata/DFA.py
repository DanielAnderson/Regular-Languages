class DFA:
    def __init__(self, equivNFA):
        self.myNFA = equivNFA
        startState = set()
        startState.add(equivNFA.startState)
        
        self.startState = frozenset(startState)
        self.states = set()
        
        toAdd = list()
        toAdd.append(self.startState)

        while(len(toAdd) > 0):
            state = toAdd.pop()
            if(state not in self.states):
                self.states.add(state)
                for character in self.myNFA.alphabet:
                    toAdd.append(frozenset(self.myNFA.applyTransition(state, character)))


