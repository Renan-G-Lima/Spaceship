#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame as pg

from code.Entity import Entity
from code.EntityFactory import EntityFactory


class Level:
    def __init__(self, screen, name, mode_game):
        self.screen = screen
        self.name = name
        self.mode_game = mode_game  # modo de jogo do menu
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('level1'))

    def run(self, ):
        while True:
            for ent in self.entity_list:
                self.screen.blit(source=ent.surf, dest=ent.rect)
                ent.move()
            pg.display.flip()
        pass
