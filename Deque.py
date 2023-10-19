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

class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []
    
    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0, item)

    def removeFront(self):
        return self.items.pop()
    
    def removeRear(self):
        return self.items.pop(0)
    
    def size(self):
        return len(self.items)
    

class DequeWithList:
    def __init__(self):
        self.head = None
    
    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False
    
    def addFront(self, item):
        if self.head == None:
            self.head = Node(item)
        
        current = self.head
        previous = None
        temp = Node(item)

        while current != None:
            previous = current
            current = current.getNext()

        previous.setNext(temp)

    def addRear(self, item):
        if self.head == None:
            self.head = Node(item)
        else:
            newnode = Node(item)
            newnode.next = self.head
            self.head = newnode

    def removeFront(self):
            










    
def palindrome(s):
    d = Deque()

    for i in s:
        d.addRear(i)

    stillEqual = True

    while d.size() > 1 and stillEqual:
        first = d.removeFront()
        last = d.removeRear()

        if first != last:
            stillEqual = False

    return stillEqual

# print(palindrome("lsdkjfskf"))
# print(palindrome("radar"))