import pygame as pg
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import COLOR_YELLOW, COLOR_WHITE
from code.Const import MENU_OPTION
from code.Const import WIN_WIDTH


class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.surf = pg.image.load('./assets/MenuInicial.png')
        self.rectangle = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        pg.mixer_music.load('./assets/music_menu.wav')
        pg.mixer_music.play(-1)

        while True:
            self.screen.blit(source=self.surf, dest=self.rectangle)
            self.text_menu(55, "WAR", COLOR_YELLOW, ((WIN_WIDTH / 2), 70))
            self.text_menu(45, "of", COLOR_YELLOW, ((WIN_WIDTH / 2), 98))
            self.text_menu(60, "Spaceships", COLOR_YELLOW, ((WIN_WIDTH / 2), 120))


            for i in range(len(MENU_OPTION)):
                self.text_menu(20, MENU_OPTION[i], COLOR_WHITE, ((WIN_WIDTH / 2), 195 + 23 * i))

            pg.display.flip()

            # checking all events for we can closed window
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()  # close the game screen
                    quit()  # end game

    def text_menu(self, text_size: int, text: str, text_color: tuple, text_center_position: tuple):
        text_font: Font = pg.font.SysFont(name="Montserrat", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_position)
        self.screen.blit(source=text_surf, dest=text_rect)
