class Calsi:
    def add(n1,n2):
        return n1+n2
    def sub(n1,n2):
        return n1-n2

class Math:
    def power(bval,exval):
        return bval**exval
    def isEven(val):
        if val%2==0:
            return True
        return False

def isOdd(val):
    if val%2!=0:
        return True
    return False

class Calsi1:
    def __init__(self,val1,val2):
        self.val1=val1
        self.val2=val2
    def __add__(self):
        return self.val1 + self.val2
    def __mul__(self):
        return self.val1 * self.val2


    



    
        
        




