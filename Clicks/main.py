import pygame

def screen_fill(color):
    screen_fill = screen.set_mode(size).fill(color)

def screen_rel_pos(rel_x, rel_y):

    #       Returns relative position from origin at top left corner.
    #   Input is a percentage

    x = screen_display.get_width()*rel_x/100
    y = screen_display.get_height()*rel_y/100
    return (x, y)


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
print("Finished Initializing.")

# Temp values
mouse_touch = False

# Text display
if pygame.font:
    font = pygame.font.Font(None, 36)
    text = font.render("Nik SUX bruh", 1, (10, 10, 10))
    center_X, center_Y = screen_rel_pos(50,50)
    textpos = text.get_rect(centerx=center_X, centery=center_Y)
    screen_display.blit(text, textpos)



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
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_touch = False


        if mouse_touch:
            if event.type == pygame.MOUSEMOTION:
                mouse_location = pygame.mouse.get_pos()
                screen_display.fill(red, rect=[mouse_location[0], mouse_location[1], 10, 10])
                print("Mouse moved!")

    pygame.display.update()
quit()