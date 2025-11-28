# Example file showing a circle moving on screen
import pygame # python3 -m pip install -U pygame --user

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

button_rect = pygame.Rect(300, 250, 200, 80)
font = pygame.font.Font(None, 36)

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
DARK_BLUE = (0, 0, 200)

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
    screen.fill("purple")


    pygame.draw.rect(screen, BLUE, button_rect)
    text = font.render("Jouer", True, WHITE)
    screen.blit(text, (button_rect.x + 50, button_rect.y + 25))
    
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