# Example file showing a circle moving on screen
import pygame # python3 -m pip install -U pygame --user
import os
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

main_dir = os.path.split(os.path.abspath(__file__))[0]
assets_dir = os.path.join(main_dir,"assets")
hologram_dir = os.path.join(assets_dir,"1. Free Hologram Interface Wenrexa")
X3_dir = os.path.join(hologram_dir,"Card X3")
button_1 = os.path.join(hologram_dir,"Button 1")

background_original = pygame.image.load(os.path.join(X3_dir,"Card X5.png")).convert_alpha()
background = pygame.transform.scale(background_original,(screen.get_size()))
# pygame setup

button_size = (300, 100)
button_image = pygame.image.load(os.path.join(button_1,"Button Normal.png"))
button_hover = pygame.image.load(os.path.join(button_1,"Button Hover.png"))

button_rect = button_image.get_rect()
button_rect.center = (400, 300)

font = pygame.font.Font(None, 36)


WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
DARK_BLUE = (0, 0, 200)

running = True
dt = 0
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                print("Bouton cliqué !")
    # fill the screen with a color to wipe away anything from last frame
    # screen.fill("purple")
    mouse_pos = pygame.mouse.get_pos()
    mouse_over_button = button_rect.collidepoint(mouse_pos)

    screen.blit(background,(0,0))



    # pygame.draw.rect(screen, BLUE, button_rect)


    screen.blit(button_image, button_rect)

    if mouse_over_button:
        screen.blit(button_hover, button_rect)
    else :
        screen.blit(button_image, button_rect)
    
    text = font.render("Jouer", True, WHITE)
    text_rect = text.get_rect(center=button_rect.center)
    screen.blit(text, text_rect)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        pass
    # flip() the display to put your work on screen

    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000


pygame.quit()