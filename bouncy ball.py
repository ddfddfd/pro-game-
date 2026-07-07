import pgzrun

WOIDTH=800
HIEGHT=600

#class is a blueprint of an object

class balls:
    #property-adjective
    def __init__(self):
        self.x=400
        self.y=300
        self.color="blue"
        self.size=30

    #method-verb
    def draw(self):
        screen.draw.filled_cirlcle((self.x,self.y),self.size,self.color)


b1=balls()#b1 is an object

def draw():
    screen.clear()
    b1.draw()


pgzrun.go()