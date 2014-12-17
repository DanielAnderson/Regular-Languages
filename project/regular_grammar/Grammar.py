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
    
        
        
        
#addes the move to production which is a moveFunction
    def addMove(self, initialVariable, inputSymbol, results):
    	
    	assert initialVariable in self.variables
    	for val in results:
    		
	    	if val == "lambda":
	    		
    			self.productions.addMove(initialVariable, inputSymbol, "F")
    		elif inputSymbol == "lambda":
    			self.productions.addLambdaMove(initialVariable, results)
    		else:
    			
    			self.productions.addMove(initialVariable, inputSymbol, results)
    	


#calles the NFA isinLanguage and gives them a string which returns a boolean
    def isInLanguage(self, string):
        return self.theNFA.isInLanguage(string)

    def __str__(self):
    	return "{\n\t" + "Variables: " + self.variables.__str__() + "\n\t" + "Σ: " + self.alphabet.__str__() + "\n\t" + "δ: " + self.productions.__str__() + "\n\t" + "S: " + self.startVariable.__str__() + "}"
    	
    	
#creates the NFA by creating a dict and adding everthing to it
    def NFA(self):
    	jsonDict = dict()
    	
    	
    	
    	 
    	jsonDict["states"] = list(self.variables)
    	jsonDict["alphabet"] = list(self.alphabet)
    	#checks to see if we need to reverse the language
    	# if we are we switch the final and start Variable
    	if self.isRight:
    		jsonDict["startState"] = self.startVariable
    	
    		jsonDict["finalStates"] = self.finalVariables
    	else:
    		jsonDict["startState"] = self.finalVariables
    	
    		jsonDict["finalStates"] = self.startVariable
    	jsonDict["moves"] = self.convertprod()
    
    	
    	theJSON= json.dumps(jsonDict)
    	#creates an NFA from our grammar for checking strings in the language
    	self.theNFA =createNFA(theJSON)
    	#self.theNFA.__str__()
    	return self.theNFA
	
	#changes the boolean isRight so we know if left or right linear meaning if we have to reverse the language
	#if we need to convert S -> Aa into A->aS  
    def setToRightDir(self):
        self.isRight=False
    
# takes moveFunction and converts it into a dict() to be added to a JSON
    def convertprod(self):
    	moves =dict()
    	
    	#goes and addes all the moves from productions to a dict 
    	for move in self.productions.moves:
    		if self.isRight:	
	    		moves[move.state()]=dict()
	    		moves[move.state()][move.inputSymbol()]=list(self.productions.getResults(move.state(),move.inputSymbol()))
	    	else:
	    	#if we are reversing the string we take the result and mae it out intial Variable
	    	#and swap it with out our previous initial Variable
	    		temp=self.productions.getResults(move.state(),move.inputSymbol()).pop()
	    		moves[temp]=dict()
	    		
	    		moves[temp][move.inputSymbol()]=move.state()
	    		
	#  goes and convert all the lambda moves in productions to a dict
    	for move in self.productions.lambdaMoves:
    		if self.isRight:	
	    		moves[move.state()]=dict()
	    		moves[move.state()][constants.LAMBDA]=list(self.productions.getResults(move.state(),constants.LAMBDA))
	    	else:
	    	#if we are reversing the string we take the result and mae it out intial Variable
	    	#and swap it with out our previous initial Variable		
    			temp=self.productions.getResults(move.state(),constants.LAMBDA).pop()
	    		moves[temp]=dict()
	    		
	    		moves[temp][constants.LAMBDA]=move.state()
    	return moves    	
    	
    	
    	
    	
    	
    	
    	
    	
    	
    	
    	
    	
    	
