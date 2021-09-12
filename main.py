import sys, pygame
from map import make_squares, with_square, draw_square

background_color = (0, 0, 0)

HEIGHT = 840
WIDTH = 600

PADDING = 150

PIXEL_SIZE = 32


screen = pygame.display.set_mode((HEIGHT, WIDTH))


pygame.display.set_caption('Maykerops for geeks')

screen.fill(background_color)

line_color = (0,0,255)

# line = pygame.Rect(150,150,5,20)
# pygame.draw.rect(screen, line_color, line)

# pygame.draw.line(screen, line_color, (0,0), (300,300), 4)
make_squares(screen)

pygame.display.flip()

running = True

last_square = [0,0]
while running:
    for event in pygame.event.get():
        print('O valor de last: ', last_square)
        paint_square = with_square(pygame.mouse.get_pos())
        if paint_square != last_square:
            draw_square(screen, last_square, paint_square)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
            print('Enter')
        if event.type == pygame.QUIT:
            running = False
        last_square = paint_square
        print('novo valor de last:', last_square)