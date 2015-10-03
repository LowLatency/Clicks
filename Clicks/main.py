#!/usr/bin/python
import pygame


def screen_fill(color):
    screen_fill = screen.set_mode(size).fill(color)


def screen_rel_pos(rel_x=50, rel_y=50):
    #       Returns relative position from origin at top left corner.
    #   Input is a percentage

    x = screen_display.get_width()*rel_x/100
    y = screen_display.get_height()*rel_y/100

    return (x, y)


def pushtext(
             message,
             rel_x=50, rel_y=50,
             color=(10, 10, 10),
             font_style=None, font_size=36,
             abs_x=0, abs_y=0,):

    # Text display
    if pygame.font:
        font = pygame.font.Font(font_style, font_size)
        text = font.render(message, 1, color)
        center_x, center_y = screen_rel_pos(rel_x,rel_y)
        if abs_x == 0 and abs_y == 0:
            text_pos = text.get_rect(centerx=center_x, centery=center_y)
        elif abs_x != 0:
            text_pos = text.get_rect(centerx=abs_x, centery=center_y)
        elif abs_y != 0:
            text_pos = text.get_rect(centerx=center_x, centery=abs_y)
        else:
            text_pos = text.get_rect(centerx=abs_x, centery=abs_y)
        screen_display.blit(text, text_pos)


def intro_message():


    for i in range(255):
        screen_display.fill((0, 0, 0))
        image = pygame.image.load("turtle.jpg")
        image.set_alpha(i)
        logoimage = screen_display.blit(image, (0, 0))
        pygame.display.flip()


    pygame.time.delay(2000)
    pushtext("Welcome!", rel_y=10, font_size=102)
    offset = 100 # px
    square_size = 100 # px

    left_x = screen_rel_pos()[0]/2 + offset - square_size/2 - 100
    right_x = screen_rel_pos()[0]/2 + offset + square_size/2 + 100

    screen_display.fill(red, rect=[left_x, screen_rel_pos(50)[1]-square_size/2, square_size, square_size])
    screen_display.fill(blue, rect=[right_x, screen_rel_pos(50)[1]-square_size/2, square_size, square_size])

    # line center
    #screen_display.fill(blue, rect=[])


# generic colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)

# set screen [width, height]
size = [640, 480]



print("Initializing...")
# initialize game engine
pygame.init()

# initialize game display
screen = pygame.display
screen_display = screen.set_mode(size)



screen_fill(white)

# initialize game clock
clock = pygame.time.Clock()

#clock.tick(30)
print("Finished Initializing.")

# Temp values
mouse_touch = False

'''
pushtext("Welcome")
pushtext("C - clear screen", rel_y=55)
pushtext("Space - change cursor color", rel_y=60)
'''
color_change = 0

pushtext("Welcome to pygame paint!",abs_y=10)

cursor_color = ((0, 0, 0), (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 255))

gameEnd = False

#screen_display.fill(cursor_color[color_change], rect=[10, 10, 50, 50])

intro_message()

# Event handler

while gameEnd == False:

    # Begin event handler
    for event in pygame.event.get():
        screen.set_caption(str(event))
        print(event)
        if event.type == pygame.QUIT:
            gameEnd = True

        if event.type == pygame.KEYDOWN:
           if event.key == pygame.K_ESCAPE:
                gameEnd = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                screen_fill(white)
                pygame.display.update()
            if event.key == pygame.K_SPACE:
                color_change += 1
                if color_change == len(cursor_color):
                    color_change = 0
                # Current Color
                screen_display.fill(cursor_color[color_change], rect=[0, 0, size[0], screen_rel_pos(5,5)[1]])
                if cursor_color[color_change] == (0, 0, 0):
                    pushtext("Current Color", color=(255, 255, 255), rel_x=50, rel_y=2, font_size=24)
                else:
                    pushtext("Current Color", rel_x=50, rel_y=2, font_size=24)

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_touch = True

        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_touch = False

        if mouse_touch:
            if event.type == pygame.MOUSEMOTION:

                mouse_location = pygame.mouse.get_pos()
                screen_display.fill(cursor_color[color_change], rect=[mouse_location[0], mouse_location[1], 10, 10])

    pygame.display.update()

quit()
