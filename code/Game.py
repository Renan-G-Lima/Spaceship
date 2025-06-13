import pygame as pg
from code.Menu import Menu


class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(size=(650, 450))

    def run(self, ):
        while True:
            menu = Menu(self.screen)
            menu.run()


