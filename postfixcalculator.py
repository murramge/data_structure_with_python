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
                try :
                    if S.top() == '*' :
                        output.append(S.top())
                        S.pop()
                        S.push(word)
                    else :
                        S.push(word)
                except IndexError :
                    S.push(word)
            elif word == '-':
                try :
                    if S.top() == '*' :
                        output.append(S.top())
                        S.pop()
                        S.push(word)
                    else :
                        S.push(word)
                except IndexError :
                    S.push(word)
            
        else :
            output.append(word)
    
    
    for stackword in range(len(S)) :
        output.append(S.pop())
    
    for filterbracket in output :
        if filterbracket == '(' :
            output.remove('(')
        elif filterbracket == ')' :
            output.remove(')')
    
    print(output)
 
    for token in output :
        if token in '+-/*' :
            a = S.pop()
            b = S.pop()
            if token == '+' :
                S.push(a+b)
            elif token == '-' :
                S.push(b-a)
            elif token == '/' :
                S.push(a/b)
            elif token == '*' :
                S.push(a*b)
        else :
            S.push(int(token))
    return S.top()


print(convertpostfix())