import random
from pythonds.basic.queue import Queue

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

# class Queue:
#     def __init__(self):
#         self.items = []

#     def isEmpty(self):
#         return self.items == []

#     def enqueue(self, item):
#         self.items.insert(0,item)

#     def dequeue(self):
#         return self.items.pop()

#     def size(self):
#         return len(self.items)



class QueueWithList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False
        
    def enqueue(self, item):
        if self.head == None:
            self.head = Node(item)
        
        else:
            newnode = Node(item)
            newnode.next = self.head
            self.head = newnode

    def dequeue(self):
        if self.isEmpty():
            return None
        else:
            temp = self.head
            self.head = temp.next

    def size(self):
        count = 0
        current = self.head

        while current != None:
            current = current.next
            count = count + 1

        return count
    

q = QueueWithList()

q.enqueue(1)
q.enqueue(2)
q.dequeue()

print(q.isEmpty())
print(q.size())



















class Printer:
    def __init__(self, ppm):
        self.pagerate = ppm
        self.currentTask = None
        self.timeRemaining = 0

    def tick(self):
        if self.currentTask != None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0:
                self.currentTask = None

    def busy(self):
        if self.currentTask != None:
            return True
        else:
            return False
        

    def startNext(self, nextTask):
        self.currentTask = nextTask
        self.timeRemaining = nextTask.getPages() * 60/self.pagerate


class Task:
    def __init__(self, time):
        self.timestamp = time
        self.pages = random.randrange(1, 41)

    def getStamp(self):
        return self.timestamp
    
    def getPages(self):
        return self.pages
    
    def waitTime(self, currenttime):
        return currenttime - self.timestamp


def newPrinttask():
    num = random.randrange(1, 91)

    if num == 90:
        return True
    else:
        return False
    
def simulation(numSeconds, pagesPerMinute):
    labPrinter = Printer(pagesPerMinute)
    printQueue = Queue()
    waitingTimes = []

    for currentSecond in range(numSeconds):
        if newPrinttask():
            task = Task(currentSecond)
            printQueue.enqueue(task)

        if (not labPrinter.busy()) and (not printQueue.isEmpty()):
            nextTask = printQueue.dequeue()
            waitingTimes.append(nextTask.waitTime(currentSecond))
            labPrinter.startNext(nextTask)

        labPrinter.tick()

    averageWait = sum(waitingTimes)/len(waitingTimes)
    print("Average Wait %6.2f secs %3d tasks remaining."%(averageWait,printQueue.size()))


# for i in range(10):
#     simulation(3600, 10)