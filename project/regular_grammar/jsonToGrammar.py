import json
from project.regular_grammar.Grammar import Grammar
import project.regular_grammar.constants as constants


def createGrammar(theJSON):
    theJSON = json.loads(theJSON)
    #verifyGrammar(theJSON)
    variables = set(theJSON['Variables'])
    alphabet = set(theJSON['alphabet'])
    startVariable = theJSON['startVariable']
    print(variables)
    print(alphabet)
    print(startVariable)    
    theGrammar = Grammar(variables, alphabet, startVariable)
    addMovesFromJSON(theJSON, theGrammar)
    theGrammar.NFA()
    print(theGrammar.productions)
    return theGrammar

def addMovesFromJSON(theJSON, theGrammar):
	moves = theJSON['Productions']
	print(moves)
	for variable in moves:
		print (moves[variable])
		for inputSymbol in moves[variable]:
			if moves[variable] in theJSON['Variables']:
				print(moves[variable])
				#BEWARE: not as the same state as above
				for variables in move[variable]:
      	
					results = convertToList(moves[variable][variables])#returnsthe string
					print("here")
					if len(results) == 1:
						theGrammar.addMove(variable, results, variables)
					if len(result) >1:
						print("here")
						terminals(variable, results, variables,theJSON, theGrammar)
					if len(result) <1:
						theGrammar.addLambdaMove(variable, variables)
			else:
				print(inputSymbol) 
			
				#Converts string to an array including only that string
				#leaves arrays alone
				results = convertToList(moves[variable][inputSymbol])
				print(inputSymbol)	
				if len(inputSymbol) == 1:
					print("=")
					theGrammar.addMove(variable, inputSymbol, results)
				if len(inputSymbol) >1:
					print(">")
					terminals(variable,inputSymbol, results,theJSON, theGrammar)
				if len(inputSymbol) <1:
					print("<")
					theGrammar.addLambdaMove(variable, results)
                    
			
	print("done")
                   
def terminals(variable, inputSymbol, result, theJSON,theGrammar):
	#this deals with the case when there's multiple terminals by creating a new state
   #for each transition
   print("ttttttttttttttttttttttttttttttttttttttt")
   print(variable)
   string="temp"
   tempin=variable
   count=0
   for character in inputSymbol:
   	print(character)
   	count= count+1
   	if count==len(inputSymbol):
   		theGrammar.addMove(tempin,character,result)
   	else:
   		i=0;
   		tempout=str(i)
   		for tempout in theJSON["Variables"]:
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
	print("")
	print (theJSON['alphabet'])
	print (theJSON['Variables'])
	print  (moves)
	print  (len(moves))
	for variable in moves:
		print  (moves[variable])		
		assert variable in theJSON['Variables']
		
		if len(variable)==1:# checks if its multiple things or just one
			print  (moves[variable])		
			if moves[variable] in theJSON['alphabet']:#chack if that thing is in the alphabet
				print  (moves[variable])
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
	









