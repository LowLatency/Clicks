import pygame

def screen_fill(color):
    screen_fill = screen.set_mode(size).fill(color)


# generic colors
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)


print("Initializing...")
# initialize game engine
pygame.init()

# set screen [width, height]
size = [640, 480]

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
    textpos = text.get_rect(centerx=screen_display.get_width()/2, centery=screen_display.get_height()/2)
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