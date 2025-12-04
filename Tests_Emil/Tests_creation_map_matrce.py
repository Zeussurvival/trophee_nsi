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
    Map = np.zeros((width,height), dtype=np.float32)
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
        map_pollu = create_round_matrice(range_pollu)
        # place_matrice_big_then_small(matrice,house_matrice,positions):
        new_map = place_matrice_big_then_small(new_map,map_pollu,pos)
        pass
    return new_map

 
def create_round_matrice(radius):
    matrice = np.zeros((radius*2+1,radius*2+1))
    matrice[radius,radius] = 1
    matrice[radius,radius+2] = 1
    print(matrice.shape[1])
    for x in range(matrice.shape[1]):
        distance_x = radius - x
        # print(distance_x)
        # print(matrice[x])
        for y in range(matrice.shape[0]):
            distance_y = radius - y
            num = min(max(0,1 - (distance_x**2+distance_y**2-1)/(radius**2)),1) #le - 1 permet davoir des contours avec quand meme une certaine valeur
            matrice[x,y]= num # et le min du dessus permet davoir le centre la valeur 1 assez forte
            # print(matrice[x,y])
    return matrice

# mat = create_round_matrice(5)
# for row in mat:
#     print(row)


def set_pollution_map_rectangle(number_of_origins,seed,map,range_pollu):
    Liste_pos = create_random_pos(seed,number_of_origins,map.shape)
    new_map = pollution_creation_rond(Liste_pos,range_pollu,map)
    # print(new_map)
    # print(Liste_pos)
    return new_map

# print(create_random_pos(seed,4,(x_map,y_map)))
# print(map123[-2::5,...])













house_matrice = np.array([[3,4,5,6],
                         [7,8,9,18],
                         [17,16,15,14],])
print(house_matrice)
def place_matrice_big_then_small(matrice,house_matrice,positions):
    for true_y in range(house_matrice.shape[0]):
        for true_x in range(house_matrice.shape[1]):
            print(positions[1]+true_x,matrice.shape[0])
            if 0 < positions[1]+true_x < matrice.shape[0] and 0 < positions[0]+true_y < matrice.shape[1]:
                matrice[positions[1]+true_x,positions[0]+true_y] = house_matrice[true_x,true_y]
    
    return matrice
map123 = place_matrice_big_then_small(map123,house_matrice,(18,18))

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