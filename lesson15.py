class A:
    def action(self):
        print ("Action from A")

class B(A):
    pass

class C(A):
    def action(self):
        print("Action from C")

class D (B,C):
    pass

dog=D()
dog.action()
print(D.__mro__)