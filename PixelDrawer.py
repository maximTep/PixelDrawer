import pygame
import math

W = 300
H = 300

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


pygame.init()
screen = pygame.display.set_mode([W, H])
pygame.display.set_caption('Drawer')
clock = pygame.time.Clock()


def multiply(a, mult: float):
    rez = []
    for i in range(len(a)):
        rez.append(a[i] * mult)
    return rez


def mid_color(col1, col2):
    return col1[0] + col2[0] / 2, col1[1] + col2[1] / 2, col1[2] + col2[2] / 2


def fade(col1, col2, cnt):
    colorRange = []
    for i in range(cnt):
        colorRange.append(mid_color(multiply(col2, (i/cnt)**1), multiply(col1, 1 - (i/cnt)**1)))
    return colorRange


def fade_circle(surface, center, radius, col):
    new_surface = pygame.surface.Surface([2 * radius, 2 * radius])
    for i in reversed(range(0, radius, 1)):
        new_surface.fill(WHITE)
        new_surface.set_alpha(255 * (1 - i / len(range(0, radius)))**4)
        new_surface.set_colorkey(WHITE)
        pygame.draw.circle(new_surface, col, [radius, radius], i)
        screen.blit(new_surface, [center[0] - radius, center[1] - radius])


def circle(surface, center, radius, col):
    pygame.draw.circle(surface, col, center, radius)


def whiten(grid, pos, val):
    x, y = pos
    try:
        if grid[y][x + 1] + val >= 1:
            grid[y][x+1] = 1
        else:
            grid[y][x+1] += val
    except:
        pass


def pixel_circle(grid, center, radius=3):
    x, y = center
    x -=1
    n = len(grid)
    m = len(grid[0])
    add1 = 0.2
    add2 = 0.1
    add3 = 0.05
    whiten(grid, [x, y], 0.3)
    whiten(grid, [x+1, y], add1)
    whiten(grid, [x+2, y], add3)
    whiten(grid, [x, y+1], add1)
    whiten(grid, [x, y+2], add3)
    whiten(grid, [x - 1, y], add1)
    whiten(grid, [x - 2, y], add3)
    whiten(grid, [x, y - 1], add1)
    whiten(grid, [x, y - 2], add3)
    whiten(grid, [x+1, y+1], add2)
    whiten(grid, [x+1, y-1], add2)
    whiten(grid, [x-1, y+1], add2)
    whiten(grid, [x-1, y-1], add2)


def small_pixel_circle(grid, center, radius=3):
    x, y = center
    x -=1
    n = len(grid)
    m = len(grid[0])
    add1 = 0.05
    whiten(grid, [x, y], 0.2)
    whiten(grid, [x+1, y], add1)
    whiten(grid, [x, y+1], add1)
    whiten(grid, [x - 1, y], add1)
    whiten(grid, [x, y - 1], add1)


scale = 10
n = len(range(H // scale))
m = len(range(W // scale))
grid = [[0 for x in range(W // scale)] for y in range(H // scale)]


f = open('last_num.txt', 'r')
last_num, cur_digit = map(int, f.read().split(' '))
pygame.display.set_caption(f'Drawer {cur_digit}')
f.close()


was_clicked = False
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    clock.tick(300)
    screen.fill(BLACK)
    mx, my = pygame.mouse.get_pos()

    for y in range(H // scale):
        for x in range(W // scale):
            pygame.draw.rect(screen, multiply(WHITE, grid[x][y]), [x * scale, y * scale, scale, scale])

    if pygame.mouse.get_pressed(3)[0]:
        was_clicked = True
        pix_x = my//scale
        pix_y = mx//scale
        pixel_circle(grid, [pix_x, pix_y])
    if pygame.mouse.get_pressed(3)[2] and was_clicked:
        was_clicked = False
        pygame.image.save(screen, f'Data\\{last_num}-{cur_digit}.png')
        if cur_digit == 9:
            last_num += 1
        cur_digit = (cur_digit + 1) % 10
        pygame.display.set_caption(f'Drawer {cur_digit}')
        grid = [[0 for x in range(W // scale)] for y in range(H // scale)]

    pygame.display.update()

f = open('last_num.txt', 'w')
f.write(str(last_num) + ' ' + str(cur_digit))
f.close()







