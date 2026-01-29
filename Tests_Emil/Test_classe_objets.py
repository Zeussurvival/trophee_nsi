import pygame
import os

pygame.display.init()
pygame.font.init()
main_dir = os.path.split(os.path.abspath(__file__))[0]
img_dir = os.path.join(main_dir,"Images") 
bg_image_dir = os.path.join(main_dir,"Tiles/Background_images")

class OBJET():
    def __init__(self,image_name,name,description,can_see):
        self.name = name
        self.description = description
        self.image = pygame.image.load(os.path.join(img_dir,image_name))
        self.image = pygame.transform.scale(self.image,(64,64))
        self.higlights_tiles = can_see
    

class Consumable(OBJET):
    def __init__(self, image_name, name, description):
        super().__init__(image_name, name, description,can_see=False)
        self.type = "consumable"

class Tool(OBJET):
    def __init__(self, image_name, name, description, damage, tier):
        super().__init__(image_name, name, description,can_see=False)
        self.type = "tool"
        self.damage = damage
        self.tier = tier