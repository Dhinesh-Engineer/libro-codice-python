# PROGRAM FOR STACK FUNCTION
#STACK MODULE

def getstack():
    '''create and return an empty stack'''
    return[]

def isempty(s):
    """ Return true if stack is empty ,else return false"""
    if s==[]:
        return True
    else:
        return False

def  top(s):
    ''' reTurn value of the top item of stack,
if stack is not empty otherwise return none'''
    if isempty(s):
        return None
    else:
        return s[len(s)-1]


def push(s,item):
    """ push an item at  the toop of the stack"""
    s.append(item)

def pop(s):
    ''' Return top of the stack if stack is not empty otherwise return none'''
    if isempty(s):
        return None
    else:
        item=s[len(s)-1]
        del s[len(s)-1]
        return (item)
    
    
