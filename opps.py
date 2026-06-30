#set up factory
class bottles():
#machine to builed
#called constructor
    def __init__(self,brand,color,shape):
        self.brand=brand
        self.color=color
        self.shape=shape
        self.size=1
#method
    def show_text(self):
        print(self.brand)
        print(self.color)
        print(self.shape)
        print(self.size)

fanta=bottles("fanta","orange","cylinder")
fanta.show_text()
cc=("coca-cola","black","cylinder")