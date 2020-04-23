class A:
    def classA():
        print("i from ClassA")

class B:
    def classB():
        print("i am from ClassB")

class C(A,B):
    def classC():
        print("i am from ClassC")

obj = C
obj.classA()
obj.classB()
obj.classC()
