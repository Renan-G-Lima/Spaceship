import pygame as pg

# C
COLOR_YELLOW = (207, 179, 53)
COLOR_WHITE = (255, 255, 255)
COLOR_PURPLE = (89, 0, 161)

# M
MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P - COOPERATIVE',
               'NEW GAME 2P - COMPETITIVE',
               'SCORE',
               'EXIT')

# E
EVENT_ENEMY = pg.USEREVENT + 1
ENTITY_SPEED = {
    'level10': 0,
    'level11': 2,
    'level12': 2,
    'level13': 2,
    'level14': 3,
    'Player1': 3,
    'Player2': 3,
    'Enemy1': 2,
    'Enemy2': 3
}

# P

PLAYER_KEY_UP = {'Player1': pg.K_UP,
                 'Player2': pg.K_w}
PLAYER_KEY_DOWN = {'Player1': pg.K_DOWN,
                 'Player2': pg.K_s}
PLAYER_KEY_LEFT = {'Player1': pg.K_LEFT,
                 'Player2': pg.K_a}
PLAYER_KEY_RIGHT = {'Player1': pg.K_RIGHT,
                 'Player2': pg.K_d}
PLAYER_KEY_SHOOT = {'Player1': pg.K_1,
                 'Player2': pg.K_t}

# S
SPAWN_SHIP = 3500

# W
WIN_WIDTH = 576
WIN_HEIGHT = 324