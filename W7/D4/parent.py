class Parent:
    def __init__(self,fname, lname, age):
        self.fname=fname
        self.lname=lname
        self.age=age
    def display(self):
        print(self.fname+self.lname+self.age)
    def delta(self,newname):
        self.lname=newname
        print("last name changed")



