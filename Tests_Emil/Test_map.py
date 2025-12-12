import pygame
import numpy
import random
import Test_def as D
import Test_classe as C
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

pygame.display.init()
pygame.font.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
dt = 0

Actual_map = D.creation_map_rectangle(20,20)
Actual_map_pollution = D.set_pollution_map_rectangle(10,10,Actual_map,5)

Actual_map[0,2] = 1
print(Actual_map)

List_tiles = [C.Tile("background_1.png",None,0),C.Tile("background_1.png",None,90),C.Tile("background_1.png",None,180),C.Tile("background_1.png",None,270),\
              C.Tile("background_2.png",None,0),C.Tile("background_2.png",None,90),C.Tile("background_2.png",None,180),C.Tile("background_2.png",None,270)]

for y in range(Actual_map.shape[0]):
    for x in range(Actual_map.shape[1]):
        Actual_map[x,y] = random.randint(0,7)


# Create a surface with per-pixel alpha
carré_pollu = pygame.Surface((100, 100), pygame.SRCALPHA)
# Fill with red and 100 alpha (approximately 40% opacity)


# Position the square
carré_rect = (0,0,16,16)
print(carré_rect[0])
carré_pollu.fill((100, 100, 100, 100))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("purple")

    for y in range(Actual_map.shape[0]):
        for x in range(Actual_map.shape[1]):
            List_tiles[Actual_map[x,y]].blit_self(screen,(x*16,y*16))
            carré_pollu.fill((100, 200, 100,(min(Actual_map_pollution[x,y] *75+20,255)//255)))
            carré_rect = (x*16,y*16,x*16+16,y*16+16)
            # print(Actual_map_pollution[x,y]*75)
            # print(min(Actual_map_pollution[x,y] *75+20,255)//255)
            screen.blit(carré_pollu,carré_rect)

    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()