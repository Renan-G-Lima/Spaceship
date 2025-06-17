import pygame as pg

from code.Menu import Menu
from code.Const import WIN_WIDTH, WIN_HEIGHT


class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):

        while True:
            menu = Menu(self.screen)
            menu.run()


