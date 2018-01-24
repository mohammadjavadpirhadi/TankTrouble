import pygame, sys, random, math
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS
import pygame.time as GAME_TIME
import Objects

pygame.init()
world = Objects.world()
surface = pygame.display.set_mode((1280, 720), pygame.FULLSCREEN)
greenTankPictureDirectory = 'Tanks/greenTank.png'
greenTank = Objects.tank(30, 30, greenTankPictureDirectory)
candyTankPictureDirectory = 'Tanks/candyTank.png'
candyTank = Objects.tank(1175, 640, candyTankPictureDirectory)


def quitGame():
    pygame.quit()
    sys.exit()
    

while True:
    world.drawMap(surface)
    greenTank.drawTank(surface)
    candyTank.drawTank(surface)

    for event in GAME_EVENTS.get():

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:
                quitGame()

    if event.type == pygame.KEYUP:

        if event.type == GAME_GLOBALS.QUIT:
            quitGame()

    pygame.display.update()
