#factory
class car:
    #constructor
    def __init__(self,color,rim_color,company):
        #properties
        self.color=color
        self.rim_color=rim_color
        self.company=company
    #method
    def intro(self):
        print("The color of the car is "+self.color)
        print("The color of the rim is "+self.rim_color)
        print("The brand of te car is "+self.company)
car1=car("jet black","black","bmw")
car2=car("black,blue","black","toyota")
car3=car("white","silver","mercedes")
car1.intro()
car2.intro()
car3.intro()