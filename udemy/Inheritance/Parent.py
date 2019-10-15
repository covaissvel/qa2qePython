class Parent:
    counter = 10

    def __init__(self):
        print("Class initialized")

    def parentFunc(self):
        print("ParentFunc being called")

    def setCounter(self,num):
        Parent.counter = num;

    def showCounter(self):
        print(Parent.counter)

        