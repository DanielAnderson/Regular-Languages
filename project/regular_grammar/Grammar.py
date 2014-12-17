import json
import project.finite_automata.NFA as NFA
from project.regular_grammar.moveFunction import MoveFunction
import project.regular_grammar.constants as constants
from project.finite_automata.jsonToNFA import createNFA
class Grammar:
    def __init__(self, variables, alphabet, startVariable):
        self.variables = variables
        self.alphabet = alphabet
        self.startVariable = startVariable
        self.finalVariables = "F"
        self.productions = MoveFunction()
        self.variables.add("F")
        self.isRight=True
    
        
        
        

    def addMove(self, initialVariable, inputSymbol, results):
    	
    	assert initialVariable in self.variables
    	#assert inputSymbol in self.alphabet or results == constants.LAMBDA
        # assert results in self.variables or results == constants.LAMBDA
    	for val in results:
    		
	    	if val == "lambda":
	    		
    			self.productions.addMove(initialVariable, inputSymbol, "F")
    		elif inputSymbol == "lambda":
    			self.productions.addLambdaMove(initialVariable, results)
    		else:
    			
    			self.productions.addMove(initialVariable, inputSymbol, results)
    	


    
    def isInLanguage(self, string):
        return self.theNFA.isInLanguage(string)

    def __str__(self):
    	return "{\n\t" + "Q: " + self.variables.__str__() + "\n\t" + "Σ: " + self.alphabet.__str__() + "\n\t" + "δ: " + self.productions.__str__() + "\n\t" + "S: " + self.startVariable.__str__() + "\n\tF: " +self.finalVariables.__str__() + "\n}"
    	
    	
    	
    def NFA(self):
    	jsonDict = dict()
    	
    	
    	
    	 
    	jsonDict["states"] = list(self.variables)
    	jsonDict["alphabet"] = list(self.alphabet)
    	if self.isRight:
    		jsonDict["startState"] = self.startVariable
    	
    		jsonDict["finalStates"] = self.finalVariables
    	else:
    		jsonDict["startState"] = self.finalVariables
    	
    		jsonDict["finalStates"] = self.startVariable
    	jsonDict["moves"] = self.convertprod()
    
    	
    	theJSON= json.dumps(jsonDict)
    	
    	self.theNFA =createNFA(theJSON)
    	#self.theNFA.__str__()
    	return self.theNFA

    def setToRightDir(self):
        self.isRight=False
    

    def convertprod(self):
    	moves =dict()
    	
    	for move in self.productions.moves:
    		if self.isRight:	
	    		moves[move.state()]=dict()
	    		moves[move.state()][move.inputSymbol()]=list(self.productions.getResults(move.state(),move.inputSymbol()))
	    	else:
	    		temp=self.productions.getResults(move.state(),move.inputSymbol()).pop()
	    		moves[temp]=dict()
	    		
	    		moves[temp][move.inputSymbol()]=move.state()
    	for move in self.productions.lambdaMoves:
    		if self.isRight:	
	    		moves[move.state()]=dict()
	    		moves[move.state()][constants.LAMBDA]=list(self.productions.getResults(move.state(),constants.LAMBDA))
	    	else:		
    			temp=self.productions.getResults(move.state(),constants.LAMBDA).pop()
	    		moves[temp]=dict()
	    		
	    		moves[temp][constants.LAMBDA]=move.state()
    	return moves    	
    	
    	
    	
    	
    	
    	
    	
    	
    	
    	
    	
    	
    	
