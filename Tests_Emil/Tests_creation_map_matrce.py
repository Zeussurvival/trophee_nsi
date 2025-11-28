import numpy as np
import pygame
import sys
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

print(sys.executable)
pygame.display.init()
pygame.font.init()

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0



def creation_map_rectangle(width,height):
    Map = np.zeros((width,height), dtype=np.uint32)
    return Map

map123 = creation_map_rectangle(10,10)
# print(map123[-2::5,...])


house_matrice = np.array([[3,4,5,6],
                         [7,8,9,18],
                         [17,16,15,14],])
def place_house(matrice,house_matrice,positions):
    for x in range(house_matrice.shape[0]):
        for y in range(house_matrice.shape[1]):
            print([positions[0]+x,positions[1]+y])
            matrice[positions[0]+x,positions[1]+y] = house_matrice[x,y]
    return matrice
map123 = place_house(map123,house_matrice,(2,2))
print(map123)

# x = np.arange(36).reshape(6, 6)
# print(x[4::-2,...])

# for a in range(len(x)):
#     for y in range(len(x[a])):
#             print(x[a,y],(a,y))





while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255,130,150))
    pygame.display.flip()
    dt = clock.tick(60) / 1000


pygame.quit()