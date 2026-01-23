import pygame
import os

pygame.display.init()
pygame.font.init()
main_dir = os.path.split(os.path.abspath(__file__))[0]
img_dir = os.path.join(main_dir,"Images") 
bg_image_dir = os.path.join(main_dir,"Tiles/Background_images")

class OBJET():
    def __init__(self,image_name,name,description):
        self.name = name
        self.description = description
        self.image = pygame.image.load(os.path.join(img_dir,image_name))
        self.image = pygame.transform.scale(self.image,(64,64))
    
    

    # def draw_hotbar(self,screen):
    #     lenght_square = 64
    #     width = 6
    #     true_lenght = lenght_square + 2*width
    #     offset = 15 
    #     y_offset = offset + 10
    #     number_shown = 5
    #     first_x = screen.get_size()[0]/2 - 2*(offset+true_lenght) - lenght_square/2
    #     y = screen.get_size()[1] -lenght_square - y_offset
    #     for i in range(0,number_shown):
    #         pygame.draw.rect(screen,(200,200,200),(first_x+(lenght_square+width+offset)*i,y,true_lenght,true_lenght),width)
    #         if self.inventaire[i] != None:
    #             screen.blit(pygame.transform.scale(self.inventaire[i].image,(lenght_square,lenght_square)),(first_x+width+(lenght_square+width+offset)*i,y+width))
        
    #     pygame.draw.rect(screen,"white",(first_x+(lenght_square+width+offset)*self.held_item_indice  -2 ,y - 2,true_lenght + 4,true_lenght + 4 ),width+ 2)


    # def do_everything(self,screen,FONT_None,dt,keys):
    #     if self.detectable and self.alive == True:
    #         self.moove(keys,dt)
    #         self.endurance_regen(dt)
    #     self.draw_hp_endurance(screen,FONT_None)
    #     self.draw_hotbar(screen)
    #     if self.alive == False:
    #         self.death_mesage(screen)


    # def use_hand(self,zombie_list,Human):
    #     if self.held_item != None:
    #         response,zombie_list = self.held_item.use_self(self.endurance,zombie_list,Human)
    #         if response:
    #             self.endurance_last_used = time.time()
    #             self.endurance -= 3 # self.held_item.endurance_used a mettre mais flm la il est 1h41

    #     else:
    #         print(None) 
    #     return zombie_list


    # def attack(self):
    #     if self.inventaire[0].type == "gun" or "knife" and self.endurance>3:
    #         self.endurance_last_used = time.time()
    #         response = self.inventaire[0].attack()
    #         print(response)
    #         if response:
    #             self.endurance -= 3


    # def change_held_item(self,keys):
    #     if keys[pygame.K_1]:
    #         self.held_item_indice = 0
    #         self.held_item = self.inventaire[0]
    #     if keys[pygame.K_2]:
    #         self.held_item_indice = 1
    #         self.held_item = self.inventaire[1]
    #     if keys[pygame.K_3]:
    #         self.held_item_indice = 2
    #         self.held_item = self.inventaire[2]
    #     if keys[pygame.K_4]:
    #         self.held_item_indice = 3
    #         self.held_item = self.inventaire[3]
    #     if keys[pygame.K_5]:
    #         self.held_item_indice = 4
    #         self.held_item = self.inventaire[4]
    #     pass
