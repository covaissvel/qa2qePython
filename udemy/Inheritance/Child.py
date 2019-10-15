from udemy.Inheritance.Parent import Parent


class Child(Parent):
    def __init__(self):
        print("Child class being initialized")

    def childFunc(self):
        print("Child func being called")


c = Child()
c.childFunc()
c.parentFunc()
c.showCounter()