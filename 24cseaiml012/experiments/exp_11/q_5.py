class parent:
    def __init__(self):
        print("parent constructor")
class child(parent):
    def __init__(self):
        super().__init__() 
        print("child constructor")
c=child()
               
