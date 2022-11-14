from csv import reader
from os import walk
import pygame

def import_csv_layout(path):
    terrain_map = []
    with open(path) as level_map:
        layout = reader(level_map,delimiter = ',')
    
        for row in layout:
            print(row)
            terrain_map.append(list(row))

        return terrain_map

def import_folder(path):
    surface_list = []
    #walk takes folder name, subfolder names as the first
    #two input, so we put _ and __ because we don't care
    for _,__,img_files in walk(path):
        for image in img_files:
            full_path = path + '/' + image
            image_surf = pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surf)
    
    return surface_list

