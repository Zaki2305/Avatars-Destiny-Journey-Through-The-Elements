import pygame,sys,BackgroundObjects

pygame.init()

def close_game():
    pygame.quit()
    sys.exit()

#set global music
pygame.mixer.music.load("sounds/startScreen.mp3")
pygame.mixer.music.play(-1)

#set screen size
screen_width = 1250
screen_height = 650
screen = pygame.display.set_mode((screen_width, screen_height))

#set color index
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_BLUE = (173, 216, 230)

def afont(size):
    avatarFont = "fonts/Avatar_Airbender.ttf"
    afont = pygame.font.Font(avatarFont,size)
    return afont


def GameIntro():
    pygame.display.set_caption(f"Game StoryLine Intro")
    screen = pygame.display.set_mode((screen_width, screen_height))
    intro = BackgroundObjects.Levels(screen, "introText")

    text_lines = ["Since the dawn of time there has been light and darkness. The light spirit has", 
                "always kept the dark spirit in check, allowing for humanity, land animals, sea",
                "animals, bugs, and vegitation to prosper. This was all until the power hungry,",
                "no good, very bad, down right evil, Lord Zuko found a way to harness the abilities",
                "of the dark spirit. Allowing him and his army of mechanical, elemental, robot people",
                "to usher in an era of darkness. Until one day you arrived and became one with the",
                "light spirit, now you must save the entire world. This is... Avatar's Destiny"]

    # Set the color of the text
    text_color = (255, 255, 255)

    # Create a surface for the scrolling text
    text_surface = pygame.Surface((screen_width, len(text_lines) * 50), pygame.SRCALPHA)
    text_surface.set_alpha(255)

    speed_up_text = afont(20).render("Click and Hold to speed up", True, (255, 255, 255))
    speed_up_text_rect = speed_up_text.get_rect()
    speed_up_text_rect.bottomright = (screen_width - 20, screen_height - 20)
    screen.blit(speed_up_text,speed_up_text_rect)

    

    # Render each line of text and blit it onto the text surface
    for i, line in enumerate(text_lines):
        line_surface = afont(35).render(line, True, text_color)
        text_surface.blit(line_surface, (screen_width/2 - line_surface.get_width()/2, i*50))

    # Set the initial position of the text surface
    text_y = screen_height

    # Set the speed at which the text scrolls
    scroll_speed = 1

    # Run the game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Check if the left mouse button is being held down
        if pygame.mouse.get_pressed()[0]:
            # If so, increase the scroll speed
            scroll_speed = 5
        else:
            # Otherwise, set the scroll speed back to the initial value
            scroll_speed = 1

        # Move the text surface up the screen
        text_y -= scroll_speed
        if text_y + 700 <= 0:
            break

        # Draw the scrolling text on the screen
        intro.update(screen)
        screen.blit(text_surface, (0, text_y/2))

        screen.blit(speed_up_text,speed_up_text_rect)
        
        # Update the display
        pygame.display.update()
        
        # Set the frame rate
        pygame.time.Clock().tick(60)

    return

def finalBossText():
    pygame.display.set_caption(f"Game Final Boss Storyline")
    screen = pygame.display.set_mode((screen_width, screen_height))
    final = BackgroundObjects.Levels(screen, "finalText")

    text_lines = ["You have traversed and liberated every reigion of the world from monsters beyond",
                "humanities worst nightmares.The Earth Kingdown, Water Tribe, Fire Nation, and Air ",
                "Temple have all been rescued and will forever be in your debt. However the job is ",
                "not done, there is one more stop on your journey. You must enter where no other",
                "human has dared to travel before... the Spirit World.",
                "The faith and future of humanity rests on your shoulders every step, every battle",
                "every punch thrown, every time you got knocked down has all led you to this one ",
                "moment... Your battle against the Dark Avatar Zuko himself!!"]

    # Set the color of the text
    text_color = (255, 255, 255)

    # Create a surface for the scrolling text
    text_surface = pygame.Surface((screen_width, len(text_lines) * 50), pygame.SRCALPHA)
    text_surface.set_alpha(255)

    speed_up_text = afont(20).render("Click and Hold to speed up", True, (255, 255, 255))
    speed_up_text_rect = speed_up_text.get_rect()
    speed_up_text_rect.bottomright = (screen_width - 20, screen_height - 20)
    screen.blit(speed_up_text,speed_up_text_rect)
    

    # Render each line of text and blit it onto the text surface
    for i, line in enumerate(text_lines):
        line_surface = afont(35).render(line, True, text_color)
        text_surface.blit(line_surface, (screen_width/2 - line_surface.get_width()/2, i*50))

    # Set the initial position of the text surface
    text_y = screen_height

    # Set the speed at which the text scrolls
    scroll_speed = 1

    # Run the game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Check if the left mouse button is being held down
        if pygame.mouse.get_pressed()[0]:
            # If so, increase the scroll speed
            scroll_speed = 8
        else:
            # Otherwise, set the scroll speed back to the initial value
            scroll_speed = 1

        # Move the text surface up the screen
        text_y -= scroll_speed
        if text_y + 800 <= 0:
            break

        # Draw the scrolling text on the screen
        final.update(screen)
        screen.blit(text_surface, (0, text_y/2))

        screen.blit(speed_up_text,speed_up_text_rect)

        # Update the display
        pygame.display.update()

        # Set the frame rate
        pygame.time.Clock().tick(60)
    
    return

def howToPlayWindow():
    pygame.display.set_caption(f"How To Play!")
    howToPlay = BackgroundObjects.Levels(screen,"howToPlay")
    
    # Create start button
    button_width = 300
    button_height = 50

    # create the return button
    Return_button_rect = pygame.Rect(screen_width/10 - button_width/10, 590, button_width-200, button_height-20)
    Return_button = pygame.Surface((button_width-200, button_height-20))
    Return_button.fill(WHITE)
    Return_button_text = afont(20).render("Return", True, BLACK)
    Return_button_text_rect = Return_button_text.get_rect(center=Return_button.get_rect().center)
    Return_button.blit(Return_button_text, Return_button_text_rect)

    pygame.display.update()

    # game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close_game()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  #check if left mouse button was pressed
                    if Return_button_rect.collidepoint(event.pos):
                        return
            elif event.type == pygame.MOUSEMOTION:
                # if the mouse is hovering over the button then change the colour 
                if Return_button_rect.collidepoint(event.pos):
                    Return_button.fill(LIGHT_BLUE)
                    Return_button.blit(Return_button_text, Return_button_text_rect)
                else: 
                    Return_button.fill(WHITE)
                    Return_button.blit(Return_button_text, Return_button_text_rect)

        #draw the background and buttons
        howToPlay.update(screen)
        screen.blit(Return_button, Return_button_rect)
            
        #draw button borders
        pygame.draw.rect(screen, BLACK, Return_button_rect, 2)

        # Update the display
        pygame.display.update()

    return


