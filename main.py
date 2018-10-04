import Functions
import Variables
import Classes
import pygame
import os
from random import *

Functions.equip(Variables.A, Classes.BasicWeapon)
Functions.equip(Variables.a, Classes.BasicWeapon)
Functions.equip(Variables.B, Classes.CircleWeapon)
Functions.equip(Variables.a, Classes.CircleWeapon)
Functions.equip(Variables.C, Classes.SniperRifle)
Functions.equip(Variables.c, Classes.SniperRifle)

for i in range(int((Variables.board_height * Variables.board_width)/10)):  # covers
    random_y = randint(1, int(Variables.board_height) - 2)
    random_x = randint(1, int(Variables.board_width) - 2)
    random_number = randint(1, 4)
    Variables.board[random_y][random_x].health = random_number
    Variables.board[random_y][random_x].is_cover = True
    Variables.board[random_y][random_x].is_open = False
    Variables.board[Variables.board_height - random_y - 1][Variables.board_width - random_x - 1].health = random_number
    Variables.board[Variables.board_height - random_y - 1][Variables.board_width - random_x - 1].name = Variables.board[Variables.board_height - random_y][Variables.board_width - random_x].health
    Variables.board[Variables.board_height - random_y - 1][Variables.board_width - random_x - 1].is_cover = True
    Variables.board[Variables.board_height - random_y - 1][Variables.board_width - random_x - 1].is_open = False

for i in range(-1, 2):  # capture points
    for j in range(-1, 2):
        Variables.Variables.board[int(Variables.board_height / 2 + i)][int(Variables.board_width / 2 + j)].is_capture_point = True
        Variables.Variables.board[int(Variables.board_height / 2 + i)][int(Variables.board_width / 2 + j)].is_cover = False
        Variables.Variables.board[int(Variables.board_height / 2 + i)][int(Variables.board_width / 2 + j)].health = 0

# cover_list = [[1, 4], [1, 5], [0, 6]]
# for coordinate in cover_list:
#    cover = Classes.Cover(name=str(random.randint(1, 4)))
#    Functions.placement_swap(cover, coordinate[0], coordinate[-1])

Functions.starting_positions(int(Variables.board_height), int(Variables.board_width))

clock = pygame.time.Clock()

_image_library = {}
def get_image(path):
    global _image_library
    image = _image_library.get(path)
    if image == None:
        canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
        image = pygame.image.load(canonicalized_path)
        _image_library[path] = image
    return image


pygame.init()
screen = pygame.display.set_mode((1920, 1080))
done = False

while not done:
    for team in Variables.teams:
        team.max_stamina = 12
        team.used_stamina = 0

    for character in Variables.current_team.team_members_alive:
        character.has_moved = 0
        character.has_shot = False
        character.has_rushed = False
        character.has_shield = True
        for area in character.weapon.areas:
            character.weapon.areas.remove(area)
        
    if Variables.current_team.team == 1:
        Variables.game_turn += 1
        
    if Variables.current_team.team == 2 and Variables.game_turn == 1:
        Variables.current_team.max_stamina = 15

    while not Variables.current_team.used_stamina < Variables.current_team.max_stamina:
        Variables.current_team.is_current_team = False
        Variables.teams[Variables.teams.index(Variables.current_team) - 1].is_current_team = True
        Variables.current_team = Variables.teams[Variables.teams.index(Variables.current_team) - 1]
        Variables.current_team.check_points()

    Variables.current_team.used_stamina += Functions.turn(Functions.choose_character())

    if Variables.current_team.team == 2 and Variables.game_turn == 1:
        for character in Variables.current_team.team_members_alive:
            character.has_rushed = False

    Functions.win()

    Functions.set_graphic_board()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    for i in range(Variables.graphic_width):  # Graphics
        for j in range(Variables.graphic_height):
            place = Variables.graphic_board[j][i]

            if len(place.areas) > 0:  # area color
                team_1_areas = 0
                team_2_areas = 0
                for area in place.areas:
                    if area.character.team == 1:
                        team_1_areas += 1
                    elif area.character.team == 2:
                        team_2_areas += 1

                    if team_1_areas > 0 and team_2_areas > 0:
                        tile = get_image('Spel sprites/area_purple.png')
                    elif team_1_areas > 0 and team_2_areas == 0:
                        tile = get_image('Spel sprites/area_blue.png')
                    elif team_1_areas == 0 and team_2_areas > 0:
                        tile = get_image('Spel sprites/area_blue.png')
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

            if place.is_walkable:
                target = get_image('Spel sprites/targetable.png')
                target = pygame.transform.scale(target, (100, 100))
                screen.blit(target, (60 + i * 100, 40 + j * 100))

            if type(place.character) == Classes.Character:
                capture_point = get_image('Spel sprites/character_' + str(place.character.team.team) + '.png')
                capture_point = pygame.transform.scale(capture_point, (100, 100))
                screen.blit(capture_point, (60 + i * 100, 40 + j * 100))
                if place.character.has_shield:
                    shield = get_image('Spel sprites/shield.png')
                    shield = pygame.transform.scale(shield, (100, 100))
                    screen.blit(shield, (60 + i * 100, 40 + j * 100))

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP] and Variables.camera_movement_y - 1 >= 0:
        Variables.camera_movement_y -= 1
    if pressed[pygame.K_DOWN] and Variables.camera_movement_y + 1 <= Variables.board_height - Variables.graphic_height:
        Variables.camera_movement_y += 1
    if pressed[pygame.K_LEFT] and Variables.camera_movement_x - 1 >= 0:
        Variables.camera_movement_x -= 1
    if pressed[pygame.K_RIGHT] and Variables.camera_movement_x + 1 <= Variables.board_width - Variables.graphic_width:
        Variables.camera_movement_x += 1

    pygame.display.flip()
    clock.tick(30)

