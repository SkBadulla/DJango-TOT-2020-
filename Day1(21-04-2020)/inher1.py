class ClassA():
    def display():
        print("i am from ClassA")

    def sub(a,b):
        return a+b

class ClassB(ClassA):
    c,d=23,34
    def show():
        print('i am from ClassA')

    def add(a,b,c):
        return a+b+c

obj = ClassB
print(obj.show())
#print(obj.sub(2,3))
#print(obj.b)
#obj.show()
#obj.display()
              

              

        
