'''
pygame intro
'''
import pygame
import sys
import math
import random

pygame.init()
screen = pygame.display.set_mode((1280,720))

circle_pos = (1280/2, 720/2)

font = pygame.font.Font(None, 30)

score = 0

def checkCircleCollision() -> bool:
    mouse_pos = pygame.mouse.get_pos()
    if math.sqrt(((mouse_pos[0] - circle_pos[0])**2) + ((mouse_pos[1] - circle_pos[1])**2)) <= 50:
        return True
    return False

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if checkCircleCollision():
                    circle_pos = (random.randint(50,1230), random.randint(50,670))
                    score += 1
                else:
                    score -= 1

    scoreObj = font.render(f'Score: {score}', True, 'black')


    screen.fill('lightblue')
    pygame.draw.circle(screen, "red", circle_pos, 50)
    screen.blit(scoreObj, (50,50))

    pygame.display.update()
