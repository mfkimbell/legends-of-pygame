import pygame 
from settings import *
from tile import Tile
from player import Player
from debug import debug



class Level:
    def __init__(self):
        #get display surface
        self.display_surface = pygame.display.get_surface()

        #sprite group initialization
        self.visible_sprites = YSortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()

        #sprite setup
        self.create_map()
    
    def create_map(self):
        for row_index, row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):
                x = col_index*TILESIZE
                y = row_index*TILESIZE
                if col == 'x':
                    Tile((x,y),[self.visible_sprites,self.obstacle_sprites])
                if col == 'p':
                    
                    self.player = Player((x,y),[self.visible_sprites],self.obstacle_sprites)
                    #this sets 'player' to the player variable that was created
                    #at the tile location of 'p'


    
    def run(self):
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()
        #update and draw the game
        debug(self.player.direction)
        pass


class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        #general setup
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()
        
    def custom_draw(self,player):
        #getting offset
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height


        #for sprite in self.sprites(): old way
        #new way has sprites ordered by y value, so the ones with higher y values
        # are rendered first, thus will appear BEHIND lower sprites
        for sprite in sorted(self.sprites(),key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image,offset_pos)