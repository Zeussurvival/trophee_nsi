# Example file showing a circle moving on screen
import pygame # python3 -m pip install -U pygame --user
import os
from class_dialogue import *


dialogue_1 = Dialogue( 640,600, 894, 200, ["Initialisation…", "Unité de nettoyage autonome : R-0.", "Statut de la planète : inhabitable.", "Mission prioritaire : nettoyer."], next)
message = dialogue_1.dialogue_text[active_message]

while running:
    previous_counter = counter 
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    if counter < speed * len(message) :
        counter +=1
    elif counter >= speed * len(message):
        done = True
        text_sound.stop()
   

    current_char = counter // speed
    previous_char = previous_counter // speed

    # if current_char > previous_char and current_char % 2 == 0 and not done:
    #     text_sound.play()

    if current_char == 1 and previous_char == 0 and not done:
        text_sound.play()

    # if current_char > previous_char and not done:
    #     text_sound.play()
    
    dialogue_1.snip = message[0:counter//speed]

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

    screen.fill("purple")

    pygame.draw.circle(screen, "red", player_pos, 40)

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
    
    if dialogue_box :
        for object in objects:
            object.process()
            object.draw(screen)
        

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000


pygame.quit()