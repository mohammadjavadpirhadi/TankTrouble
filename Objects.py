import random, pygame


class world:
    def loadMaps(self):
        self.maps.append(pygame.image.load('Maps/Map.png'))

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

    def loadPicture(self, directory):
        self.picture = pygame.image.load(directory)

    def drawTank(self, surface):
        surface.blit(self.picture, (self.x, self.y))

    def __init__(self, X, Y, directory):
        self.picture = None
        self.loadPicture(directory)
        self.x = X
        self.y = Y
        self.height = 50
        self.width = 75


class bullet:
    pass
