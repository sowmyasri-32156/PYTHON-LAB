class parent:
    def show(self):
        print("parent class")
class child(parent):
    def show(self):
        print("child class")   
d1=child()
d1.show()
             