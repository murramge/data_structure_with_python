from collections import deque

numbers = input()
rotation = input()


numbers = int(numbers)+1
rotation = int(rotation)


def joseqhus(number,rotation):
    numberlist = []

    for number in range(1,int(numbers)):
        numberlist.append(number)

    deq = deque(numberlist)

    while len(deq)>1:
        deq.rotate(-rotation+1)
        deq.popleft()
    return deq.popleft()
        
            
                
print(joseqhus(numbers,rotation))