import math
import pygame
import pygame.event as GAME_EVENTS
import pygame.locals as GAME_GLOBALS
import pygame.time as GAME_TIME
import random
import sys

import Objects

pygame.init()
world = Objects.world()
surface = pygame.display.set_mode((1280, 720), pygame.FULLSCREEN)
greenTankPictureDirectory = 'Tanks/greenTank3.png'
greenTank = Objects.tank(50, 50, greenTankPictureDirectory)
purpleTankPictureDirectory = 'Tanks/purpleTank.png'
purpleTank = Objects.tank(1230, 670, purpleTankPictureDirectory)


def quitGame():
    pygame.quit()
    sys.exit()


while True:
    for event in GAME_EVENTS.get():

        if event.type == pygame.KEYDOWN:
            # greenTank
            if event.key == pygame.K_UP:
                greenTank.forwardDirection = True
                greenTank.backwardDirection = False
            if event.key == pygame.K_DOWN:
                greenTank.forwardDirection = False
                greenTank.backwardDirection = True
            if event.key == pygame.K_LEFT:
                greenTank.leftRotate = True
                greenTank.rightRotate = False
            if event.key == pygame.K_RIGHT:
                greenTank.leftRotate = False
                greenTank.rightRotate = True
            if event.key == pygame.K_RCTRL:
                greenTank.fire()
            # purpleTank
            if event.key == pygame.K_e:
                purpleTank.forwardDirection = True
                purpleTank.backwardDirection = False
            if event.key == pygame.K_d:
                purpleTank.forwardDirection = False
                purpleTank.backwardDirection = True
            if event.key == pygame.K_s:
                purpleTank.leftRotate = True
                purpleTank.rightRotate = False
            if event.key == pygame.K_f:
                purpleTank.leftRotate = False
                purpleTank.rightRotate = True
            if event.key == pygame.K_a:
                purpleTank.fire()
            if event.key == pygame.K_ESCAPE:
                quitGame()

    if event.type == pygame.KEYUP:
        # greenTank
        if event.key == pygame.K_UP:
            greenTank.forwardDirection = False
        if event.key == pygame.K_DOWN:
            greenTank.backwardDirection = False
        if event.key == pygame.K_LEFT:
            greenTank.leftRotate = False
        if event.key == pygame.K_RIGHT:
            greenTank.rightRotate = False
        # purpleTank
        if event.key == pygame.K_e:
            purpleTank.forwardDirection = False
        if event.key == pygame.K_d:
            purpleTank.backwardDirection = False
        if event.key == pygame.K_s:
            purpleTank.leftRotate = False
        if event.key == pygame.K_f:
            purpleTank.rightRotate = False
        if event.type == GAME_GLOBALS.QUIT:
            quitGame()

    world.drawMap(surface)
    greenTank.move()
    greenTank.rotate()
    greenTank.drawTank(surface)
    purpleTank.move()
    purpleTank.rotate()
    purpleTank.drawTank(surface)
    for bullet in purpleTank.bullets:
        collisionKind = bullet.collision(surface)
        if collisionKind == "GREEN TANK COLLISION":
            greenTank.isWracked = True
            bullet.isExpired = True
        elif collisionKind == "PURPLE TANK COLLISION":
            purpleTank.isWracked = True
            bullet.isExpired = True
        bullet.draw(surface)
    for bullet in greenTank.bullets:
        collisionKind = bullet.collision(surface)
        if collisionKind == "GREEN TANK COLLISION":
            greenTank.isWracked = True
            bullet.isExpired = True
        elif collisionKind == "PURPLE TANK COLLISION":
            purpleTank.isWracked = True
            bullet.isExpired = True
        bullet.draw(surface)
    pygame.display.update()
