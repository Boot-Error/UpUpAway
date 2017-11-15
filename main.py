#!/usr/bin/env python

import pygame
from pygame.locals import *
import sys
import math
import random

from world import World
from player import Player
from physics import Entity, Environment

pygame.init()
size = (32 * 15, 32 * 30)

FPS = 60
fpsClock = pygame.time.Clock()

screen = pygame.display.set_mode(size)

# game objects init
world = World(size)
player_entity = Entity((0, 0), (32, 64), False)
environ = Environment(size)

player = Player(player_entity)

environ.add_entity(player_entity)

[world.scroll() for x in range(30)]

while True:

    fpsClock.tick(FPS)

    pygame.display.set_caption("Up Up Away")

    # world render
    world.render(screen, 0)
    player.render(screen, player_entity)
    environ.compute()
    # environ.entity_render(screen)

    # key presses
    kp = pygame.key.get_pressed()
    if kp[K_RIGHT]:
        player_entity.move([-2, 0])
    if kp[K_LEFT]:
        player_entity.move([2, 0])
    if kp[K_DOWN]:
        player_entity.velY = 0

    if player_entity.y < 100:
        pass ##[world.scroll() for i in range(1)]

    if pygame.key.get_pressed()[K_SPACE]:

        player_entity.jump(5)
        # world.scroll()
        new_blocks = world.get_stand_as_entities()
        [environ.add_entity(e) for e in new_blocks[:world.board_w]]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
