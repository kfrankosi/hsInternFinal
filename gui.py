import pygame
import sys


init_status = pygame.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()


print ("Move joystick up to play Duck Hunt")
print ("Move joystick right to play Snake")
print ("Move joystick down to play Flappy Bird")
print ("Move joystick left to play Space Invaders")

#game loop
while True:
    if True:
        pygame.mouse.set_visible(0)

    playing = False
    while True:
            for event in pygame.event.get():
                    y = int(joystick.get_axis(1)*1.5)
                    x = int(joystick.get_axis(0)*1.5)

                    #if event.type == pygame.QUIT:
                     #       pygame.quit()
                      #      sys.exit()
                    if event.type == pygame.JOYAXISMOTION:
                        playing = True
                        # joystick up for duckhunt
                        if y == -1:
                            print("Duck Hunt")
                            import os
                            print (os.getcwd()) # File "/home/pi/Desktop/retro
                            import config_master
                            from DuckHunt import duckhunt
                            duckhunt.play()
                            print("after duckhunt.play()")
                            
                        # joystick right for snake
                        elif x == 1:
                            print ("Snake")
                            from Snake import snake_game
                            #foo = imp.load_source('snake_game.py', '/home/pi/Desktop/retrogamesoriginal/Snake/snake_game.py')
                            #foo()
                        # joystick down for flappy bird
                        elif y == 1:
                            print("Flappy Bird")
                            from FlappyBird import flappy
                            
                        # joystick left for space invaders
                        elif x == -1:
                            #print("Space Invaders")
                            from SpaceInvaders import spaceinvaders

