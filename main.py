# Example file showing a circle moving on screen
import pygame # python3 -m pip install -U pygame --user
from fenetre_dialogue import Dialogue
import os 

# Chemins
main_dir = os.path.split(os.path.abspath(__file__))[0]
assets_dir = os.path.join(main_dir,"assets")
police_dir = os.path.join(assets_dir,"polices")
sounds_dir = os.path.join(assets_dir, "sounds")

# pygame setup
pygame.init()
pygame.font.init()
pygame.mixer.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

# Variables fade
fade_alpha = 255 
fade_speed = 1
fade_active = True
timer = 100

# Variables dialogue
objects = []
counter = 0
speed = 4
done = False
active_message = 0
dialogue_box = True

# Chargement des assets
dialogue_image = pygame.image.load(os.path.join(assets_dir, "dialogue_box.png"))
police_dialogue_path = os.path.join(police_dir, "police_dialogue.ttf")
dialogue_sounds_path = os.path.join(sounds_dir, "typewriter.mp3")
text_sound = pygame.mixer.Sound(dialogue_sounds_path)
text_sound.set_volume(1)

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
fade_alpha = 255 
fade_speed = 1    
fade_active = True
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
timer = 100



while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("black")
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
        
    if fade_active:
        if timer > 0 :
            screen.fill ((0,0,0))
            timer -=1
        else :
            fade_alpha -= fade_speed 
            if fade_alpha <= 0:
                fade_alpha = 0
                fade_active = False
  

    fade_surface = pygame.Surface((1280, 720))
    fade_surface.set_alpha(fade_alpha)
    fade_surface.fill((0, 0, 0))  
    screen.blit(fade_surface, (0, 0))
    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000


pygame.quit()