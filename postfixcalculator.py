from stack import Stack

S = Stack()

infix = input()

output = []

def convertpostfix() :
    for word in infix :
        if word == '(':
            S.push(word)
        if word == ')':
            while S.top() != '(' :
                output.append(S.top())
                S.pop()
             
        if word in '+-/*' :
            if word == '*' or word == '/' :
                S.push(word)
            elif word == '+':
                S.push(word)
            elif word == '-':
                S.push(word)
        else :
            output.append(word)
    
    
    for stackword in range(len(S)) :
        output.append(S.pop())
    
    for filterlist in output :
        if filterlist == '(' :
            output.remove('(')
        elif filterlist == ')' :
            output.remove(')')
        
    return output


print(convertpostfix())