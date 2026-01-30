# Example file showing a circle moving on screen
import pygame # python3 -m pip install -U pygame --user
import os 
import classe_dialogue as C_D


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
timer = 25

# Variables dialogue

counter = 0
speed = 4
done = False
active_message = 0
dialogue_box = True

# Chargement des assets

dialogue_sounds_path = os.path.join(sounds_dir, "typewriter.mp3")
text_sound = pygame.mixer.Sound(dialogue_sounds_path)
text_sound.set_volume(1)


player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)




main_dir = os.path.split(os.path.abspath(__file__))[0]
assets_dir = os.path.join(main_dir,"assets")
police_dir = os.path.join(assets_dir,"polices")
sounds_dir = os.path.join(assets_dir, "sounds")


objects = C_D.objects
counter = 0
speed = 4
done = False
active_message = 0


dialogue_image = pygame.image.load(os.path.join(assets_dir, "dialogue_box.png"))
police_dialogue_path = os.path.join(police_dir, "police_dialogue.ttf")
dialogue_sounds_path = os.path.join(sounds_dir, "typewriter.mp3")
text_sound = pygame.mixer.Sound(dialogue_sounds_path)
text_sound.set_volume(1)

dialogue_box_width = 400
dialogue_box_height = 200
dialogue_box_x = (screen.get_width() - dialogue_box_width) // 2
dialogue_box_y = (screen.get_height() - dialogue_box_height) // 2
dialogue_box = True

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)






dialogue_1 = C_D.Dialogue( 640,600, 894, 200, ["Initialisation…", "Unité de nettoyage autonome : R-0.", "Statut de la planète : inhabitable.", "Mission prioritaire : nettoyer."], next)
message = dialogue_1.dialogue_text[active_message]


while running:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == (pygame.K_SPACE or pygame.K_RETURN):
                if done :
                    if active_message < len(dialogue_1.dialogue_text) - 1:
                        active_message += 1
                        done = False
                        message = dialogue_1.dialogue_text[active_message]
                        counter = 0
                        text_sound.stop()
                    else :
                        dialogue_box = False
                        text_sound.stop()                        
                else:
                    counter = speed * len(message)
                    done = True
                    text_sound.stop() 
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    pygame.draw.circle(screen, "red", player_pos, 40)

       
    if fade_active:
        if timer > 0 :
            screen.fill ((0,0,0))
            timer -=1
        else :
            fade_alpha -= fade_speed 
            if fade_alpha <= 0:
                fade_alpha = 0
                fade_active = False
                print("fade finis")
    else :
        if dialogue_box :
            for object in objects:

                object.process()
                object.draw(screen)

    fade_surface = pygame.Surface((1280, 720))
    fade_surface.set_alpha(fade_alpha)
    fade_surface.fill((0, 0, 0))  
    screen.blit(fade_surface, (0, 0))

    previous_counter = counter 
    if counter < speed * len(message) :
        counter +=1
    elif counter >= speed * len(message):
        done = True
        text_sound.stop()

    current_char = counter // speed
    previous_char = previous_counter // speed

    if current_char == 1 and previous_char == 0 and not done:
        text_sound.play()
    
    dialogue_1.snip = message[0:counter//speed]

    if dialogue_box == False :
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