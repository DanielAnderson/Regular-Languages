import json



def createGrammar(theJSON):
    theJSON = json.loads(theJSON)
    verifyGrammar(theJSON)
    variables = set(theJSON['variables'])
    alphabet = set(theJSON['alphabet'])
    startVariable = theJSON['startVariable']
    theGrammar = Grammar(variables, alphabet, startVariable, finalVariables)
    addMovesFromJSON(theJSON, theGrammar)
    temp = 0
    return theGrammar

def addMovesFromJSON(theJSON, theGrammar):
	moves = theJSON['Productions']

	for variable in moves:
		if moves[variable] in theJSON["alphabet"]: 
			for inputSymbol in moves[variable]:
				#Converts string to an array including only that string
				#leaves arrays alone
  				results = convertToList(moves[variable][inputSymbol])	
  				if len(inputSymbol) == 1:
  					theGrammar.addMove(variable, inputSymbol, results)
  				if len(inputSymbol) >1:
  					terminals(variable,inputSymbol, results)
  				if len(inputSymbol) <1:
  					theGrammar.addLambdaMove(variable, results)
                    
		if moves[variable] in theJSON['variables']:
			#BEWARE: not as the same state as above
			for variables in move[variable]:
      	
				results = convertToList(moves[variable][variables])#returnsthe string
				if len(results) == 1:
					theGrammar.addMove(variable, results, variables)
				if len(result) >1:
					terminals(variable, results, variables)
				if len(result) <1:
					theGrammar.addLambdaMove(variable, variables)
                   
def terminals(inputSymbol, variable, result, theJSON,theGrammar):
	#this deals with the case when there's multiple terminals by creating a new state
   #for each transition
   string="temp"
   tempin=variable
   count=0
   for character in inputSymbol:
   	
   	count= count+1
   	if count==len(inputSymbol):
   		theGrammar.addMove(tempin,character,result)
   	else:
   		i=0;
   		tempout=string + i
   		for tempout in theJSON["variables"]:
   			i=i+1
   			tempout=string+ i
   		theGrammar.addMove(tempin,character,tempout)
   		tempin=tempout
        

def convertToList(stringOrList):
	if type(stringOrList) is list:
		return stringOrList
	else:
		return [stringOrList]

def verifyGrammar(theJSON):
	assert theJSON['startVariable'] in theJSON['variables']
	assert 'lambda' not in theJSON['alphabet']
	moves = theJSON['moves']
	for variable in moves:
		assert variable in theJSON['variables'] 
		for alphabetMember in moves[variable]:
			assert alphabetMember in theJSON['alphabet'] or alphabetMember == constants.LAMBDA or variable in theJSON['alphabet']
			for nextVariable in convertToList(moves[variable][alphabetMember]):
				assert nextVariable in theJSON['variables'] or alphabetMember == constants.LAMBDA or variable in theJSON['alphabet']







