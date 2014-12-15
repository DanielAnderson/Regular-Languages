from project.finite_automata.NFA import NFA
from project.regular_grammar.moveFunction import MoveFunction
import project.regular_grammar.constants as constants
import project.finite_automata.jsonToNFA as createNFA
class Grammar:
    def __init__(self, variables, alphabet, startVariable):
        self.variables = variables;
        self.alphabet = alphabet
        self.startVariable = startVariable
        self.finalVariables = set()
        self.productions = moveFunction()
        #create theNFA
        theJSON= json.dump(
					{
						"states": self.variables, 
						"alphabet": self.alphabet, 
						"startState": self.startVariable, 
						"finalStates":  self.finalVariables, 
						"moves" : self.productions
					})
        self.theNFA =createNFA(theJSON)

    def addMove(self, initialVariable, inputSymbol, results):
        assert initialVariable in self.variables
        assert inputSymbol in self.alphabet or results == constants.LAMBDA
        assert results in self.variable or results == constants.LAMBDA
        if results == constants.LAMDA:
            self.finalVariables.add(initialVariable)
        if inputSymbol == constants.LAMDA:
            self.productions.addLambdaMove(initialVariable, results)
        else:
            self.productions.addMove(initialVariable, inputSymbol, results)

    
    def isInLanguage(self, string):
        assert len(finalVariables) > 0
        return self.NFA.isInLanguage(self,string)

    def __str__(self):
    	return "{\n\t" + "Q: " + self.variables.__str__() + "\n\t" + "Σ: " + self.alphabet.__str__() + "\n\t" + "δ: " + self.productions.__str__() + "\n\t" + "q0: " + self.startVariable.__str__() + "\n\tF: " +self.finalVariables.__str__() + "\n}"
    def NFA(self):
    	return self.theNFA
