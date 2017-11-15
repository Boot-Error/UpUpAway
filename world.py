import math
import random
import pygame

from physics import Entity

class World(object):

    def __init__(self, screen_size):

        self.board_w = 15
        self.board_h = 30
        self.screenBuff = [[0] * self.board_w] * self.board_h
        self.air_platform_count = 0
        self.last_side = 1

    def new_platform(self, sides = 1, board_size = 3):

        if sides in [1, 2]:
        
            snap_side = sides - 1
            if snap_side == 0:
                return [1]*board_size + [0]*(self.board_w - board_size)
            else:
                return [0]*(self.board_w - board_size) + [1]*board_size

        elif sides == 3:

            left_size = random.randint(1, board_size)
            right_size = random.randint(1, board_size)
            air = self.board_w - (left_size + right_size)

            return [1]*left_size + [0]*air + [1]*right_size

        else:

            return [0] * self.board_w

    def stand_blocks(self):

        result = []
        for (j, row) in enumerate(self.screenBuff):
            for (i, block_id) in enumerate(row):
                coords = (32 * i, 32 * j,  (32 * i) + 32, (32 * j) + 32)
                if block_id == 1:
                    result.append(coords)

        return result

    def get_stand_as_entities(self):

        return map(lambda x: Entity(x[:2], (32, 32), True), self.stand_blocks())

    def render(self, screen, offset = -2):

        for (j, row) in enumerate(self.screenBuff):
            for (i, block_id) in enumerate(row):
                coords = (32 * i, 32 * j,  (32 * i) + 32, (32 * j) + 32)
                if block_id == 0:
                    pygame.draw.rect(screen, (0, 0, 200), coords, 0)

                if block_id == 1:
                    pygame.draw.rect(screen, (100, 20, 0), coords, 0)

    def scroll(self):

        if self.air_platform_count > 1:
            sides = 0
            self.air_platform_count %= 3

        else:
            sides = self.last_side
            self.last_side = 1 if self.last_side == 2 else 2

        self.air_platform_count += 1

        new_row = self.new_platform(sides = sides, board_size = random.randint(2, 5))
        self.screenBuff.pop()
        self.screenBuff.insert(0, new_row)

        return new_row
