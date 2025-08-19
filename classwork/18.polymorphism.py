#method over ridding

class Normaluser:
    def __init__(self,username):
        self.username=username
        print(f"welcome to the")
    def playvedio(self):
        print("ads are includes ")
        print("no background play ")
        print("no high quality download ")
    def likes(self):
        print("likes")
    def comment(self):
        print("comment")
    def subscribe(self):
        print("subscribe")
class premi(Normaluser):
    def __init__(self,username):
        super().__init__(username)
    def playvedio(self):
        print(" no ads are includes ")
        print("background play ")
        print(" high quality download ")

sheshu=Normaluser("sheshu")
sheshu.playvedio()
sheshu.comment()
sheshu.likes()
sheshu.subscribe()

supriya=premi("supriya")
supriya.playvedio()



#method over loading
class numbers:
    def __init__(self,N1):
        self.N1=N1
    def __add__(self,other):
        return self.N1 + other.N1
    def __sub__(self,other):
        return self.N1 + other.N1
    def __mul__(self,other):
        return self.N1 * other.N1
    def __eq__(self,other):
        return self.N1 == other.N1
    def __gt__(self,other):
        return self.N1 < other.N1
    
