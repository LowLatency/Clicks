#!/usr/bin/python
import pygame


def screen_fill(color):
    screen_fill = screen.set_mode(size).fill(color)


def screen_rel_pos(rel_x, rel_y):
    #       Returns relative position from origin at top left corner.
    #   Input is a percentage

    x = screen_display.get_width()*rel_x/100
    y = screen_display.get_height()*rel_y/100

    return (x, y)


def pushtext(message,rel_x=50, rel_y=50, color=(10, 10, 10)):
    # Text display
    if pygame.font:
        font = pygame.font.Font(None, 36)
        text = font.render(message, 1, color)
        center_X, center_Y = screen_rel_pos(rel_x,rel_y)
        text_pos = text.get_rect(centerx=center_X, centery=center_Y)
        screen_display.blit(text, text_pos)

# generic colors
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)


print("Initializing...")
# initialize game engine
pygame.init()

# set screen [width, height]
size = [800, 600]

# initialize game display
screen = pygame.display
screen_display = screen.set_mode(size)



screen_fill(white)

# initialize game clock
clock = pygame.time.Clock()

clock.tick(30)
print("Finished Initializing.")

# Temp values
mouse_touch = False


pushtext("Nik sux")

gameEnd = False
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

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_touch = True
            pushtext("Touch down!")
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_touch = False
            pushtext("Lift off!")

        if mouse_touch:
            if event.type == pygame.MOUSEMOTION:

                pushtext("Motion denied!")

                mouse_location = pygame.mouse.get_pos()
                screen_display.fill(red, rect=[mouse_location[0], mouse_location[1], 10, 10])

    pygame.display.update()
quit()