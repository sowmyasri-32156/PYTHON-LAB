class grandparent:
    def old(self):
        print("free from all the responsibilities")
class parent(grandparent):
    def business(self):
        print("handles business")
class child(parent):
    def education(self):
        print("ongoing with his education")
d1=child()
d1.old()
d1.business()
d1.education()                        