import json
from project.regular_grammar.Grammar import Grammar
import project.regular_grammar.constants as constants


def createGrammar(theJSON):
    theJSON = json.loads(theJSON)
    #verifyGrammar(theJSON)
    variables = set(theJSON['Variables'])
    alphabet = set(theJSON['alphabet'])
    startVariable = theJSON['startVariable']
      
    theGrammar = Grammar(variables, alphabet, startVariable)
    addMovesFromJSON(theJSON, theGrammar)
    
    theGrammar.NFA()
    return theGrammar

def addMovesFromJSON(theJSON, theGrammar):
	moves = theJSON['Productions']
	
	for variable in moves:
		
		for inputSymbol in moves[variable]:
			
			if inputSymbol in theJSON['Variables']:
				
				theGrammar.setToRightDir()
				
				#BEWARE: not as the same state as above
      	
				results = moves[variable][inputSymbol]#returnsthe string
					
				if len(results) == 1:
					
					theGrammar.addMove(variable, results, inputSymbol)
				if len(results) >1:
				
					terminals(variable, results, inputSymbol,theJSON, theGrammar)
				if len(results) <1:
					theGrammar.addLambdaMove(variable, inputSymbol)
						
			elif inputSymbol==constants.LAMBDA:
				results = moves[variable][inputSymbol]
				
				if 	results in theJSON['Variables']:
						theGrammar.addLambdaMove(variable, results)
						
				else:		
					if len(results) == 1:
						
						theGrammar.addMove(variable, results, [constants.LAMBDA])
					if len(results) >1:
				
						terminals(variable, results, constants.LAMBDA,theJSON, theGrammar)
						
						
			else:
				
			
				#Converts string to an array including only that string
				#leaves arrays alone
				results = convertToList(moves[variable][inputSymbol])
					
				if len(inputSymbol) == 1:
				
					theGrammar.addMove(variable, inputSymbol, results)
				if len(inputSymbol) >1:
				
					terminals(variable,inputSymbol, results,theJSON, theGrammar)
				if len(inputSymbol) <1:
					
					theGrammar.addLambdaMove(variable, results)
                    
			
	
                   
def terminals(variable, inputSymbol, result, theJSON,theGrammar):
	#this deals with the case when there's multiple terminals by creating a new state
  
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
	assert theJSON['startVariable'] in theJSON['Variables']
	assert 'lambda' not in theJSON['alphabet']
	moves = theJSON['Productions']
	
	for variable in moves:
				
		assert variable in theJSON['Variables']
		
		if len(variable)==1:# checks if its multiple things or just one
					
			if moves[variable] in theJSON['alphabet']:#chack if that thing is in the alphabet
				
				for alphabetMember in moves[variable]:

					assert alphabetMember in theJSON['alphabet'] or alphabetMember == constants.LAMBDA
					assert len (convertToList(moves[variable][alphabetMember])) ==1 
					assert moves[variable][alphabetMember]==constants.LAMBDA
					assert moves[variable][alphabetMember] in theJSON['Variables']
			elif moves[variable] in theJSON['Variables']  or  moves[variable]==constants.LAMBDA : #chack if that thing is in the Variables  if its a lambda move
				for VariablestMember in moves[variable]:
					assert VariablestMember in theJSON['Variables'] or VariablestMember==constants.LAMBDA
					for nextalphabet in convertToList(moves[variable][VariablestMember]):
						assert alphabetMember == constants.LAMBDA or variable in theJSON['alphabet']
			else:# if its neither 
				assert  moves[variable] in theJSON['alphabet'] or moves[variable] in theJSON['Variables']

		else:#the start of the grammer is multiple things long check if there all in alphabet 
			for alphabetMember in moves[variable]:
				for character in alphabetMember:
					assert character in theJSON['alphabet']        
	









