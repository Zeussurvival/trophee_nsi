import pygame

class Button():
    def __init__(self, screen, button_image, button_hover, button_click, font, x, y, width, height, buttonText='Button', onclickFunction=None, onePress=False, icon=None, icon_only=False):
        self.screen = screen
        self.button_image = button_image
        self.button_hover = button_hover
        self.button_click = button_click
        self.font = font
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onclickFunction = onclickFunction
        self.onePress = onePress
        self.alreadyPressed = False
        self.icon = icon
        self.icon_only = icon_only
    
        if not icon_only:
            self.normal_image = pygame.transform.scale(button_image, (width, height))
            self.hover_image = pygame.transform.scale(button_hover, (width, height))
            self.pressed_image = pygame.transform.scale(button_click, (width, height))

        self.buttonRect = pygame.Rect(0, 0, self.width, self.height)
        self.buttonRect.center = (x, y)
        
        self.buttonSurf = self.font.render(buttonText, True, (255, 255, 255))

    def process(self):
        mousePos = pygame.mouse.get_pos()

        if self.buttonRect.collidepoint(mousePos):
            if not self.icon_only:
                self.screen.blit(self.pressed_image, self.buttonRect)
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                if not self.icon_only:
                    self.screen.blit(self.pressed_image, self.buttonRect)
                if self.onePress:
                    self.onclickFunction()
                elif not self.alreadyPressed:
                    self.onclickFunction()
                    self.alreadyPressed = True
            else:
                if not self.icon_only:
                    self.screen.blit(self.hover_image, self.buttonRect)
                self.alreadyPressed = False
        else:
            if not self.icon_only:
                self.screen.blit(self.normal_image, self.buttonRect)
            self.alreadyPressed = False 

        if self.icon:
            if self.icon_only:
                icon_rect = self.icon.get_rect(center=self.buttonRect.center)
                self.screen.blit(self.icon, icon_rect)
            else:    
                icon_rect = self.icon.get_rect()
                total_width = self.buttonSurf.get_width() + 15 + icon_rect.width       
            
                text_rect = self.buttonSurf.get_rect()
                text_rect.center = (self.buttonRect.centerx - total_width // 2 + self.buttonSurf.get_width() // 2, self.buttonRect.centery)
                
                icon_rect.midleft = (text_rect.right + 15, self.buttonRect.centery)

                self.screen.blit(self.buttonSurf, text_rect)
                self.screen.blit(self.icon, icon_rect)
        else:
            text_rect = self.buttonSurf.get_rect(center=self.buttonRect.center)
            self.screen.blit(self.buttonSurf, text_rect) 


class Settings_Button():
    def __init__(self, screen, button_image, button_hover, button_click, font, x, y, width, height, buttonText='Button', onclickFunction=None, onePress=False, icon=None, icon_only=False):
        self.screen = screen
        self.button_image = button_image
        self.button_hover = button_hover
        self.button_click = button_click
        self.font = font
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onclickFunction = onclickFunction
        self.onePress = onePress
        self.alreadyPressed = False
        self.icon = icon
        self.icon_only = icon_only
    
        if not icon_only:
            self.normal_image = pygame.transform.scale(button_image, (width, height))
            self.hover_image = pygame.transform.scale(button_hover, (width, height))
            self.pressed_image = pygame.transform.scale(button_click, (width, height))

        self.buttonRect = pygame.Rect(0, 0, self.width, self.height)
        self.buttonRect.center = (x, y)
        
        self.buttonSurf = self.font.render(buttonText, True, (255, 255, 255))
        
    def process(self):
        mousePos = pygame.mouse.get_pos()

        if self.buttonRect.collidepoint(mousePos):
            if not self.icon_only:
                self.screen.blit(self.pressed_image, self.buttonRect)
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                if not self.icon_only:
                    self.screen.blit(self.pressed_image, self.buttonRect)
                if self.onePress:
                    self.onclickFunction()
                elif not self.alreadyPressed:
                    self.onclickFunction()
                    self.alreadyPressed = True
            else:
                if not self.icon_only:
                    self.screen.blit(self.hover_image, self.buttonRect)
                self.alreadyPressed = False
        else:
            if not self.icon_only:
                self.screen.blit(self.normal_image, self.buttonRect)
            self.alreadyPressed = False 

        if self.icon:
            if self.icon_only:
                icon_rect = self.icon.get_rect(center=self.buttonRect.center)
                self.screen.blit(self.icon, icon_rect)
            else:    
                icon_rect = self.icon.get_rect()
                total_width = self.buttonSurf.get_width() + 15 + icon_rect.width       
            
                text_rect = self.buttonSurf.get_rect()
                text_rect.center = (self.buttonRect.centerx - total_width // 2 + self.buttonSurf.get_width() // 2, self.buttonRect.centery)
                
                icon_rect.midleft = (text_rect.right + 15, self.buttonRect.centery)

                self.screen.blit(self.buttonSurf, text_rect)
                self.screen.blit(self.icon, icon_rect)
        else:
            text_rect = self.buttonSurf.get_rect(center=self.buttonRect.center)
            self.screen.blit(self.buttonSurf, text_rect) 


class Music_Button():
    def __init__(self, screen, button_image, button_hover, button_click, font, x, y, width, height, buttonText='Button', onclickFunction=None, onePress=False, icon=None, icon_only=False):
        self.screen = screen
        self.button_image = button_image
        self.button_hover = button_hover
        self.button_click = button_click
        self.font = font
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onclickFunction = onclickFunction
        self.onePress = onePress
        self.alreadyPressed = False
        self.icon = icon
        self.icon_only = icon_only
    
        if not icon_only:
            self.normal_image = pygame.transform.scale(button_image, (width, height))
            self.hover_image = pygame.transform.scale(button_hover, (width, height))
            self.pressed_image = pygame.transform.scale(button_click, (width, height))

        self.buttonRect = pygame.Rect(0, 0, self.width, self.height)
        self.buttonRect.center = (x, y)
        
        self.buttonSurf = self.font.render(buttonText, True, (255, 255, 255))
        
    def process(self):
        mousePos = pygame.mouse.get_pos()

        if self.buttonRect.collidepoint(mousePos):
            if not self.icon_only:
                self.screen.blit(self.pressed_image, self.buttonRect)
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                if not self.icon_only:
                    self.screen.blit(self.pressed_image, self.buttonRect)
                if self.onePress:
                    self.onclickFunction()
                elif not self.alreadyPressed:
                    self.onclickFunction()
                    self.alreadyPressed = True
            else:
                if not self.icon_only:
                    self.screen.blit(self.hover_image, self.buttonRect)
                self.alreadyPressed = False
        else:
            if not self.icon_only:
                self.screen.blit(self.normal_image, self.buttonRect)
            self.alreadyPressed = False 

        if self.icon:
            if self.icon_only:
                icon_rect = self.icon.get_rect(center=self.buttonRect.center)
                self.screen.blit(self.icon, icon_rect)
            else:    
                icon_rect = self.icon.get_rect()
                total_width = self.buttonSurf.get_width() + 15 + icon_rect.width       
            
                text_rect = self.buttonSurf.get_rect()
                text_rect.center = (self.buttonRect.centerx - total_width // 2 + self.buttonSurf.get_width() // 2, self.buttonRect.centery)
                
                icon_rect.midleft = (text_rect.right + 15, self.buttonRect.centery)

                self.screen.blit(self.buttonSurf, text_rect)
                self.screen.blit(self.icon, icon_rect)
        else:
            text_rect = self.buttonSurf.get_rect(center=self.buttonRect.center)
            self.screen.blit(self.buttonSurf, text_rect)