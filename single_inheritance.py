#single Inheritance
class A:
    def printA(self):
        print("This was printed by class A")

class B(A):
    def printB(self):
        print("this was printed by class B")
    
b=B()
b.printA()
b.printB()
