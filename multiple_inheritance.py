#multiple inheritance
class A:
   def printA(self):
        print("This was printed by class A")

class B:
    def printB(self):
        print("this was printed by class B")

class C(A,B):
    def printC(self):
        print("this was printed by class C")

c=C()
c.printA()
c.printB()
c.printC()
