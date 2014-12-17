from project.finite_automata.move import Move
import json

class DFA:
    def __init__(self, equivNFA):
        self.myNFA = equivNFA
        startState = set()
        startState.add(equivNFA.startState)
        self.alphabet = equivNFA.alphabet
        
        self.startState = frozenset(startState)
        self.states = set()

        self.moves = dict()

        self.generateStates()
        
        self.convertStates()
        
    """Converts from having each state as a frozenset to having normal states, determines final states"""
    def convertStates(self):
        statesDict = dict()
        newMoves = dict()
        self.finalStates = set()
        newStates = set()
        
        for index, state in enumerate(self.states):
            newName = "q" + str(index)
            statesDict[state] = newName
            if(state & self.myNFA.finalStates):
                self.finalStates.add(newName)
            if(self.startState == state):
                self.startState = newName
            newStates.add(newName)
        
        for move in self.moves:
            previousMove = move
            previousStartState = move.state()
            previousResult = self.moves[move]
            
            nextMove = Move(statesDict[previousStartState], move.inputSymbol())
            newMoves[nextMove] = statesDict[previousResult]
        
        self.moves = newMoves
        self.states = newStates
        
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

# '''
#                     {
#                         "states": ["q1", "q2"], 
#                         "alphabet": ["a","b"], 
#                         "startState": "q1", 
#                         "finalStates": ["q1"], 
#                         "moves" : 
#                             {
#                                 "q1": {
#                                     "a": ["q1"],
#                                     "b": ["q2"]
#                                     },
#                                 "q2": {
#                                     "a": ["q2"], 
#                                     "b": ["q1"]
#                                     }
#                             }
#                     }'''

    def __str__(self):
        ans = "{\n\t"
        ans += '"states": ' + setToListString(self.states) + ","
        ans += '\n\t"alphabet": ' + setToListString(self.alphabet) + ","
        ans += '\n\t"startState": ' + '"' + self.startState + '"' + ","
        ans += '\n\t"finalStates": ' + setToListString(self.finalStates) + ","
        ans += '\n\t"moves":' + self.movesToString()
        ans += '}'
        return ans

    def movesToString(self):
        conversionDict = dict()
        for move in self.moves:
            originalState = move.state()
            inputSymbol = move.inputSymbol()
            result = self.moves[move]
            if originalState not in conversionDict.keys():
                conversionDict[originalState] = dict()

            conversionDict[originalState][inputSymbol] = result
            
        ans = "{\n"

        for state in conversionDict:
            toAdd = "\n" + json.dumps(conversionDict[state], sort_keys=True, indent=4)
            toAdd = toAdd.replace("\n", "\n\t\t\t")
            ans += toAdd
            ans += ','
        ans = ans[0:-1]
        ans += "\n\t\t}\n"

        return ans

def setToListString(theSet):
    ans = "["
    for element in theSet:
        ans += '"' + str(element) + '"' + ", "

    ans = ans[0: -2] + "]"
    return ans


    
    """Returns a new DFA for this language that is minimized"""    
    """def minimize(self):
        association = dict()
        for(state in self.states):
            if state in """
