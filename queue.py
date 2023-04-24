
class Queue:
    def __init__(self) :
        self.items = []
        self.front_index = 0
    def enqueue(self, value) :
        self.items.append(value)
        print(self.items)
    def dequeue(self):
        if self.front_index == len(self.items) :
            print("Q is empty")
        else :
            result = self.items[self.front_index]
            self.front_index += 1
            return result
