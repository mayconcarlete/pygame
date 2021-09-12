import pygame


def make_squares(screen):
    line_color = (0, 0, 255)
    line = []
    width_count = 0
    height_count = 0
    while height_count < 600:
        line.append(pygame.draw.line(screen, line_color ,(width_count, height_count), (860, height_count)))
        height_count += 50
    line.append(pygame.draw.line(screen, line_color ,(0, 599), (860, 599)))
    
    width_count = 0
    height_count = 0
    
    while width_count < 860:
        line.append(pygame.draw.line(screen, line_color, (width_count, height_count), (width_count, 599)))
        width_count += 50


def with_square(position):
    
    x = position[0]/50
    x = (int(x + (0 if x%1 == 0 else 1)) -1)
    y = position[1] / 50
    y = (int(y + (0 if y%1 == 0 else 1)) -1)  

    print(x, y)
    
    return [x, y]

    # line_color = (255, 0, 0)
    # left = (x * 50) + 1
    # top = (y * 50) + 1
    # width = 49
    # height = 49
    
    # rect = pygame.Rect(left, top, width, height)

    # pygame.draw.rect(screen, line_color, rect)
    # pygame.display.flip()

def draw_square(screen, last_square, position):
    # print('last_square: ', last_square)
    # print('position: ', position)
    x = last_square[0]
    y = last_square[1]
    line_color = (0, 0, 0)
    left = (x * 50) + 1
    top = (y * 50) + 1
    width = 50
    height = 50
    
    rect = pygame.Rect(left, top, width, height)

    pygame.draw.rect(screen, line_color, rect)
    pygame.display.flip()
    make_squares(screen)
    x = position[0]
    y = position[1]
    line_color = (255, 0, 0)
    left = (x * 50) + 4
    top = (y * 50) + 3
    width = 44
    height = 44
    
    rect = pygame.Rect(left, top, width, height)

    pygame.draw.rect(screen, line_color, rect)
    pygame.display.flip()