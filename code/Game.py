import pygame as pg

from code.Menu import Menu
from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):

        while True:
            menu = Menu(self.screen)
            menu_return = menu.run()

            if menu_return == MENU_OPTION[0]:
                pass
            elif menu_return == MENU_OPTION[4]:
                pg.quit()  # close the game screen
                quit()  # end game