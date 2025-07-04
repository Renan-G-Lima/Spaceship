#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from code.Background import Background
from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Enemy import Enemy
from code.Player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'level1':
                list_background = []
                for i in range(5):
                    list_background.append(Background(f'level1{i}', (0, 0)))
                    list_background.append(Background(f'level1{i}', (WIN_WIDTH, 0)))
                return list_background
            case 'Player1':
                return Player('Player1', (20, WIN_HEIGHT /5))
            case 'Player2':
                return Player('Player2', (20, WIN_HEIGHT / 2))
            case 'Enemy1':
                return Enemy('Enemy1', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT -20)))
            case 'Enemy2':
                return Enemy('Enemy2', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT -20)))
        return None
