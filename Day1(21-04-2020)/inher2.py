class A():
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def display(self):
        print(" i am from Class A")

class B(A):
    def __init__(self,a,b,c):
        self.c=c
        super().__init__(a,b)
        #super.display()

    def show(self):
        print(self.c)

obj = B(5,6,7)
obj.show()

        
