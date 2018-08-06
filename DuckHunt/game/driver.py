import os, sys, time
import pygame
import registry, states, sounds
import config_master
fullPath = '/home/pi/Desktop/retrogamesoriginal/DuckHunt/media'


class Driver(object):
    def __init__(self, surface):
        # Set a global registry
        self.registry = registry.Registry()
        self.registry.set('surface', surface)
        self.registry.set('soundHandler', sounds.SoundHandler())

        controls = pygame.image.load(os.path.join (fullPath, 'controls.png'))
        tup7= (int(states.adjpos (*controls.get_size ())[0]), int(states.adjpos (*controls.get_size ())[1]))
        self.registry.set('controlImgs', pygame.transform.smoothscale (controls, tup7))

        sprites = pygame.image.load(os.path.join (fullPath, 'sprites.png'))
        tup8 =  (int(states.adjpos (*sprites.get_size ())[0]), int(states.adjpos (*sprites.get_size ())[1]))
        sprites = pygame.transform.scale (sprites, tup8)
        self.registry.set('sprites', sprites)
        
        rsprites = pygame.transform.flip(sprites, True, False)
        self.registry.set('rsprites', rsprites)

        self.registry.set('score', 0)
        self.registry.set('round', 1)

        # Start the game
        self.state = states.StartState(self.registry)
        self.state = self.state.start()

    def handleEvent(self, event):
        # Toggle sound
        if event.type == pygame.KEYDOWN and event.key is pygame.K_s:
            self.registry.get('soundHandler').toggleSound()

        self.state.execute(event)

    def update(self):
        newState = self.state.update()

        if newState:
            self.state = newState

    def render(self):
        self.state.render()
        self.registry.get('soundHandler').flush()
