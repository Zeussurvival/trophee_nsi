import numpy as np
import pygame
import sys
import winreg
import random
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

x_map = 20
y_map = 20
seed = 25


def creation_map_rectangle(width,height):
    Map = np.zeros((width,height), dtype=np.uint32)
    return Map

map123 = creation_map_rectangle(x_map,y_map)

def create_random_pos(seed,numbers_to_gen,map_length):
    random.seed(seed)
    map_total = map_length[0] * map_length[1]
    Liste_n = []
    for _ in range(numbers_to_gen):
        num = int(random.random()*map_total)
        Liste_n.append((num // map_length[0],num % map_length[0]))
    return Liste_n

def pollution_creation_rond(Liste_pos,range_pollu,map): # pas forcement realiste au top mais bon
    new_map = np.zeros(map.shape)
    for pos in Liste_pos:
        new_map[pos[1],pos[0]] = 1
    
    for x in range(map.shape[0]):
        for y in range(map.shape[1]):
            pos = x,y

# print(create_random_pos(seed,4,(x_map,y_map)))

def set_pollution_map_rectangle(number_of_origins,seed,map,range_pollu):
    Liste_pos = create_random_pos(seed,number_of_origins,map.shape)
    new_map = pollution_creation_rond(Liste_pos,range_pollu,map)
    print(new_map)
    print(Liste_pos)
    return Liste_pos

set_pollution_map_rectangle(4,seed,map123,5)

# print(map123[-2::5,...])


house_matrice = np.array([[3,4,5,6],
                         [7,8,9,18],
                         [17,16,15,14],])
def place_house(matrice,house_matrice,positions):
    for x in range(house_matrice.shape[0]):
        for y in range(house_matrice.shape[1]):
            matrice[positions[0]+x,positions[1]+y] = house_matrice[x,y]
    return matrice
map123 = place_house(map123,house_matrice,(2,2))


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