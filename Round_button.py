import pygame


class RoundButton:
    def __init__(self, radius, center_x, center_y, is_active):
        self.radius = radius
        self.center_x = center_x
        self.center_y = center_y
        self.is_pressed = False
        self.is_active = is_active
        self.is_unavailable = False
        self.color = (100, 100, 100)

    def check_if_pressed(self):
        pressed_mouse = pygame.mouse.get_pressed()
        mouse_pos = pygame.mouse.get_pos()

        if ((self.center_x - mouse_pos[0]) ** 2 + (self.center_y - mouse_pos[1]) ** 2) ** 0.5 <= self.radius:
            if pressed_mouse[0]:
                self.is_pressed = True
            else:
                self.is_pressed = False
        else:
            self.is_pressed = False

    def draw_self(self, screen):
        if self.is_unavailable:
            self.color = (50, 50, 50)
        else:
            self.color = (100, 100, 100)
        pygame.draw.circle(screen, self.color, (self.center_x, self.center_y), self.radius)
