import pygame
from pygame.locals import *
import settings

class GameMap(pygame.sprite.Sprite):
    def __init__(self, map_image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(map_image)
        self.splits = 15
        self.scale = 2
        self.tile_width = self.image.get_width() / self.splits
        self.tile_height = self.image.get_height() / self.splits
        self.tiles = []
        self.last_left = -1
        self.last_top = -1

        # for i in range(0, self.splits, 1):
        #     for j in range(0, self.splits, 1):
        #         self.tiles.append(self.image.subsurface(
        #             Rect(i * self.tile_width,
        #                  j * self.tile_height,
        #                  self.tile_width,
        #                  self.tile_height)))
        #
        #         for x in range(0, self.scale, 1):
        #             self.tiles[-1] = pygame.transform.scale2x(self.tiles[-1])

        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.load_sector(settings.car_x, settings.car_y)

    def load_sector(self, car_x, car_y):
        left = car_x - (car_x % self.tile_width) - (2 * self.tile_width)
        top = car_y - (car_y % self.tile_height) - (2 * self.tile_height)
        print("Tile height: " + str(self.tile_height) + "      tile width: " + str(self.tile_width))
        print("Centre x: " + str(car_x) + "    left: " + str(left))
        print("Centre y: " + str(car_y) + "    top: " + str(top))

        if (abs(left - self.last_left) >= (1.5 * self.tile_width)) or (abs(top  - self.last_top)  >= (1.5 * self.tile_height)):
                self.tiles = []
                for i in range(0, 5, 1):
                    for j in range(0, 5, 1):
                        self.tiles.append(self.image.subsurface(
                            Rect(i * self.tile_width,
                                 j * self.tile_height,
                                 self.tile_width,
                                 self.tile_height)))
                        for x in range(0, self.scale, 1):
                            self.tiles[-1] = pygame.transform.scale2x(self.tiles[-1])

        self.last_left = left
        self.last_top = top

    #draw map from top left of screen
    def draw(self, screen, camera):
        for i in range(0, 5, 1):
            for j in range(0, 5, 1):
                screen.blit(self.tiles[j + i * 5],
                            Rect(i * self.tile_width * (2 ^ self.scale),
                            j * self.tile_height * (2 ^ self.scale),
                            self.tile_width * (2 ^ self.scale),
                            self.tile_height * (2 ^ self.scale)))
