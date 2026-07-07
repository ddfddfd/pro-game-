import pygame
pygame.init()

screen= pygame.display.set_mode((600,600))

CYAN=(0,255,255)# rgb code
RED=(255,0,0)


class Rect:
    def __init__(self,color,dims):
        self.color=color
        self.dims=dims
    def draw(self):
        pygame.draw.rect(screen,self.color,self.dims)


R1=Rect(RED,(50,20,100,100))
R2=Rect(RED,(150,200,50,100))



running=True
while running:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            running =False

    screen.fill(CYAN)
    R1.draw()
    R2.draw()
    pygame.display.update()



pygame.quit()