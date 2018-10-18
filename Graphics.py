import pygame
import os
import Variables
import Classes
import Functions

_image_library = {}
def get_image(path):
    global _image_library
    image = _image_library.get(path)
    if image == None:
        canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
        image = pygame.image.load(canonicalized_path)
        _image_library[path] = image
    return image


def graphics(screen, font):
    for i in range(Variables.graphic_width):  # Graphics
        for j in range(Variables.graphic_height):
            place = Variables.graphic_board[j][i]
            if len(place.areas) > 0:  # area color
                team_1_areas = 0
                team_2_areas = 0
                for area in place.areas:
                    if area.character.team == Variables.team_1:
                        team_1_areas += 1
                    elif area.character.team == Variables.team_2:
                        team_2_areas += 1

                    if team_1_areas > 0 and team_2_areas > 0:
                        tile = get_image('Spel sprites/area_purple.png')
                    elif team_1_areas > 0 and team_2_areas == 0:
                        tile = get_image('Spel sprites/area_blue.png')
                    elif team_1_areas == 0 and team_2_areas > 0:
                        tile = get_image('Spel sprites/area_red.png')

            elif place.is_target:
                tile = get_image('Spel sprites/area_purple.png')

            else:
                tile = get_image('Spel sprites/tile.png')

            tile = pygame.transform.scale(tile, (100, 100))
            screen.blit(tile, (60 + i * 100, 40 + j * 100))

            if place.is_cover:
                cover = get_image('Spel sprites/cover_' + str(place.health) + '.png')
                cover = pygame.transform.scale(cover, (100, 100))
                screen.blit(cover, (60 + i * 100, 40 + j * 100))

            if place.is_capture_point:
                capture_point = get_image('Spel sprites/capture_point.png')
                capture_point = pygame.transform.scale(capture_point, (100, 100))
                screen.blit(capture_point, (60 + i * 100, 40 + j * 100))

            if place.is_in_range:
                target = get_image('Spel sprites/targetable.png')
                target = pygame.transform.scale(target, (100, 100))
                screen.blit(target, (60 + i * 100, 40 + j * 100))

                if int(place.required_stamina) > 0 and not Variables.current_character.is_shooting:
                    required_stamina = font.render(str(place.required_stamina), True, (0, 128, 0))
                    screen.blit(required_stamina, (90 + i * 100, 60 + j * 100))

            if type(place.character) == Classes.Character:
                capture_point = get_image('Spel sprites/character_' + str(place.character.team.team) + '.png')
                capture_point = pygame.transform.scale(capture_point, (100, 100))
                screen.blit(capture_point, (60 + i * 100, 40 + j * 100))
                if place.character.has_shield:
                    shield = get_image('Spel sprites/shield.png')
                    shield = pygame.transform.scale(shield, (100, 100))
                    screen.blit(shield, (60 + i * 100, 40 + j * 100))

    if Variables.current_team.team == 1:
        color = (25, 40, 150)
    else:
        color = (150, 25, 25)

    pygame.draw.circle(screen, color, (Variables.end_turn_button.center_x, Variables.end_turn_button.center_y), Variables.end_turn_button.radius + 20)

    for button in Variables.all_buttons:
        if button.is_active:
            button.draw_self(screen)

    screen.blit(font.render(str(Variables.current_team.stamina), True, (255, 255, 255)), (Variables.end_turn_button.center_x - 20 * len(str(Variables.current_team.stamina)), Variables.end_turn_button.center_y - 30))

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP] and Variables.camera_movement_y - 1 >= 0:
        Variables.camera_movement_y -= 1
    if pressed[pygame.K_DOWN] and Variables.camera_movement_y + 1 <= Variables.board_height - Variables.graphic_height:
        Variables.camera_movement_y += 1
    if pressed[pygame.K_LEFT] and Variables.camera_movement_x - 1 >= 0:
        Variables.camera_movement_x -= 1
    if pressed[pygame.K_RIGHT] and Variables.camera_movement_x + 1 <= Variables.board_width - Variables.graphic_width:
        Variables.camera_movement_x += 1

