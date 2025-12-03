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
        matrice_for_pos = circle_gradient_matrix(range_pollu)

        haut,long = new_map.shape
        ha_p,lo_p = range_pollu*2+1,range_pollu*2+1
        for y in range(ha_p):
            for x in range(lo_p):
                y_actu = pos[1] + y
                x_actu = pos[1] + x

                if 0 <= x_actu < long and 0 <= y_actu < haut:
                    new_map[y_actu,x_actu] += matrice_for_pos[y_actu,x_actu]

# print(create_random_pos(seed,4,(x_map,y_map)))
# print(map123[-2::5,...])


def circle_gradient_matrix(radius): # fait par gpt parce que flm de refaire les ronds en pixel chef
    diameter = radius * 2
    mat = np.zeros((diameter+1, diameter+1), dtype=np.float32)
    circle_x, circle_y = radius, radius  # centre

    for y in range(diameter + 1):
        for x in range(diameter + 1):
            distance_x = x - circle_x
            dy = y - circle_y
            distance = (distance_x**2 + dy**2)**0.5  # distance euclidienne
            if distance <= radius:
                mat[y, x] = 1 - distance/radius
            else:
                mat[y, x] = 0
    return mat

# Exemple pour radius=3
mat = circle_gradient_matrix(3)

def set_pollution_map_rectangle(number_of_origins,seed,map,range_pollu):
    Liste_pos = create_random_pos(seed,number_of_origins,map.shape)
    new_map = pollution_creation_rond(Liste_pos,range_pollu,map)
    # print(new_map)
    # print(Liste_pos)
    return new_map

for row in mat:
    print(row)

map_pollu = set_pollution_map_rectangle(4,seed,map123,5)









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