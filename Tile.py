import pygame
from settings import *

class Tile(pygame.sprite.Sprite):
    def __init__(self,pos,groups): #pos is position #groups is the sprite group it will be a part of
        super().__init__(groups)
        self.image = pygame.image.load(''../graphics/test/rock.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
