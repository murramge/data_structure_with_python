
class Stack :
    def __init__(self) :
        self.items = []
    def push(self, value) :
        self.items.append(value)
    def pop(self) :
        return self.items.pop()
    def top(self):
        return self.items[-1]
    def __len__(self):
        return len(self.items)