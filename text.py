import sys
import pygame

# Initialize pygame so it runs in the background and manages things
pygame.init()

miku = pygame.Color(100, 225, 225)
red = pygame.Color(100, 0, 0)

# Create a display. Size must be a tuple, which is why it's in parentheses
screen = pygame.display.set_mode( (400, 400) )
font = pygame.font.Sysfont("Comic Sans",  100)

text = font.render("blood", True, red)

# Main loop. Your game would go inside this loop
while True:
    # do something for each event in the event queue (list of things that happen)
    for event in pygame.event.get():
        # Check to see if the current event is a QUIT event
        print(event)
        if event.type == pygame.QUIT:
            # If so, exit the program
            sys.exit()
    screen.fill(miku)
    screen.blit(text, pygame.mouse.get_pos())
    pygame.display.flip()