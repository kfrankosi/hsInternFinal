import os, sys
import pygame
import pygame.transform
#sys.path.append('/home/pi/Desktop/retrogamesoriginal/DuckHunt/game/')
#from DuckHunt import config_master
#from DuckHunt import game
from game.registry import adjpos, adjrect, adjwidth, adjheight
import config_master
from config_master import fullPath
# Game parameters
print("inn dh game")
SCREEN_WIDTH, SCREEN_HEIGHT = adjpos (800, 500)
TITLE = "Symons Media: Duck Hunt"
FRAMES_PER_SEC = config_master.frames

BG_COLOR = 255, 255, 255

# Initialize pygame before importing modules
pygame.mixer.pre_init(44100, -16, 2, 1024)
pygame.init()
pygame.display.set_caption(TITLE)
pygame.mouse.set_visible(False)

import game.driver


class Game(object):
    def __init__(self):
        self.running = True
        self.surface = None
        self.clock = pygame.time.Clock()
        self.size = SCREEN_WIDTH, SCREEN_HEIGHT

       

        background = os.path.join(fullPath, 'background.jpg')
        bg = pygame.image.load(background)
        self.size = (int(self.size[0]), int(self.size[1]))
        self.background = pygame.transform.smoothscale (bg, self.size)
        self.driver = None

    def init(self):
        self.surface = pygame.display.set_mode(self.size)
        self.driver = game.driver.Driver(self.surface)

    def handleEvent(self, event):
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key is 27):
            self.running = False
        else:
            self.driver.handleEvent(event)

    def loop(self):
        self.clock.tick(FRAMES_PER_SEC)
        self.driver.update()

    def render(self):
        self.surface.blit(self.background, (0,0))
        self.driver.render()
        pygame.display.flip()

    def cleanup(self):
        pygame.quit()
        sys.exit(0)

    def execute(self):
        self.init()
        if True:
            pygame.display.toggle_fullscreen()
        while (self.running):
            for event in pygame.event.get():
                self.handleEvent(event)
            self.loop()
            self.render()

        self.cleanup()

#if __name__ == "__main__":
def play():
    theGame = Game()
    theGame.execute()
