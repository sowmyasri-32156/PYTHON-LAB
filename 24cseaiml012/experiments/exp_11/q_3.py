class father:
     def skill1(self):
          print("he is responsible")
class mother:
     def skill2(self):
          print("home maker")
class child(father, mother):
     def skill3(self):
          print("studying")
d1=child()
d1.skill1()
d1.skill2()
d1.skill3()