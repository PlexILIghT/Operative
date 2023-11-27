import pygame
from math import *
screenWidth = 1536
screenHeight = screenWidth // 16 * 9
screenSize = (screenWidth, screenHeight)
fps = 60
fieldOfView = pi / 2.5
accuracyOfDraw = 750
paddingOfRays = fieldOfView / accuracyOfDraw
depthOfField = screenWidth

keys = {"forward": pygame.K_w, "left": pygame.K_a, "back": pygame.K_s, "right": pygame.K_d}

map = [
"1111111111111111",
"14      3     41",
"1    11    22221",
"1            3 1",
"1            3 1",
"1222   2222    1",
"14            41",
"1111111111111111"]

blockSize = 100

worldMap = dict()
for y in range(len(map)):
    for x in range(len(map[0])):
        if map[y][x] != " ":
            worldMap[(x * blockSize, y * blockSize)] = map[y][x]

distanceFromScreen = accuracyOfDraw / (2 * tan(fieldOfView / 2))
proectionCoefficient = screenHeight * 0.01 / accuracyOfDraw * 200
rayThickness = screenWidth / accuracyOfDraw

miniMapScale = 4

textureWidth = 800
textureHeight = 800
textureScale = textureWidth / blockSize

