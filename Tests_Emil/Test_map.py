import pygame
import numpy
import random
import Test_def as D
import Test_classe_tile as CT
import Test_classe_humain as CH
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
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
dt = 0

Actual_map = D.creation_map_rectangle(20,20)
Actual_map_pollution = D.set_pollution_map_rectangle(10,10,Actual_map,5)

Actual_map[0,2] = 1
print(Actual_map)

List_tiles = [CT.Tile("background_1.png",None,0),CT.Tile("background_1.png",None,90),CT.Tile("background_1.png",None,180),CT.Tile("background_1.png",None,270),\
              CT.Tile("background_2.png",None,0),CT.Tile("background_2.png",None,90),CT.Tile("background_2.png",None,180),CT.Tile("background_2.png",None,270),\
              ]

for y in range(Actual_map.shape[0]):
    for x in range(Actual_map.shape[1]):
        Actual_map[x,y] = random.randint(0,7)
print(Actual_map_pollution)


Robot = CH.Humanoid("robot_front_wait.png",["robot_front_walking.png"])

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("purple")
    keys = pygame.key.get_pressed()

    for y in range(Actual_map.shape[0]):
        for x in range(Actual_map.shape[1]):
            List_tiles[Actual_map[x,y]].blit_self(screen,(x*64,y*64))

    Robot.do_movement_by_self(keys,dt,screen)
    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()