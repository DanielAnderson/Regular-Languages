import json
from project.regular_grammar.Grammar import Grammar
import project.regular_grammar.constants as constants

#this is the method that should be called when converting a json to a grammar
def createGrammar(theJSON):
    theJSON = json.loads(theJSON)
    verifyGrammar(theJSON)
    variables = set(theJSON['Variables'])
    alphabet = set(theJSON['alphabet'])
    startVariable = theJSON['startVariable']
      
    theGrammar = Grammar(variables, alphabet, startVariable)
    addMovesFromJSON(theJSON, theGrammar)
    
    theGrammar.NFA()
    return theGrammar
#this goes through the productions in theJSON and addes them to the Grammar 

def addMovesFromJSON(theJSON, theGrammar):
	moves = theJSON['Productions']
	
	for variable in moves:
		
		for inputSymbol in moves[variable]:
			
			if inputSymbol in theJSON['Variables']:
				
				theGrammar.setToRightDir()
# if the first symbol is in Variables then we know that the language is right linear so we tell the grammar that
#the result of moves[variable][inputSymbol] should be a set of some terminals
#if its just one then we know to addMove 
#if its less then one then it must be a lambda move (which shouldnt happen)
#if its more then one then we call terminal and have it add it to theGrammar
      	
				results = moves[variable][inputSymbol]
					
				if len(results) == 1:
					
					theGrammar.addMove(variable, results, inputSymbol)
				if len(results) >1:
				
					terminals(variable, results, inputSymbol,theJSON, theGrammar)
				if len(results) <1:
					theGrammar.addLambdaMove(variable, inputSymbol)
						
			elif inputSymbol==constants.LAMBDA:
				results = moves[variable][inputSymbol]
#in this case the input symbol is lambda which we dont know if that means its for alphabet or variable then we must check its result to see what that lambda represents 
#like if the result is in Variables then the lambda represents a null alphabet
# or if the result is in alphabet then we know the lambda is a Variable to move to 
				
				if 	results in theJSON['Variables']:
						theGrammar.addLambdaMove(variable, results)
						
				else:		
					if len(results) == 1:
						
						theGrammar.addMove(variable, results, [constants.LAMBDA])
					if len(results) >1:
				
						terminals(variable, results, constants.LAMBDA,theJSON, theGrammar)
						
						
			else:
# if the first symbol is in alphabet then we know that the language is left linear 
#the result of moves[variable][inputSymbol] should be a Variable
#if the first symbol just one then we know to addMove 
#if the first symbol less then one then it must be a lambda move (which shouldnt happen)
#if the first symbol more then one then we call terminal and have it add it to theGrammar				
			
				
				results = convertToList(moves[variable][inputSymbol])
					
				if len(inputSymbol) == 1:
				
					theGrammar.addMove(variable, inputSymbol, results)
				if len(inputSymbol) >1:
				
					terminals(variable,inputSymbol, results,theJSON, theGrammar)
				if len(inputSymbol) <1:
					
					theGrammar.addLambdaMove(variable, results)
                    
			
	
                   
def terminals(variable, inputSymbol, result, theJSON,theGrammar):
#this deals with the case when there's multiple terminals by creating a new state for each terminal and haveing each character have an idvidual move
  
   tempin=variable
   count=0
   for character in inputSymbol:
   	
   	
   	count= count+1 
   	if count==len(inputSymbol):
   		theGrammar.addMove(tempin,character,result)
   	
   	else:
   		i=0;
   		tempout=str(i)
   		
   		for tempout in theGrammar.variables:
   			i=i+1
   			tempout=str(i)
   		
   		theGrammar.variables.add(tempout)
   		theGrammar.addMove(tempin,character,tempout)
   		tempin=tempout
   	 

def convertToList(stringOrList):
	if type(stringOrList) is list:
		return stringOrList
	else:
		return [stringOrList]

def verifyGrammar(theJSON):
#verifies that the json of the grammar is a possible json
	assert theJSON['startVariable'] in theJSON['Variables']
	assert 'lambda' not in theJSON['alphabet']
	moves = theJSON['Productions']
	for variable in moves:			
		assert variable in theJSON['Variables']     
	









