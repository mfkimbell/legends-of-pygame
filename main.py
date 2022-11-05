import pygame, sys
from settings import *
from debug import debug

# WIDTH    = 1280	
# HEIGTH   = 720
# FPS      = 60
# TILESIZE = 64

class Game:
    def __init__(self):

        #general setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGTH))
        self.clock = pygame.time.Clock()
    
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            self.screen.fill('black')
            pygame.display.set_caption('legendsOfPygame')
            pygame.display.update()
            self.clock.tick(FPS)
    
if __name__ == '__main__':
    game = Game()
    game.run()