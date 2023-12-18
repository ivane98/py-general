
class C2:
    pass

class C3:
    pass

class C1(C2, C3):
    def __init__(self, name):
        self.name = name


I1 = C1('bob') # Sets I1.name to 'bob'
I2 = C1('mel') # Sets I2.name to 'mel'
print(I1.name) 