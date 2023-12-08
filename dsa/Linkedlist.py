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

class UnorderedList:
    def __init__(self):
        self.head = {'data': None, 'length': 0}
        
    def isEmpty(self):
        return self.head['data'] == None
    
    def __str__(self):
        ls = []
        current = self.head['data']
        while current.getNext() != None:
            ls.append([current.getData(), current.getNext().getData()])
            current = current.getNext()
        return str(ls)
    
    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head['data'])
        self.head['data'] = temp
        self.head['length'] = self.head['length'] + 1


    def size(self):
        return self.head['length']
    
    def search(self, item):
        current = self.head['data']
        found = False

        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found
    
    def remove(self, item):
        current = self.head['data']
        previous = None
        found = False

        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
                if current == None:
                    print('item is not in the list')
                    return
           
        if previous == None:
            self.head['data'] = current.getNext()
        else:
            previous.setNext(current.getNext())
        
        self.head['length'] = self.head['length']  - 1


    def append(self, item):
        current = self.head['data']
        previous = None
        temp = Node(item)

        while current != None:
            previous = current
            current = current.getNext()

        previous.setNext(temp)

    def index(self, item):
        current = self.head['data']
        found = False
        count = -1

        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
            count = count + 1

        return count
    
    def insert(self, item, idx):
        current = self.head['data']
        temp = Node(item)
        previous = None
        count = 0

        while count != idx:
            previous = current
            current = current.getNext()
            if current == None:
                print('item is not in the list')
                return
            count = count + 1

        
        previous.setNext(temp)
        temp.setNext(current)

        
        self.head['length'] = self.head['length']  + 1
        


l = UnorderedList()
l.add(1)
l.add(3)
l.add(4)
print(l.insert(2, 1))
print(l)
    
class OrderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None
    
    def size(self):
        current = self.head
        count = 0

        while current != None:
            count = count +1
            current = current.getNext()
        return count
    
    def remove(self, item):
        current = self.head
        previous = None
        found = False

        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def search(self, item):
        current = self.head
        found = False
        stop = False

        while current != None and not found and not stop:
            if current.getData() == item:
                found = True

            elif current.getData() > item:
                stop = True
            else:
                current = current.getNext()

        return found
    
    def add(self, item):
        temp = Node(item)
        current = self.head
        previous = None
        stop = False

        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)


    
        
    


        

