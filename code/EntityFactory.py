#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Background import Background
from code.Const import WIN_WIDTH


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
        return None
