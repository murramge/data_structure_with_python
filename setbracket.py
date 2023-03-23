from stack import Stack

S = Stack()

brakets = input()

def handlebrakets() :
    for braket in brakets :
        if braket == '(' :
            S.push(braket)
        elif braket == ')' :
            try : 
                S.pop()
            except IndexError :
                return False
        else :
            return print("not allow")
    if len(S) > 0 :
        return False
    else :
        return True
    
    
print(handlebrakets())