import pygame


class SquareButton:
    def __init__(self, start_x, end_x, start_y, end_y, is_active):
        self.start_x = start_x
        self.end_x = end_x
        self.start_y = start_y
        self.end_y = end_y
        self.is_pressed = False
        self.is_active = is_active
        self.is_unavailable = False
        self.color = (100, 100, 100)

    def check_if_pressed(self):
        pressed_mouse = pygame.mouse.get_pressed()
        mouse_pos = pygame.mouse.get_pos()

        if self.start_x < mouse_pos[0] <= self.end_x and self.start_y < mouse_pos[1] <= self.end_y:
            if pressed_mouse[0]:
                self.is_pressed = True
            else:
                self.is_pressed = False
        else:
            self.is_pressed = False

    def draw_self(self, screen):
        print(self.is_unavailable)
        if self.is_unavailable:
            self.color = (50, 50, 50)
        else:
            self.color = (100, 100, 100)
        pygame.draw.rect(screen, self.color, pygame.Rect(self.start_x, self.start_y, self.end_x - self.start_x, self.end_y - self.start_y))
