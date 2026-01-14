# Example file showing a circle moving on screen
import pygame # python3 -m pip install -U pygame --user

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0



dialogue_box_width = 400
dialogue_box_height = 200
dialogue_box_x = (screen.get_width() - dialogue_box_width) // 2
dialogue_box_y = (screen.get_height - dialogue_box_height) // 2
dialogue_box = False

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)


class Dialogue():
    def __init__(self, x, y, width, height, dialogue_text="hey", onlickFunction=None, one_press=False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onclickFunction = onlickFunction
        self.one_press = one_press
        self.already_pressed = False

        self.dialogue_rect = pygame.Rect(0, 0, self.width, self.height)
        self.dialogue_rect.center = (x, y)


        self.normal_image = pygame.transform.scale(dialogue_image, (width, height))

    def process(self):
        if pygame.mouse.get_pressed():
            if self.one_press :
                self.onclickFunction()
            elif not self.already_pressed:
                self.onclickFunction()
                self.already_pressed = True
            else :
                self.already_pressed = True
        else :
            self.already_pressed = False






def open_dialogue_box ():
    global dialogue_box
    dialogue_box = True

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