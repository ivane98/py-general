def gcd(m,n):
        while m%n != 0:
            oldm = m
            oldn = n

            m = oldn
            n = oldm%oldn
        return n

class Fraction:
    def __init__(self,top,bottom):
        self.num = top
        self.den = bottom

        if type(self.num) == int and type(self.den) == int:
            common = gcd(self.num, self.den)
            self.num = top//common
            self.den = bottom//common
        else:
            raise Exception('both num and den must be ints')

    def __str__(self):
        return str(self.num)+"/"+str(self.den)

    
    def show(self):
        print(self.num,"/",self.den)
    
    
    def __add__(self, otherfraction):
        newnum = self.num*otherfraction.den + self.den*otherfraction.num
        newden = self.den * otherfraction.den

        return Fraction(newnum, newden)
    
    def __iadd__(self, otherfraction):
        self.num = self.num*otherfraction.den + self.den*otherfraction.num
        self.den = self.den * otherfraction.den

        return Fraction(self.num, self.den)
    

    def __radd__(self, otherfraction):
        newnum = otherfraction.num*self.den + otherfraction.den*self.num
        newden = otherfraction.den * self.den

        return Fraction(newnum, newden)
        
    
    def __sub__(self, otherfraction):
        newnum = self.num*otherfraction.den - self.den*otherfraction.num
        newden = self.den * otherfraction.den
        
        return Fraction(newnum,newden)
    
    def __mul__(self, other):
        newnum = self.num * other.num
        newden = self.den * other.den

        return Fraction(newnum, newden)
    
    def __truediv__(self, other):
        newnum = self.num * other.den
        newden = self.den * other.num

        return Fraction(newnum, newden)
    
    def __eq__(self, other):
        firstnum = self.num*other.den
        secondnum = self.den*other.num

        return firstnum == secondnum
    
    def __ne__(self, other):
        firstnum = self.num*other.den
        secondnum = self.den*other.num

        return firstnum != secondnum
    
    def __gt__(self, other):
        firstnum = self.num/self.den
        secondnum = other.num/other.den

        return firstnum > secondnum
    
    def __ge__(self, other):
        firstnum = self.num/self.den
        secondnum = other.num/other.den

        return firstnum >= secondnum
    
    def __lt__(self, other):
        firstnum = self.num/self.den
        secondnum = other.num/other.den

        return firstnum < secondnum
    
    def __le__(self, other):
        firstnum = self.num/self.den
        secondnum = other.num/other.den

        return firstnum <= secondnum
    

    

f1=Fraction(1, 2)
f2=Fraction(3, 4)

print(repr(f1))




