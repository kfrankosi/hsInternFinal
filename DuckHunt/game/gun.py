import os, sys
import pygame
import config_master
fullPath = '/home/pi/Desktop/retrogamesoriginal/DuckHunt/media'

class Gun(object):
    def __init__(self, registry):
        self.registry = registry
        #num of bullets
        self.rounds = config_master.numRounds
        self.mousePos = (0,0) # Starting postion
        self.mouseImg = pygame.image.load(os.path.join(fullPath, 'crosshairs.png'))

    def render(self):
        surface = self.registry.get('surface')
        surface.blit(self.mouseImg, self.mousePos)

    def reloadIt(self):
        #num of bullets per reload
        self.rounds = config_master.numReload

    def moveCrossHairs(self, pos):
        xOffset = self.mouseImg.get_width() / 2
        yOffset = self.mouseImg.get_height() / 2
        x, y = pos
        self.mousePos = (x - xOffset), (y - yOffset)

    def shoot(self):
        if self.rounds <= 0:
            return False

        self.registry.get('soundHandler').enqueue('blast')
        self.rounds = self.rounds - 1
        return True
