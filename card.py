import pygame, time

pygame.init()

WIDTH = 600
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Birthday Card!!")

CYAN = (0, 255, 255)
NAVY = (0, 0, 128)

font = pygame.font.SysFont("Arial", 50)
screen.fill(NAVY)
pygame.display.update()
run = True
show=False
start_time=time.time()

baloon=pygame.image.load("baloons.png")
while run:
    for event in pygame.event.get():
         if event.type == pygame.QUIT:
            run = False
    # 2 sec
    if not show and time.time()-start_time>=2 and time.time()-start_time<5: 
        screen.fill(NAVY)
        text=font.render("this is muhammad",True,CYAN)
        text_rect=text.get_rect(center=(300,300))

        screen.blit(text,text_rect)
        pygame.display.update()
    #5 seconds
    if not show and time.time()-start_time>=5 and time.time()-start_time<10: 
            screen.fill(NAVY)
            font = pygame.font.SysFont("Arial", 30)
            text=font.render("Wishing u happy birthday",True,CYAN)
            text_rect=text.get_rect(center=(300,300))
    
            screen.blit(text,text_rect)
            pygame.display.update()
    if not show and time.time()-start_time>=10:
         screen.fill(NAVY)
         screen.blit(baloon,(-100,100))
         pygame.display.update()
pygame.QUIT()
