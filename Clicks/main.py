#!/usr/bin/python
import random

# pygame module is mandatory, game can not run without it
try:
    import pygame
except ImportError:
    print("pygame is required!")
    quit()


def screen_fill(input_color):
    screen.set_mode(size).fill(input_color)


def screen_rel_pos(rel_x=50, rel_y=50):
    #       Returns relative position from origin at top left corner.
    #   - Input is a percentage

    x = screen_display.get_width()*rel_x/100
    y = screen_display.get_height()*rel_y/100

    return x, y


def insert_image(file, location=(0, 0)):
    image = pygame.image.load(file)
    screen_display.blit(image, location)
    pygame.display.flip()


def pushtext(
             message,
             rel_x=50, rel_y=50,
             color=(10, 10, 10),
             font_style=None, font_size=36,
             abs_x=0, abs_y=0):
    #       Prints text to display
    #   - Position can be customized relative or absolute to the screen dimensions.
    #   - Will always be using relative position unless an absolute position is specified.
    #   - If given a absolute position value in a single axis, then the perspective perpendicular axis will be
    #   using the relative value.

    # Text display
    if pygame.font:
        font = pygame.font.Font(font_style, font_size)
        text = font.render(message, 1, color)
        center_x, center_y = screen_rel_pos(rel_x, rel_y)

        if abs_x == 0 and abs_y == 0:
            text_pos = text.get_rect(centerx=center_x, centery=center_y)
        elif abs_x != 0 and abs_y != 0:
            text_pos = text.get_rect(centerx=abs_x, centery=abs_y)
        elif abs_x != 0:
            text_pos = text.get_rect(centerx=abs_x, centery=center_y)
        elif abs_y != 0:
            text_pos = text.get_rect(centerx=center_x, centery=abs_y)

        screen_display.blit(text, text_pos)
    pygame.display.update()


def intro_message(animation=True, message="Welcome", color=(0, 0, 0)):
    #       Splash screen with simple message prompt

    # Splash screen image display
    for i in range(128):
        screen_display.fill((0, 0, 0))
        image = pygame.image.load("turtle.jpg")
        if animation:
            image.set_alpha(i/128*255)
        screen_display.blit(image, (0, 0))
        pygame.display.flip()

    if message:
        pushtext(message=message, rel_y=12, font_size=102, color=color)


def game_pick():
    #       Display two rectangular buttons for user to decide which path to take
    #   - From center of screen, offset is how many pixels from relative center of display.
    #   - Square size allows you to customize how big or small the square shall be.
    
    #   Output:
    #   left button, result = 1
    #   right button, result = 2
    
    offset = 100
    square_size = 100

    height_top = int(screen_rel_pos(50)[1] - square_size/2)
    height_bottom = int(screen_rel_pos(50)[1] + square_size/2)
    
    # left button
    ll_x = int(screen_rel_pos()[0] - offset - square_size)
    lr_x = int(screen_rel_pos()[0] - offset)
    
    # right button
    rl_x = int(screen_rel_pos()[0] + offset)
    rr_x = int(screen_rel_pos()[0] + offset + square_size)

    # create buttons
    screen_display.fill(red, rect=[ll_x, height_top, square_size, square_size])
    screen_display.fill(blue, rect=[rl_x, height_top, square_size, square_size])

    pygame.display.update()

    result = False
    pick = False
    
    # Event handler
    while not pick:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pick = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pick = True

            if event.type == pygame.MOUSEBUTTONDOWN:

                mouse_location = pygame.mouse.get_pos()
                if height_top <= mouse_location[1] <= height_bottom:

                    # check press button
                    if ll_x <= mouse_location[0] <= lr_x:

                        result = 1
                        pick = True

                    elif rl_x <= mouse_location[0] <= rr_x:

                        result = 2
                        pick = True
    return result

# Parameters

# generic colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
orange = (255, 140, 0)
cursor_color = (black, red, green, blue, white, orange)

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

print("Finished Initializing.")

# Temp values
mouse_touch = False
gameEnd = False
color_change = 0
alligatorArt = "Alligator.png"


# Game begin

while not gameEnd:

    intro_message()
    handle = True

    # Select option
    output = game_pick()

    if output == 0:
        # Exit
        quit()

    elif output == 1:
        # Penguin tickle option

        screen_fill(white)
        pushtext("Red Option!", rel_y=10, color=red)
        for i in range(2):
            for color in cursor_color:
                pushtext("Red has been selected!", abs_y=100, color=color)
                pygame.time.delay(50)

        screen_fill(white)

        image_size_x = 300
        image_size_y = 300

        image_location = (screen_rel_pos()[0] - image_size_x/2, screen_rel_pos()[1] - image_size_y/2)

        insert_image("penguin.jpg", image_location)

        pushtext("Penguin Click Counter", abs_y=100, color=orange)

        clicks = True

        score = 0

        # Begin event handler for penguin clicks
        while clicks:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        clicks = False
                if event.type == pygame.MOUSEBUTTONDOWN:

                    # Detect if mouse clicks are within image dimensions
                    mouse_location = pygame.mouse.get_pos()
                    if image_location[1] <= mouse_location[1] <= image_location[1] + image_size_y:
                        if image_location[0] <= mouse_location[0] <= image_location[0] + image_size_x:
                            score += 1

                            print(score)
                            screen_display.fill(white, rect=[0, 0, 50, 35])
                            pushtext("ESC - main menu", rel_y=90, color=cursor_color[score % 5])
                            pygame.display.flip()
                            pushtext(str(score), abs_x=20, abs_y=20)

                            if score == 10:
                                for color in cursor_color:
                                    pushtext("Release the Alligators!", rel_y=10, color=color)
                                    pygame.time.delay(50)
                                pushtext("Release the Alligators!", rel_y=10, color=red)

                            if score >= 10:
                                insert_image(alligatorArt, (random.randrange(0, size[0]), random.randrange(0, size[1])))

        handle = False

    elif output == 2:
        # Freestyle painting
        intro_message(False, message="Blue Option", color=blue)

        pushtext("Welcome to pygame paint!", abs_y=100, color=orange)

        pushtext("C - clear screen", rel_y=55, color=white)
        pushtext("Space - change cursor color", rel_y=60, color=white)
        pushtext("ESC - main menu", rel_y=90, color=green)

    # Begin event handler for paint
    while handle:
        for event in pygame.event.get():
            screen.set_caption(str(event))
            print(event)
            if event.type == pygame.QUIT:
                handle = False
                gameEnd = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    handle = False
                    gameEnd = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    screen_fill(white)
                    pygame.display.update()
                if event.key == pygame.K_SPACE:
                    color_change += 1
                    if color_change == len(cursor_color):
                        color_change = 0
                    screen_display.fill(cursor_color[color_change], rect=[0, 0, size[0], screen_rel_pos(5,5)[1]])
                    if cursor_color[color_change] == black:
                        pushtext("Current Color", color=white, rel_x=50, rel_y=2, font_size=24)
                    else:
                        pushtext("Current Color", rel_x=50, rel_y=2, font_size=24)

            #       Monitors mouse clicks and movement for painting
            #   - If mouse is stationary, no paint will be recorded on canvas.
            #   - Left click and mouse drag is required for painting on canvas.
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
