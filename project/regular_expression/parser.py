from six import string_types

'''Parses a string including parentheses'''
def parenthesesParser(string):
    parsed = __parenParser__(string)
    ans = []
    if len(parsed['left']) > 0:
        ans.append(parsed['left'])
    if '(' in parsed['middle']:
        ans.append(parenthesesParser(parsed['middle']))
    else:
        ans.append([parsed['middle']])

    if '(' in parsed['remainder']:
        ans.append(parenthesesParser(parsed['remainder']))
    elif len(parsed['remainder']) > 0:
        ans.append(parsed['remainder'])

    if len(ans) == 1 and len(ans[0]) == 1:
        return ans[0]
    else:
        return ans

'''Given a string <x>(<y>)<z> returns {'left': <x>, 'middle': <y>, 'remainder': <z>}'''
def __parenParser__(string):
    ans = dict()
    ans['left'], leftLength = __leftOfParen__(string)
    ans['middle'], ans['remainder'] = __matchLeadingParen__(string[leftLength:])
    return ans

'''Given string <x>(<z>, returns (<x>, len(x))'''
def __leftOfParen__(string):
    index = string.index('(')
    return string[0:index], index

'''given a string in the form (<balanced parens>)<remainder>, returns (<balanced parens>, <remainder>)'''
def __matchLeadingParen__(string):
    count = 0
    assert string[0] == '('
    for index,character in enumerate(string):
        if character == '(':
            count += 1
        elif character == ')':
            count -=1

        if count == 0:
            return string[1:index], string[index + 1:]

        assert count >0
"""Takes a list which has already been parsed for parentheses, and binds each unary operator with its operand"""
def bindUnaryOperators(parenParsedString):
    unpackAt = []
    for index in range(len(parenParsedString)):
        if isinstance(parenParsedString[index], string_types):
            while len(parenParsedString[index]) > 0 and parenParsedString[index][0] in UnaryOperation.UNARY_OPERATORS: #Bind previous element to unary operator 
                parenParsedString[index-1] = UnaryOperation(parenParsedString[index-1], parenParsedString[index][0])
                parenParsedString[index] = parenParsedString[index][1:] #Get rid of the leading unary operator
            parenParsedString[index] = bindUnaryInString(parenParsedString[index])
        else: #it is a list
            parenParsedString[index] = bindUnaryOperators(parenParsedString[index])
            unpackAt.append(index -1) #it will be a list, we need to  unpack the list, but not until we finish this operation, so that the iteration isn't messed up
    unpacked = unpack(parenParsedString, unpackAt)
    # print(parenParsedString)
    # print(unpackAt)
    return parenParsedString

"""Takes a list: [a, b, c, [d, e], [f, g]] and which elements to unpack [3] and returns : [a, b, c, d, e, [f, g]]
Note, the list of elements to unpack must be in order"""
def unpack(theList, whereToUnpack):
    print(theList, whereToUnpack)
    originalLength = len(whereToUnpack)
    diff = 0 
    for index, element in enumerate(theList):
        if index + diff >= len(theList):
            return theList
        if index - diff in whereToUnpack:
            print(index + diff)
            originalItem = theList[index + diff]
            del(theList[index + diff])
            for thingToAdd in originalItem:
                theList.insert(index + diff, thingToAdd)
                diff += 1
            diff -= 1 #We should add one for every element in the list, then subtract one because we removed the list itself
    return theList

"""Takes a string, and returns a list with each unary operator bound appropriately.
   The initial string must not start with a unary operator"""
def bindUnaryInString(string):
    answer = []
    for character in string:
        if character in UnaryOperation.UNARY_OPERATORS:
            answer[-1] = UnaryOperation(answer[-1], character)
        else:
            answer.append(character)
    return mergeStrings(answer)

"""Takes a list of strings and objects. For each sequence of strings, merges that sequence into the concatenation of each string
IE ['a','b','c', <object>, 'd','e'] -> ['abc', <object>, 'de']"""
def mergeStrings(theList):
    answer = []
    for element in theList:
        if len(answer) == 0: #if answer is empty, add the first element to it 
            answer.append(element)
        elif not isinstance(answer[-1], string_types): #if the last element of answer is not a string, then append the next element to answer
            answer.append(element)
        else: #the last element of answer is a string
            if isinstance(element, string_types):
                answer[-1] = answer[-1] + element
            else:
                answer.append(element)

    return answer



"""Represents a unary operation on something that is a valid regular expression"""
class UnaryOperation:
    UNARY_OPERATORS = {'?', '+', '*'}
    def __init__(self, operand, operator):
        assert operator in UnaryOperation.UNARY_OPERATORS
        self.operand = operand
        self.operator = operator
        if len(operand) == 1 :
            operand = operand[0]

    def __eq__(self,other):
        return self.operand == other.operand and self.operator == other.operator

    def __repr__(self):
        return "{UnaryOperation: {operator: " + self.operator + " operand: " + self.operand.__repr__() + "}}"


unpack(['a','b','c', ['a',['b'], 'c'], ['a'], ['x', 'y']], [3, 5])

parenParsed = parenthesesParser("ab|aab|(a | b(a | b)*)?")
print(parenParsed)
foo = bindUnaryOperators(parenParsed)
print(foo)
