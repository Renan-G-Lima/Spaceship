import pygame as pg

print('game start')
pg.init()
screen = pg.display.set_mode(size=(650, 450))
print('game end')

print('game loop start')
while True:
    # Check for all events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()  # Close window
            quit()  # end pygame
