class Bike():
    condition="new"
    def __init__(self,model,color,average):
        self.model=model
        self.color=color
        self.average=average

    def display_bike(self):
        print("This is a {} {} with {} average".format(self.color,self.model,self.average))




my_bike = Bike('Bullet','Red','New')
my_bike.display_bike()

