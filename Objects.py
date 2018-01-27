import math
import pygame
import pygame.event as GAME_EVENTS
import pygame.locals as GAME_GLOBALS
import pygame.time as GAME_TIME
import random


class world:
    def loadMaps(self):
        self.maps.append(pygame.image.load('Maps/Map1.png'))

    def chooseMap(self):
        self.Map = self.maps[random.randrange(len(self.maps))]

    def drawMap(self, surface):
        self.chooseMap()
        surface.blit(self.Map, (0, 0))

    def __init__(self):
        self.maps = []
        self.loadMaps()
        self.Map = None

class tank:

    def loadPicture(self, Imagedirectory):
        self.picture = pygame.image.load(Imagedirectory)

    def rotate(self):
        if self.leftRotate:
            self.angle += self.rotateSpeed
            if self.angle >= 360:
                self.angle = self.angle - (360 * int(self.angle / 360))
        if self.rightRotate:
            self.angle -= self.rotateSpeed
            if self.angle <= -360:
                self.angle = self.angle + (360 * int(self.angle / -360))
        self.rouPicture = pygame.transform.rotate(self.picture, self.angle)

    def drawTank(self, surface):
        if not self.isWracked:
            halfOfDiameter = (self.pictureWidth ** 2 + self.pictureWidth ** 2) ** (0.5)
            self.pictureAngle = self.angle
            if self.pictureAngle >= 90:
                self.pictureAngle = self.pictureAngle - (90 * int(self.angle / 90))
            if self.pictureAngle <= -90:
                self.pictureAngle = self.pictureAngle + (90 * int(self.angle / -90))
            if self.pictureAngle < 0:
                self.pictureAngle = -self.pictureAngle
            xyDifference = (self.pictureWidth * math.cos(
                (self.pictureAngle) * math.pi / 180) + self.pictureWidth * math.sin(
                (self.pictureAngle) * math.pi / 180))

            surface.blit(self.rouPicture,
                         (
                             self.x - xyDifference / 2,
                             self.y - xyDifference / 2))

    def move(self):
        if self.forwardDirection:
            self.vx = self.v * math.cos((-self.angle * math.pi) / 180)
            self.vy = self.v * math.sin((-self.angle * math.pi) / 180)
            self.x += self.vx
            self.y += self.vy
        if self.backwardDirection:
            self.vx = self.v * math.cos((-self.angle * math.pi) / 180)
            self.vy = self.v * math.sin((-self.angle * math.pi) / 180)
            self.x -= self.vx
            self.y -= self.vy

    def fire(self):
        if not self.isWracked and len(self.bullets) < 5:
            bullet(self)

    def collision(self):
        pass

    def __init__(self, X, Y, Imagedirectory):
        self.x = X
        self.y = Y
        self.picture = None
        self.rouPicture = None
        self.pictureAngle = 0
        self.loadPicture(Imagedirectory)
        self.height = 50
        self.width = 75
        self.pictureHeight = 75
        self.pictureWidth = 75
        self.angle = random.randrange(360)
        self.rotateSpeed = 3
        self.v = 5
        self.vx = self.v * math.cos((-self.angle * math.pi) / 180)
        self.vy = self.v * math.sin((-self.angle * math.pi) / 180)
        self.forwardDirection = False
        self.backwardDirection = False
        self.leftRotate = False
        self.rightRotate = False
        self.rotate()
        self.bullets = []
        self.isWracked = False


class bullet:
    def __init__(self, tank):
        self.tank = tank
        self.x = tank.x + tank.width * math.cos((-tank.angle * math.pi) / 180) / 2
        self.y = tank.y + tank.width * math.sin((-tank.angle * math.pi) / 180) / 2
        self.angle = tank.angle
        self.radius = 5
        self.v = 3.5
        self.vx = self.v * math.cos((self.angle * math.pi) / 180)
        self.vy = self.v * math.sin((self.angle * math.pi) / 180)
        tank.bullets.append(self)
        self.isExpired = False
        self.startTime = GAME_TIME.get_ticks()
        self.expireTime = 10000

    def draw(self, surface):
        if not self.isExpired:
            if (GAME_TIME.get_ticks() - self.startTime) < self.expireTime:
                self.move()
                pygame.draw.circle(surface, (0, 0, 0), (round(self.x), round(self.y)), self.radius, 0)
            else:
                self.isExpired = True
                self.tank.bullets.remove(self)

    def move(self):
        self.vx = self.v * math.cos((-self.angle * math.pi) / 180)
        self.vy = self.v * math.sin((-self.angle * math.pi) / 180)
        self.x += self.vx
        self.y += self.vy

    def collision(self, surface):
        if surface.get_at((int(self.x + self.radius), int(self.y))) == (101, 101, 101, 255):
            self.angle = 180 - self.angle
        elif surface.get_at((int(self.x - self.radius), int(self.y))) == (101, 101, 101, 255):
            self.angle = 180 - self.angle
        elif surface.get_at((int(self.x), int(self.y + self.radius))) == (101, 101, 101, 255):
            self.angle = - self.angle
        elif surface.get_at((int(self.x), int(self.y - self.radius))) == (101, 101, 101, 255):
            self.angle = - self.angle
            return "WALL COLLISION"
        if surface.get_at((int(self.x + self.radius), int(self.y))) == (1, 1, 1, 255) or surface.get_at(
                (int(self.x - self.radius), int(self.y))) == (1, 1, 1, 255) or surface.get_at(
                (int(self.x), int(self.y + self.radius))) == (1, 1, 1, 255) or surface.get_at(
                (int(self.x), int(self.y - self.radius))) == (1, 1, 1, 255):
            if GAME_TIME.get_ticks() - self.startTime > 100:
                return "PURPLE TANK COLLISION"
        if surface.get_at((int(self.x + self.radius), int(self.y))) == (1, 101, 1, 255) or surface.get_at(
                (int(self.x - self.radius), int(self.y))) == (1, 101, 1, 255) or surface.get_at(
                (int(self.x), int(self.y + self.radius))) == (1, 101, 1, 255) or surface.get_at(
                (int(self.x), int(self.y - self.radius))) == (1, 101, 1, 255):
            if GAME_TIME.get_ticks() - self.startTime > 100:
                return "GREEN TANK COLLISION"
    # def collisions(self):
    # if surface.get_at(self.x , self.y + self.radius) == (0, 0, 0, 255):
    # leftOfPlayerOnPlatform = False
