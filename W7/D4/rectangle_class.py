class Rectangle():
    def __init__(self, angle1, angle2, angle3,angle4):
        self.angle1 =angle1
        self.angle2 =angle2
        self.angle3 = angle3
        self.angle4 = angle4

    number_of_sides=4
    def check_angles(self):
        if self.angle1+self.angle2+self.angle3+self.angle4==360:
            return True
        else:
            return False


class Square(Rectangle):
    angle=90
    def __init__(self):
        super().__init__(angle1=90,angle2=90,angle3=90,angle4=90)



obj1 = Rectangle(90,30,60,90)
print(obj1.check_angles())
obj2 = Square()
print(obj2.check_angles())






