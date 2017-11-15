import math
import pygame

class Entity(object):

    def __init__(self, position, size, static):

        self.x = position[0]
        self.y = position[1]

        self.velY = 0
        self.g = 0.09

        self.width = size[0]
        self.height = size[1]

        self.color = 0

        self.static = static

    def get_points(self):

        return [
                [self.x, self.y],
                [self.x + self.width, self.y],
                [self.x + self.width, self.y + self.height],
                [self.x, self.y + self.height]
            ]

    def move(self, deltas):

        self.x += deltas[0]
        self.y += deltas[1]

    def jump(self, mag):

        self.velY = -mag

    def poop(self):
        print "%d, %d, %d" % (self.x, self.y, self.static)

class Environment(object):

    def __init__(self, screen_size):
        self.entities = []
        self.env_size = screen_size

    def add_entity(self, entity):
        self.entities.append(entity)

    def is_collided(self, e1, e2):

        if all([
                e1.x < (e2.x + e2.width),
                (e1.x + e1.width) > e2.x,
                e1.y < (e2.y + e2.height),
                (e1.y + e1.height) > e2.y
                ]):
            return True
        else: 
            return False

    def prune(self):
        
        for (i, e) in enumerate(self.entities):
            if e.x > self.env_size[0] or e.y > self.env_size[1]:
                del self.enitites[i]

    def compute(self):
        
        # check collisons
        for e1, e2 in zip(self.entities, self.entities[1:]):
            if self.is_collided(e1, e2):
                print e1.poop()
                e1.velY = 0
                e2.velY = 0


        # fall
        for e in self.entities:
            if e.static == False:
                e.y += e.velY
                e.velY += e.g

    def entity_render(self, screen):

        colors = [
                (0, 200, 0),
                (100, 20, 0)
                ]
        for e in self.entities:
            pygame.draw.rect(screen, colors[e.color], (e.x, e.y, e.width, e.height), 0)
