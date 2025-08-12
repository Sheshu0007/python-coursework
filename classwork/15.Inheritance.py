#single inhertence
class a:
    def display_a(self):
        print("parent class")
class b(a):
    def display_b(self):
        print("child class")
A=a()# call int the child class
A.display_a()# call the function

B=b()# call int the child class
B.display_b()# call the function

B.display_a()# calling the parent method for the chaild call


#multiple inhertence
class p1:
    def display_p1(self):
        print("parent class p1")
class p2:
    def display_p2(self):
        print("parent class p2")
class p3:
    def display_p3(self):
        print("parent class p3")
class p4(p1,p2,p3):#                   # child call of p1,p2,p3  *(multiple parent and a single child)
    def display_p4(self):
        print("child  class of p1,p2,p3->p4")

P4=p4()
P4.display_p1()
P4.display_p2()
P4.display_p3()
P4.display_p4()

# multi level inheritance
class p1:
    def display_p1(self):
        print("parent class p1")
class p2(p1):
    def display_p2(self):
        print("parent class p2")
class p3(p2):
    def display_p3(self):
        print("parent class p3")
class p4(p3):#                  
    def display_p4(self):
        print("class p4")

P4=p4()  # it is a multilevel inhertence can
P4.display_p1()
P4.display_p2()
P4.display_p3()
P4.display_p4()




#hiracial inhertence
class p1: # it is a  hiracial inhertence the parent function can call by using all chaild class but we have to call all the child class 
    def display_p1(self):
        print("parent class p1")
class p2(p1):
    def display_p2(self):
        print("parent class p2")
class p3(p1):
    def display_p3(self):
        print("parent class p3")
class p4(p1):#                  
    def display_p4(self):
        print("class p4")

P4=p4()
P4.display_p1()
P3=p3()
P3.display_p1()
P2=p2()
P2.display_p1()

 

class status2015():
    def view(self):
        print("status view")
    def comment(self):
        print("comment")
    def caption(self):
        print("You can add caption")


class status2020(status2015):
    def uploading(self):
        print("uploadimage")
    def uploadvid(self):
        print("uploadvid")

class status2023(status2020):
    def reaction(self):
        print("reaction")
    def like(self):
        print("like")

class status2024(status2015):
    def statusrings(self):
        print("statusring")

class status2025(status2024,status2020):
    def music(self):
        print("You can add music")
    def mention(self):
        print("You can mention them")
    def collab(self):
        print("You can share your status from insta or fb")
    def voicenote(self):
        print("You can voice note")
sheshu=status2015()
sheshu.view()
sheshu.comment()
sheshu.caption()

supriya=status2020()
supriya.view()
supriya.comment()
supriya.caption()
supriya.uploading()
supriya.uploadvid()

teja=status2023()
teja.reaction()
teja.like()
teja.view()
teja.comment()
teja.caption()
teja.uploading()
teja.uploadvid()

shivani=status2024()
shivani.statusrings()
shivani.view()
shivani.comment()
shivani.caption()

shiva=status2025()
shiva.statusrings()
shiva.music()
shiva.mention()
shiva.view()
shiva.comment()
shiva.caption()
shiva.uploading()
shiva.uploadvid()