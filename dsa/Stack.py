 
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

class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data
    
    def getNext(self):
        return self.next
    
    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext


class StackWithList:
    def __init__(self):
        self.head = None

    def is_Empty(self):
        if self.head == None:
            return True
        else:
            return False
        
    def push(self, item):
        if self.head == None:
            self.head = Node(item)
        
        else:
            newnode = Node(item)
            newnode.next = self.head
            self.head = newnode

    def pop(self):
        if self.is_Empty():
            return None
        
        else:
            popnode = self.head
            self.head = self.head.next
            popnode.next = None
            return popnode.data
        
    
    def peek(self):
        if self.is_Empty():
            return None
        else:
            return self.head.data
        
    def size(self):
        count = 0
        current = self.head

        while current != None:
            current = current.next
            count = count + 1

        return count
    
s = StackWithList()
s.push(1)
s.push(2)
s.pop()
print(s.is_Empty())
print(s.size())

