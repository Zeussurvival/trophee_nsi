# Example file showing a circle moving on screen
import pygame # python3 -m pip install -U pygame --user
import os


main_dir = os.path.split(os.path.abspath(__file__))[0]
assets_dir = os.path.join(main_dir,"assets")
police_dir = os.path.join(assets_dir,"polices")



# pygame setup
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
objects = []
timer = pygame.time.Clock()
counter = 0
speed = 3
done = False

dialogue_image = pygame.image.load(os.path.join(assets_dir, "dialogue_box.png"))
police_dialogue_path = os.path.join(police_dir, "police_dialogue.ttf")


dialogue_box_width = 400
dialogue_box_height = 200
dialogue_box_x = (screen.get_width() - dialogue_box_width) // 2
dialogue_box_y = (screen.get_height() - dialogue_box_height) // 2
dialogue_box = True

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)


class Dialogue():
    def __init__(self, x, y, width, height, dialogue_text="hey", onlickFunction=None, one_press=False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.dialogue_text = dialogue_text
        self.snip = ""
        self.onclickFunction = onlickFunction
        self.one_press = one_press
        self.already_pressed = False

        self.dialogue_rect = pygame.Rect(0, 0, self.width, self.height)
        self.dialogue_rect.center = (x, y)

        self.normal_image = pygame.transform.scale(dialogue_image, (width, height))
        objects.append(self)

        self.font = pygame.font.Font(police_dialogue_path, 25)
        
    def draw(self, screen):
        screen.blit(self.normal_image, self.dialogue_rect)
        text_surface = self.font.render(self.snip, True, (137, 244, 255))
        text_rect = text_surface.get_rect(
            topleft=(self.dialogue_rect.left + 40, self.dialogue_rect.top + 40))
        screen.blit(text_surface, text_rect)

    def process(self):
        if pygame.mouse.get_pressed()[0]:
            if self.dialogue_rect.collidepoint(pygame.mouse.get_pos()):
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


def next():
    print("next")

dialogue_1 = Dialogue( 640,600, 894, 200, "hello tgretf regfeferhy", next)

while running:

    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    if counter < speed * len(dialogue_1.dialogue_text) :
        counter +=1
    elif counter >= speed * len(dialogue_1.dialogue_text):
        done = True
   
    dialogue_1.snip = dialogue_1.dialogue_text[0:counter//speed]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE :
                if dialogue_box:
                    dialogue_box = False


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