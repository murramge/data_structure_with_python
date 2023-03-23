class Stack:
    def __init__(self):
      self.items = []
      
    def push(self, val):
        self.items.append(val)
        
    def pop(self):
        
            return self.items.pop()
            
    def top(self):
        try:
            return self.items[-1]
        except IndexError:
            print("Stack is null")
    
    def __len__(self):
        return len(self.items)
    
    
    