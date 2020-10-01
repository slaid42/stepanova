import pygame
import numpy as np

BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
pygame.init()
sc = pygame.display.set_mode([500, 500])

pygame.display.set_caption("Angry smile")

done = False
clock = pygame.time.Clock()

while not done:
    clock.tick(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    sc.fill(WHITE)
    '''

    pygame.draw.line(screen, BLUE, [0, 50], [100, 50], 15)
    pygame.draw.line(screen, BLUE, [400, 50], [400, 150], 5)

    pygame.draw.lines(screen, BLUE, False, [[270, 150], [270, 50], [320, 50], [320, 150]])

    pygame.draw.ellipse(screen, BLUE, [50, 70, 100, 60], 5)

'''
    #Лицо
    pygame.draw.circle(sc, YELLOW, (250, 250), 200)
    pygame.draw.circle(sc, BLACK, (250, 250), 201, 1)
    
    #Глаза
    pygame.draw.circle(sc, RED, (35*5, 35*5), 5*5)
    pygame.draw.circle(sc, BLACK, (35*5, 35*5), 5*5+1, 1)
    pygame.draw.circle(sc, BLACK, (35*5, 35*5), 2*5)
 
    pygame.draw.circle(sc, RED, (65*5, 35*5), 4*5)
    pygame.draw.circle(sc, BLACK, (65*5, 35*5), 4*5+1, 1)
    pygame.draw.circle(sc, BLACK, (65*5, 35*5), 2*5)

    #Рот
    pygame.draw.line(sc, BLACK, [35*5, 65*5], [65*5, 65*5], 25) 
    
    #Брови
    surface = pygame.Surface([40*5, 20*5], pygame.SRCALPHA)
    pygame.draw.line(surface, BLACK, [0,0], [38*5, 0], 20)
    surface_rot = pygame.transform.rotate(surface, 333)
    sc.blit(surface_rot, [2*5, 15*5])

    surface = pygame.Surface([40*5, 20*5], pygame.SRCALPHA)
    pygame.draw.line(surface, BLACK, [0,0], [35*5, 0], 18)
    surface_rot = pygame.transform.rotate(surface, 27)
    sc.blit(surface_rot, [56*5, 15*5])

    pygame.display.flip()


pygame.quit()


