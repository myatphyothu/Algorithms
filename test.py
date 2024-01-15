class BaseClass(object):
    def __init__(self):
        self.__method()

    def __method (self):
        print("Base CLass method")

class ChildClass(BaseClass):
    def __init__(self):
        super(ChildClass,self).__init__()
    
    def _BaseClass__method(self):
        print("Child Class method")


bClass = BaseClass()
cClass = ChildClass()