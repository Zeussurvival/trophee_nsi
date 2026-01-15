import numpy
import pygame
import random
import os

pygame.display.init()
pygame.font.init()
main_dir = os.path.split(os.path.abspath(__file__))[0]
img_dir = os.path.join(main_dir,"Humanoid") 
frames_image_dir = os.path.join(main_dir,"Tiles/frames")


#         self.image = pygame.image.load(os.path.join(img_dir, image)).convert_alpha()
#         self.image = pygame.transform.rotate(self.image,rotate)
#         self.image = pygame.transform.scale(self.image,(16,16))
#         if background_image != None:
#             self.background_image = pygame.image.load(os.path.join(bg_image_dir, background_image)).convert_alpha()
#         else:
#             self.background_image = None
class Humanoid:
    def __init__(self,pos,pv,base_damage,speed,image,list_images,LEN_SQUARE):
        self.vect = pygame.math.Vector2(0,0)
        self.pos = pos
        self.pv = pv
        self.speed = speed * LEN_SQUARE
        self.base_damage = base_damage
        self.image_length = (64,96)



        if image != None:
            self.image = pygame.image.load(os.path.join(img_dir, image)).convert_alpha()
            self.image = pygame.transform.scale(self.image,(64,96))
        else:
            self.image = None

        if list_images != None:
            self.images_to_add = list_images
            self.True_list_images = []
            for img in list_images:
                image = pygame.image.load(os.path.join(img_dir, img)).convert_alpha()
                image = pygame.transform.scale(image,(64,96))
                self.True_list_images.append(image)
        else:
            self.images_to_add = None
        self.poid = 0

    def blit_self(self,screen,pos,key_pressed):
        vrai_pos = pos[0]-32,pos[1]-48
        if len(key_pressed) < 1:

            screen.blit(self.image,vrai_pos)
        else:
            screen.blit(self.True_list_images[0],vrai_pos)
        self.blit_center_self(screen,pos,key_pressed)
        
    def blit_center_self(self,screen,pos,key_pressed):
        H,W = pygame.Surface.get_height(screen),pygame.Surface.get_width(screen) #self.image_length[1]/2
        screen.blit(self.image,(W/2-self.image_length[0]/2,H/2-self.image_length[1]/2))
        pygame.draw.line(screen,"green",(W/2,H/2-100),(W/2,H/2+100)) # Croix central
        pygame.draw.line(screen,"green",(W/2-100,H/2),(W/2+100,H/2)) # Croix central

    def do_movement_by_self(self,keys,dt,screen,Actual_map):
        self.vect = pygame.math.Vector2(0,0)
        last_key_pressed = []
        if keys[pygame.K_q]:
            self.vect[0] -= self.speed * dt
            last_key_pressed.append("q")
        if keys[pygame.K_d]:
            self.vect[0] += self.speed * dt
            last_key_pressed.append("d")    
        if keys[pygame.K_s]:
            self.vect[1] += self.speed * dt    
            last_key_pressed.append("s")        
        if keys[pygame.K_z]:
            self.vect[1] -= self.speed * dt
            last_key_pressed.append("z")    

        if self.vect.length()!= 0: # eviter de faire des calculs pour rien ET ...
            if self.vect.length() / (self.speed *dt + 10 **-10) > 1:
                self.vect = self.vect.normalize() * self.speed *dt
            # if self.pos[0] - 0 < 0: # le -0 sert a faire une collision simple eviter de sortir de la map niveau image du joueur et le nb devrait etre taille image / 2
            #     self.pos[0] = 0 
            # if self.pos[1] - 0 < 0:
            #     self.pos[1] = 0
            self.do_collision_check(self.vect,self.pos,Actual_map)

            self.pos[0],self.pos[1] = round(self.pos[0],2),round(self.pos[1],2)
        self.blit_center_self(screen,self.pos,last_key_pressed)

    def do_collision_check(self,vect_mvt,pos,Map):
        final_posi = pos + vect_mvt

        fake_pos = final_posi
        if fake_pos[0] - self.image_length[0]/2 < 0: # Check les collisions pour les bords de la map
            fake_pos[0] = self.image_length[0]/2
        if fake_pos[1] - self.image_length[1]/2< 0:
            fake_pos[1] = self.image_length[1]/2
        if fake_pos[0] + self.image_length[0]/2 > Map.shape[1] * 64: # 64 et pas LEN SQUARE !!
            fake_pos[0] = Map.shape[1] * 64 - self.image_length[0]/2
        if fake_pos[1] + self.image_length[1]/2 > Map.shape[1] * 64:
            fake_pos[1] = Map.shape[1] * 64 - self.image_length[1]/2

        print(vect_mvt.length())
        self.pos = fake_pos

        