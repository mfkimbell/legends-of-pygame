import pygame
pygame.init()
font = pygame.font.Font(None,30)

def debug(info,y = 10, x = 10):
	display_surface = pygame.display.get_surface()
	debug_surf = font.render(str(info),True,'White')
	debug_rect = debug_surf.get_rect(topleft = (x,y))
	pygame.draw.rect(display_surface,'Black',debug_rect)

	display_surface.blit(debug_surf,debug_rect)

def debug2(info, y = 40, x = 10):
	display_surface = pygame.display.get_surface()
	debug_surf = font.render("PlayerX: " + str(info),True,'White')
	debug_rect = debug_surf.get_rect(topleft = (x,y))
	pygame.draw.rect(display_surface,'Black',debug_rect)
	display_surface.blit(debug_surf,debug_rect)

def debug3(info, y = 70, x = 10):
	display_surface = pygame.display.get_surface()
	debug_surf = font.render("PlayerY: " + str(info),True,'White')
	debug_rect = debug_surf.get_rect(topleft = (x,y))
	pygame.draw.rect(display_surface,'Black',debug_rect)
	display_surface.blit(debug_surf,debug_rect)

def debug4(info, y = 110, x = 10):
	display_surface = pygame.display.get_surface()
	debug_surf = font.render("PlayerCollide: " + str(info),True,'White')
	debug_rect = debug_surf.get_rect(topleft = (x,y))
	pygame.draw.rect(display_surface,'Black',debug_rect)
	display_surface.blit(debug_surf,debug_rect)

def debug5(info, y = 140, x = 10):
	display_surface = pygame.display.get_surface()
	debug_surf = font.render("Offset: " + str(info),True,'White')
	debug_rect = debug_surf.get_rect(topleft = (x,y))
	pygame.draw.rect(display_surface,'Black',debug_rect)
	display_surface.blit(debug_surf,debug_rect)

def debug6(info, y = 170, x = 10):
	display_surface = pygame.display.get_surface()
	debug_surf = font.render("Status: " + str(info),True,'White')
	debug_rect = debug_surf.get_rect(topleft = (x,y))
	pygame.draw.rect(display_surface,'Black',debug_rect)
	display_surface.blit(debug_surf,debug_rect)


