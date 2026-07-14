import pgzrun
import random


WIDTH = 800 
HEIGHT = 600 

class Balls: 
    def __init__(self):
        
        self.x = random.randint(50, 750)
        self.y = random.randint(50, 550)
        self.color = "blue"
        self.size = 30 
        
    def draw(self):
        screen.draw.filled_circle((self.x, self.y), self.size, self.color)


ball_list = []
for i in range(5):
    ball_list.append(Balls())

def draw():
    screen.clear()
    
    for ball in ball_list:
        ball.draw()

pgzrun.go()
