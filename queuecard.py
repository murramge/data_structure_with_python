from queue import Queue

Q = Queue()

numbers = input()

numbers = int(numbers)+1

def cardselect() :
    for number in range(1,int(numbers)):
        Q.enqueue(number)
    x = Q.dequeue()
    Q.enqueue(x)
    
    
    
print(cardselect())