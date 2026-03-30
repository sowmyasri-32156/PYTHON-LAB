class Animal:
    def speak(self):
        print("animals speak")
class dog(Animal):
    def bark(self):
       print("dogs bark")        
d1=dog()
d1.bark()
d1.speak()