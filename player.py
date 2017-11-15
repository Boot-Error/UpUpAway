import pygame
import math

class Player(object):

    def __init__(self, entity):

        self.posX = entity.x
        self.posY = entity.y
    
    def render(self, screen, entity):
        
        self.posX = entity.x
        self.posY = entity.y

        coords = (
                self.posX,
                self.posY,
                32,
                64)
        pygame.draw.rect(screen, (0, 200, 0), coords, 0)
