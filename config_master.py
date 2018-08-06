import api
#import pygame
import sys
from random import shuffle, randrange, choice


#Variables

outside_temp = 'https://cb-oakpi4-vis.dev.osisoft.int/piwebapi/streams/F1AbEXkS_2HFm7kCzmNswAI5qJQRxSpaIiO6BGRRgAd3LcnsQB-8MmU-3ZEihAnbVtoWyHAQ0ItT0FLUEk0LUFGMVxGQUNJTElUSUVTIC0gMTYwMCBBTFZBUkFET1xDQi1PQUtQSTQtUkVMQVlcU0xUQ1xXRUFUSEVSXENBTENVTEFUSU9OU3xPVVRTSURFIEFJUiBURU1QRVJBVFVSRQ/value'

viewglass =  'https://cb-oakpi4-vis.dev.osisoft.int/piwebapi/streamsets/F1EmXkS_2HFm7kCzmNswAI5qJQkgarboiO6BGRRgAd3LcnsQQ0ItT0FLUEk0LUFGMVxGQUNJTElUSUVTIC0gMTYwMCBBTFZBUkFET1xDQi1PQUtQSTQtUkVMQVlcVklFVyBHTEFTUw/value'

kwh = 'https://cb-oakpi4-vis.dev.osisoft.int/piwebapi/streams/F1AbEXkS_2HFm7kCzmNswAI5qJQjxOpaIiO6BGRRgAd3LcnsQq0k2UM21qECUTgx09JHWqgQ0ItT0FLUEk0LUFGMVxGQUNJTElUSUVTIC0gMTYwMCBBTFZBUkFET1xDQi1PQUtQSTQtUkVMQVlcU0xUQ1xFTkVSR1kgQ09OU1VNUFRJT058QlVJTERJTkcgRU5FUkdZIEtXSA/value'

target = 'https://cb-oakpi4-vis.dev.osisoft.int/piwebapi/streams/F1AbEXkS_2HFm7kCzmNswAI5qJQPBKpaIiO6BGRRgAd3LcnsQDMwu-s7Dv1QDdMdK-EzjuQQ0ItT0FLUEk0LUFGMVxGQUNJTElUSUVTIC0gMTYwMCBBTFZBUkFET1xDQi1PQUtQSTQtUkVMQVlcREVWSUNFU1xWQVZSSCAxLTA2fFJPT00gVEVNUEVSQVRVUkV8VEFSR0VU/value'

indoor_temp = 'https://cb-oakpi4-vis.dev.osisoft.int/piwebapi/streams/F1AbEXkS_2HFm7kCzmNswAI5qJQPBKpaIiO6BGRRgAd3LcnsQFbdwUBTaVF8NBDcDIB-IGgQ0ItT0FLUEk0LUFGMVxGQUNJTElUSUVTIC0gMTYwMCBBTFZBUkFET1xDQi1PQUtQSTQtUkVMQVlcREVWSUNFU1xWQVZSSCAxLTA2fFJPT00gVEVNUEVSQVRVUkU/value'

#DUCKHUNT CONFIG


numRounds = int(api.getVal(target) - 70)
if (numRounds < 2):
    numRounds = 2
if (numRounds >  5):
    numRounds = 5   
print(numRounds)
numReload = numRounds #NUMROUNDS
speedx =  int((api.getVal(outside_temp) - 68) + 5)
if (speedx < 3):
    speedx = 3#4
speedy = speedx + 2 #speedX + 2
score = (int((1/(api.getVal(kwh)))*100)) #10
timer = 10 #10


roundSpeed = 1 # 1
frames = 60 #60
#amount of ducks available per round.
testnum = 10 #10

#amt of ducks + 2
amtDucks = 0 #0
miss = 4 #4

fullPath = '/home/pi/Desktop/retrogamesoriginal/DuckHunt/media'

#END DUCKHUNT CONFIG

#FLAPPYBIRD CONFIG

fps = 30 #30
gapsize = 100 #100
gravity = 1 #1
jumpheight = -9 #-9
#rotational bounce
bounce = 20 #20
angularspeed = 3 #3
velocitydown = 10 #10
flappyscore = 1 #1

flappypath = '/home/pi/Desktop/retrogamesoriginal/FlappyBird/assets/sprites'

#END FLAPPYBIRD CONFIG

#SPACEINVADERS CONFIG

enemyPositionDefault = 65 #65
shipSpeed = 10 # 10
bulletSpeed = 15 #15
enSpeed = 5 #5
enBulletSpeed = 700 #700 - lower makes it faster
spacepath = '/home/pi/Desktop/retrogamesoriginal/SpaceInvaders/images'
#END SPACEINVADERS CONFIG

#SNAKE CONFIG

width = 1000  #640
height = 500 #320
snakescore = 1 #1
gamespeed = 15 #15
multiplier = 1 #1

#END SNAKE CONFIG
