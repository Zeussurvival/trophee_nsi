import numpy
import pygame
import random
import os

pygame.display.init()
pygame.font.init()
main_dir = os.path.split(os.path.abspath(__file__))[0]
img_dir = os.path.join(main_dir,"Tiles") 
bg_image_dir = os.path.join(main_dir,"Tiles/Background_images")


#         self.image = pygame.image.load(os.path.join(img_dir, image)).convert_alpha()
#         self.image = pygame.transform.rotate(self.image,rotate)
#         self.image = pygame.transform.scale(self.image,(16,16))
#         if background_image != None:
#             self.background_image = pygame.image.load(os.path.join(bg_image_dir, background_image)).convert_alpha()
#         else:
#             self.background_image = None
class Tile:
    def __init__(self,image,list_images,rotate):
        self.image = pygame.image.load(os.path.join(img_dir, image)).convert_alpha()
        self.image = pygame.transform.rotate(self.image,rotate)
        self.image = pygame.transform.scale(self.image,(16,16))
        if list_images != None:
            self.images_to_add = list_images
        else:
            self.images_to_add = None
        self.poid = 0

    def blit_self(self,screen,pos):
        screen.blit(self.image,pos)