#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame as pg

from code.Const import ENTITY_SPEED, PLAYER_KEY_UP, PLAYER_KEY_DOWN, PLAYER_KEY_RIGHT, PLAYER_KEY_LEFT
from code.Entity import Entity


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    # Usar ELIF somente pode ir a uma direção por vez. Com if pode apertar 2 teclas simultâneas
    def move(self, ):
        pressedKey = pg.key.get_pressed()
        if pressedKey[PLAYER_KEY_UP[self.name]] and self.rect.top > 5:
            self.rect.centery -= ENTITY_SPEED[self.name]

        if pressedKey[PLAYER_KEY_DOWN[self.name]] and self.rect.bottom < 319:
            self.rect.centery += ENTITY_SPEED[self.name]

        if pressedKey[PLAYER_KEY_RIGHT[self.name]] and self.rect.right < 574:
            self.rect.centerx += 1.5

        if pressedKey[PLAYER_KEY_LEFT[self.name]] and self.rect.right > 100:
            self.rect.centerx -= 3.5
