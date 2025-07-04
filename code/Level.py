#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

import pygame as pg
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import COLOR_PURPLE, WIN_HEIGHT, MENU_OPTION, EVENT_ENEMY, SPAWN_SHIP
from code.Entity import Entity
from code.EntityFactory import EntityFactory


class Level:
    def __init__(self, screen, name, mode_game):
        self.screen = screen
        self.name = name
        self.mode_game = mode_game  # modo de jogo do menu
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('level1'))
        self.entity_list.append(EntityFactory.get_entity('Player1'))
        self.timeout = 20000  # 20s
        if mode_game in [MENU_OPTION[1], MENU_OPTION[2]]:
            self.entity_list.append(EntityFactory.get_entity('Player2'))
        pg.time.set_timer(EVENT_ENEMY, SPAWN_SHIP)

    def run(self, ):
        pg.mixer_music.load(f'./assets/backgroundmusic_lvl1.wav')
        pg.mixer_music.play(-1)
        clock = pg.time.Clock()  # define um fps fixo para rodar na maquina
        while True:
            clock.tick(60)  # define um fps fixo para rodar na maquina
            for ent in self.entity_list:
                self.screen.blit(source=ent.surf, dest=ent.rect)
                ent.move()
            for event in pg.event.get():  # esse evento permite fechar o jogo mesmo após entrar na fase
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()  # sai da janela
                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Enemy1', 'Enemy2')) #randomiza o spawn das naves inimigas
                    self.entity_list.append(EntityFactory.get_entity(choice))

            # texto do level
            self.level_text(20, f'{self.name} - Timeout: {self.timeout / 1000 :.1f}s', COLOR_PURPLE, (10, 5))
            self.level_text(14, f'fps: {clock.get_fps() :.0f}', COLOR_PURPLE, (10, WIN_HEIGHT - 35))
            self.level_text(18, f'Entidades na tela: {len(self.entity_list)}', COLOR_PURPLE, (10, WIN_HEIGHT - 20))
            pg.display.flip()
            pass

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pg.font.SysFont(name="Montserrat", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.screen.blit(source=text_surf, dest=text_rect)
