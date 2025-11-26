# Example file showing a circle moving on screen
import pygame # python3 -m pip install -U pygame --user
import numpy
# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)








# Map_tiles = np.array([[13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13],
#                       [13,13, 4, 7,13,13,13,13,13,13,13,13,13,13,13,13],
#                       [13,13, 0, 2,13,13,13,18,13,13,13,13,13,13,13,13],
#                       [13,13, 0, 2,13,13,13,17,13,13,13,13,13,13,13,13],
#                       [13, 4, 8, 2,13,13,13,16,13,13,13,13,13,13,13,13],
#                       [13, 0,14,11, 3, 3,13,15,13,13,13,13,13,13,13,13],
#                       [13, 0,14,14,13,12,13,13,13,13,13,13,13,13,13,13],
#                       [13, 0,14,14,13,12,13,13,13,13,13,13,13,13,13,13],
#                       [13, 0,14,14,13,13,13,13,13,13,13,13,13,13,13,13],
#                       [13, 0,13,13,13,13,13,13,13,13,13,13,13,13,13,13],
#                       [13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13],
#                       [13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13],
#                       [13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13],
#                       [13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13],
#                       [13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13],
#                       [13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13]])


# Map_collision = np.zeros(Map_tiles.shape)
# Map_collision[5,7] = 1 
# print(Map_collision)

# list_loaded_tiles = [T.Road(None,"Road_0.png",0),T.Road(None,"Road_0.png",90),T.Road(None,"Road_0.png",180),T.Road(None,"Road_0.png",270),\
#     T.Road(None,"Road_coin_1.png",0),T.Road(None,"Road_coin_1.png",90),T.Road(None,"Road_coin_1.png",180),T.Road(None,"Road_coin_1.png",270),\
#     T.Road(None,"Road_anticoin_1.png",0),T.Road(None,"Road_anticoin_1.png",90),T.Road(None,"Road_anticoin_1.png",180),T.Road(None,"Road_anticoin_1.png",270),\
#     T.Grass(None,"Grass_0.png",0),\
#     T.Grass(None,"Grass_01.png",0),\
#     T.Road(None,"Road_empty_1.png",0),\
#     T.Tree(None,"Grass_1.png","Tree_1_bottom.png",0),T.Tree(None,"Grass_1.png","Tree_1.png",0),T.Tree(None,"Grass_1.png","Tree_1_top.png",0),T.Tree(None,"Grass_1.png","Tree_1_leaves_1.png",0),\
#             ]

#     for i in range(len(Map_tiles)):
#         for b in range(len(Map_tiles[i])):
#                 # pygame.draw.rect(screen,"green",(b*16,i*16,16,16))
#                 # screen.blit(list_loaded_tiles[Map_tiles[i,b]].image,(b*16*GLOBAL_ZOOM,i*16*GLOBAL_ZOOM))
#                 tuty = 2*16*GLOBAL_X_SIZE
#                 list_loaded_tiles[Map_tiles[i,b]].draw_self(screen,(b-Human1.pos[0]+S_WIDTH/(tuty),i-Human1.pos[1]+S_HEIGHT/(tuty)),(GLOBAL_X_SIZE,GLOBAL_Y_SIZE))
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    pygame.draw.circle(screen, "red", player_pos, 40)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_z]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_q]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000


pygame.quit()