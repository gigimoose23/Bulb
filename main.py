import pygame
import time


pygame.init()


WIDTH = 500
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))


screen.fill((255, 255, 255))  # white


bulboff = pygame.image.load("images/bulboff.png")
bulbon = pygame.image.load("images/bulbon.png")


running = True
while running:

    event = pygame.event.poll()

    if event.type == pygame.QUIT:
        running = False

   
    if event.type == pygame.MOUSEBUTTONDOWN:
        
        screen.fill((255, 255, 255))  # white

        screen.blit(bulboff, (0, 0))  
        pygame.display.update()
    if event.type == pygame.MOUSEBUTTONUP:
        screen.fill((255, 255, 255))  # white
    
        screen.blit(bulbon, (0, 0))  
        pygame.display.update()


    pygame.display.update()


pygame.quit()
