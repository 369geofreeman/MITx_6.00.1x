# Fraction Class


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

     def __str__(self):
         return str(self.num)+"/"+str(self.den)

     def show(self):
         print(self.num,"/",self.den)

     def __add__(self,otherfraction):
         newnum = self.num*otherfraction.den + \
                      self.den*otherfraction.num
         newden = self.den * otherfraction.den
         common = gcd(newnum,newden)
         return Fraction(newnum//common,newden//common)

     def __eq__(self, other):
         firstnum = self.num * other.den
         secondnum = other.num * self.den
         return firstnum == secondnum

     def __mul__(self, other):
        firstNum = self.num*other.num
        secondNum = self.den*other.den
        common = gcd(firstNum,secondNum)
        return Fraction(firstNum//common,secondNum//common)

     def __truediv__(self, other):
        firstNum = self.num*other.den
        secondNum = self.den*other.num
        common = gcd(firstNum,secondNum)
        return Fraction(firstNum//common,secondNum//common)

     def __sub__(self, other):
        firstNum = self.num *other.den - self.den*other.num
        secondNum = self.den*other.num
        common = gcd(firstNum,secondNum)
        return Fraction(firstNum//common,secondNum//common)

     def __gt__(self,other):
         firstnum = self.num / self.den
         secondnum = other.num / other.den
         return firstnum > secondnum

     def __it__(self,other):
         firstnum = self.num / self.den
         secondnum = other.num / other.den
         return firstnum < secondnum









x = Fraction(1,2)
y = Fraction(2,3)
print('Division: ', x/y)
print('Addition: ', x+y)
print('Multiplication: ', x*y)
print('Subtraction', x-y)
print('Equity: ', x==y)
print('Bigger than: ', x>y)
print('Smaller than: ', x<y)

