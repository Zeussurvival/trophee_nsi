import pygame
import numpy
import random
import time
import math
import Test_def as D
import Test_classe_tile as CT
import Test_classe_humain as CH
import Test_classe_objets as CO
import winreg
def audio_device_available():
    # Retourne True si Windows a AU MOINS un périphérique audio fonctionnel.
    # On lit le registre Windows : s'il n'y a aucun endpoint audio actif,
    # pygame.mixer ne doit PAS être initialisé.
    try:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,r"SOFTWARE\Microsoft\Windows\CurrentVersion\MMDevices\Audio\Render")
        pygame.mixer.init()
    except:
        return False
    
# https://www.youtube.com/watch?v=uWvb3QzA48c&list=PLsk-HSGFjnaG-BwZkuAOcVwWldfCLu1pq

pygame.display.init()
pygame.font.init()

W,H = (1280, 720)
screen = pygame.display.set_mode((W,H))
clock = pygame.time.Clock()
LEN_SQUARE = 64
dt = 0

Actual_map = D.creation_map_rectangle(120,120)
Actual_map_pollution = D.set_pollution_map_rectangle(10,10,Actual_map,5)

List_tiles = [CT.Tile("background_1.png",None,0),CT.Tile("background_1.png",None,90),CT.Tile("background_1.png",None,180),CT.Tile("background_1.png",None,270),\
              CT.Tile("background_2.png",None,0),CT.Tile("background_2.png",None,90),CT.Tile("background_2.png",None,180),CT.Tile("background_2.png",None,270),\
              ]

for y in range(Actual_map.shape[0]):
    for x in range(Actual_map.shape[1]):
        Actual_map[x,y] = random.randint(0,7)
print(Actual_map_pollution)

List_ground_objets = []
pomme = CO.Consumable("apple.png","Pomme","Une pomme bien délicieuse")
List_ground_objets.append((pomme,(300,200)))
bush = CO.Tool("bush.png","Buisson","Ce buisson permet de cultiver des pommes",10,1)


Arial_font = pygame.font.SysFont('Arial', 30)
Surface_text_pickup = Arial_font.render('Press [E] to pick it up !', False, (255,255,255))
can_pickup = True


hotbar = [bush,None,None,None,None]
Robot = CH.Humanoid((15*LEN_SQUARE,15*LEN_SQUARE),100,5,5,"robot_front_wait.png",["robot_front_walking.png"],LEN_SQUARE,hotbar)
print("running now")
running = True
while running:
    time_0 = time.time()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("black")
    keys = pygame.key.get_pressed()
    mouse_pos = pygame.mouse.get_pos()

    for y in range(Actual_map.shape[0]): # montre la map
        for x in range(Actual_map.shape[1]):
            List_tiles[Actual_map[x,y]].blit_self(screen,(x*LEN_SQUARE-Robot.pos[0]+W/2, y*LEN_SQUARE-Robot.pos[1]+H/2))

    if keys[pygame.K_e]: #recuperer objets
        for obj in List_ground_objets:
            if (Robot.pos[0] - obj[1][0])**2 +(Robot.pos[1] - obj[1][1])**2 <= (LEN_SQUARE*Robot.range_pickup)**2 and can_pickup:
                can_pickup = False
                if Robot.pickup(obj[0]):
                    List_ground_objets.remove(obj)
    else:
        can_pickup = True               

    if keys[pygame.K_n]:
        if Robot.hotbar[Robot.held_item_indice] != None:
            List_ground_objets.append((Robot.hotbar[Robot.held_item_indice],Robot.pos))
            Robot.hotbar[Robot.held_item_indice] = None



    for obj in List_ground_objets: # mettre le texte pick up
        if (Robot.pos[0] - obj[1][0])**2 +(Robot.pos[1] - obj[1][1])**2 <= (LEN_SQUARE*Robot.range_pickup)**2:
            screen.blit(Surface_text_pickup, (obj[1][0]-Robot.pos[0]+W/2-Surface_text_pickup.get_size()[0]/2, obj[1][1]-Robot.pos[1]+H/2-Surface_text_pickup.get_size()[1]/2 - 32 - 10 - 8*math.cos(time.time())))
        screen.blit(pygame.transform.scale(obj[0].image,(32,32)),(obj[1][0]-Robot.pos[0]+W/2 - 16,obj[1][1]-Robot.pos[1]+H/2 - 16))

    Pos_souris_monde=(Robot.pos[0]-W/2+mouse_pos[0],Robot.pos[1]-H/2+mouse_pos[1]) # position de la souris ds le monde en pixels
    tile_souris = ((Pos_souris_monde[0]//LEN_SQUARE)*LEN_SQUARE,(Pos_souris_monde[1]//LEN_SQUARE)*LEN_SQUARE) # on va floor (si victor a raison que cest un floor mdr) la position a la case 
    centre_tile = (tile_souris[0]+32,tile_souris[1]+32) # on prends dcp le centre de la tile, en gros c juste len_square /2 mais on va simplifier
    diff = (centre_tile[0]-Robot.pos[0],centre_tile[1]-Robot.pos[1]) # reconversion en pos ecran
    if diff[0]**2+diff[1]**2<=(Robot.range_pickup*LEN_SQUARE+LEN_SQUARE)**2:
        screen_pos=(W/2-(Robot.pos[0]-tile_souris[0]),H/2-(Robot.pos[1]-tile_souris[1]))
        pygame.draw.rect(screen,"red",(screen_pos[0],screen_pos[1],LEN_SQUARE,LEN_SQUARE),2)

    # print(Robot.pos)
    Robot.do_all(keys,dt,screen,Actual_map)
    pygame.display.flip()
    if time.time()-time_0 > dt:
        print(" OH SHIT", time.time()-time_0- dt)
    # print(time.time()-time_0- dt)
    dt = clock.tick(120) / 1000

pygame.quit()