import pygame as pg
from math import cos, sin, radians


def draw_table(rad, num, size):
    pg.draw.circle(screen, color, (width // 2, height // 2), radius, 1)
    for i in range(360):
        x = int(-cos(radians(i)) * radius) + height // 2
        y = int(sin(radians(i)) * radius) + height // 2
        x_2 = int(-cos(radians(i * number)) * radius) + height // 2
        y_2 = int(sin(radians(i * number)) * radius) + height // 2
        pg.draw.line(screen, color, (x, y), (x_2, y_2))


pg.init()
color = pg.Color(255, 255, 255)
number = 1.0
step = 0.0008
width, height = 2000, 2000
radius = 300
screen = pg.display.set_mode((width, height))
draw_table(radius, number, height)
animated = False


running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                animated = False if animated else True
            if event.key == pg.K_f:
                step *= -1
            if event.key == pg.K_UP:
                step *= 10
            if event.key == pg.K_DOWN:
                step /= 10
            if event.key == pg.K_r:
                step = 0.0008

        if event.type == pg.MOUSEBUTTONDOWN and not animated:
            screen.fill((0, 0, 0))
            number = number + 1 if event.button == 1 else number - 1
            number = int(number)
            draw_table(radius, number, height)
            print(number)

    if animated:
        screen.fill((0, 0, 0))
        draw_table(radius, number, height)
        number += step
        color.hsva = (abs(sin(number)) * 360, 100, 100, 100)

    pg.display.flip()

pg.quit()
