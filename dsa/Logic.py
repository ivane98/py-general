class LogicGate:

    def __init__(self,n):
        self.name = n
        self.output = None

    def getLabel(self):
        return self.name

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output


class BinaryGate(LogicGate):

    def __init__(self,n):
        super(BinaryGate, self).__init__(n)

        self.pinA = None
        self.pinB = None

    def getPinA(self):
        if self.pinA == None:
            return int(input("Enter Pin A input for gate "+self.getLabel()+"-->"))
        else:
            return self.pinA.getFrom().getOutput()

    def getPinB(self):
        if self.pinB == None:
            return int(input("Enter Pin B input for gate "+self.getLabel()+"-->"))
        else:
            return self.pinB.getFrom().getOutput()

    def setNextPin(self,source):
        if self.pinA == None:
            self.pinA = source
        else:
            if self.pinB == None:
                self.pinB = source
            else:
                print("Cannot Connect: NO EMPTY PINS on this gate")


class AndGate(BinaryGate):

    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a==1 and b==1:
            return 1
        else:
            return 0

class OrGate(BinaryGate):

    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a ==1 or b==1:
            return 1
        else:
            return 0

class UnaryGate(LogicGate):

    def __init__(self,n):
        LogicGate.__init__(self,n)

        self.pin = None

    def getPin(self):
        if self.pin == None:
            return int(input("Enter Pin input for gate "+self.getLabel()+"-->"))
        else:
            return self.pin.getFrom().getOutput()

    def setNextPin(self,source):
        if self.pin == None:
            self.pin = source
        else:
            print("Cannot Connect: NO EMPTY PINS on this gate")


class NotGate(UnaryGate):

    def __init__(self,n):
        UnaryGate.__init__(self,n)

    def performGateLogic(self):
        if self.getPin():
            return 0
        else:
            return 1
        
class Nandgate(BinaryGate):

    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a==1 and b==1:
            return 0
        else:
            return 1
        
class Norgate(BinaryGate):

    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a ==1 or b==1:
            return 0
        else:
            return 1
        
class Xorgate(BinaryGate):
    def __init__(self,n):
        BinaryGate.__init__(self,n)
    
    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()

        if a==b:
            return 0
        else:
            return 1

class HalfAdder(BinaryGate):
    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()

        if a ==1 and b==1:
            SUM = 0
        elif (a ==0 and b==1) or (a==1 and b==0):
            SUM = 1
        else:
            SUM = 0

        if a==1 and b==1:
            CARRY = 1
        else:
            CARRY = 0

        return SUM, CARRY 
        

class FullAdder(BinaryGate):
    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def getC(self):
        return int(input('C-IN: '))

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()

        c = self.getC()

        if a==0 and b==0 and c==0:
            SUM = 0
            Cout = 0
        elif a==0 and b==0 and c==1:
            SUM = 1
            Cout = 0
        elif a==0 and b==1 and c==0:
            SUM = 1
            Cout = 0
        elif a==0 and b==1 and c==1:
            SUM = 0
            Cout = 1
        elif a==1 and b==0 and c==0:
            SUM = 1
            Count = 0
        elif a==1 and b==0 and c==1:
            SUM = 0
            Cout = 1
        elif a==1 and b==1 and c==0:
            SUM = 0
            Cout = 1
        elif a==1 and b==1 and c==1:
            SUM = 1
            Cout = 1

        return SUM, Cout   

class Connector:

    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate

        tgate.setNextPin(self)

    def getFrom(self):
        return self.fromgate

    def getTo(self):
        return self.togate


def main():
   g1 = FullAdder("G1")
#    g2 = Xorgate('g2')
#    g2 = AndGate("G2")
#    g3 = OrGate("G3")
#    g4 = NotGate("G4")
#    c1 = Connector(g1,g3)
#    c2 = Connector(g2,g3)
#    c3 = Connector(g3,g4)
   print(g1.getOutput())

main()
