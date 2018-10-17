import pygame


class RoundButton:
    def __init__(self, radius, center_x, center_y, is_active):
        self.radius = radius
        self.center_x = center_x
        self.center_y = center_y
        self.is_pressed = False
        self.is_active = is_active
        self.color = (100, 100, 100)

    def check_if_pressed(self):
        pressed_mouse = pygame.mouse.get_pressed()
        mouse_pos = pygame.mouse.get_pos()

        if pressed_mouse[0]:
            if ((self.center_x - mouse_pos[0])**2 + (self.center_y - mouse_pos[1])**2)**0.5 <= self.radius:
                self.is_pressed = True
            else:
                self.is_pressed = False

    def draw_self(self, screen):
        pygame.draw.circle(screen, self.color, (self.center_x, self.center_y), self.radius)
