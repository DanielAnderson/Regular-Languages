'''Parses a string including parentheses'''
def parenthesesParser(string):
    print('ARGS: ' + string)
    parsed = __parenParser__(string)
    print('PARSED' + str(parsed))
    ans = []
    if len(parsed['left']) > 0:
        ans.append(parsed['left'])
    # print(parsed)
    if '(' in parsed['middle']:
        ans.append(parenthesesParser(parsed['middle']))
    else:
        ans.append([parsed['middle']])

    if '(' in parsed['remainder']:
        ans.append(parenthesesParser(parsed['remainder']))
    elif len(parsed['remainder']) > 0:
        ans.append(parsed['remainder'])

    print('ANSWER: ' + ans.__str__())
    if len(ans) == 1 and len(ans[0]) == 1:
        return ans[0]
    else:
        return ans

'''Given a string <x>(<y>)<z> returns {'left': <x>, 'middle': <y>, 'remainder': <z>}'''
def __parenParser__(string):
    # print('__parenParser__ ARGS: ' + string)
    ans = dict()
    ans['left'], leftLength = __leftOfParen__(string)
    ans['middle'], ans['remainder'] = __matchLeadingParen__(string[leftLength:])
    # print('__parenParser__ ANS: ' + str(ans))
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





    

# print(parenthesesParser('asdf(f(ds)a)'))
# print(parenthesesParser('f(ds)a'))
print(parenthesesParser('(c)'))