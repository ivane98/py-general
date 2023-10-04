class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[len(self.items)-1]
    
    def size(self):
        return len(self.items)

word = 'art'

def rev_string(mystring):
    rev = ''
    s = Stack()
    for i in mystring:
        s.push(i)
    while s.is_empty() == False:
        rev = rev + s.pop()

    return rev

print(rev_string(word))
