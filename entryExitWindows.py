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
pygame.display.set_caption("Entry/Exit Window")

#set color index
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_BLUE = (173, 216, 230)

def afont(size):
    avatarFont = "fonts/Avatar_Airbender.ttf"
    afont = pygame.font.Font(avatarFont,size)
    return afont



# function for opening the start screen
def createStartWindow():
    pygame.display.set_caption(f"Entry Window")
    # setting the text and the background for the start screen
    startScreenLevel = BackgroundObjects.Levels(screen,"start")
    title_text = afont(100).render("Avatars Destiny;", True, WHITE)
    title_text2 = afont(70).render(" A Journey through the Elements", True, WHITE)

    # Create start button
    button_width = 300
    button_height = 50

    # create the start button
    start_button_rect = pygame.Rect(screen_width/10 - button_width/10, 400, button_width, button_height)
    start_button = pygame.Surface((button_width, button_height))
    start_button.fill(WHITE)
    start_button_text = afont(50).render("Start Game", True, BLACK)
    start_button_text_rect = start_button_text.get_rect(center=start_button.get_rect().center)
    start_button.blit(start_button_text, start_button_text_rect)

    # creating the quit button
    quit_button_rect = pygame.Rect(screen_width/10 - button_width/10, 465, button_width, button_height)
    quit_button = pygame.Surface((button_width, button_height))
    quit_button.fill(WHITE)
    quit_button_text = afont(50).render("Quit Game", True, BLACK)
    quit_button_text_rect = quit_button_text.get_rect(center=quit_button.get_rect().center)
    quit_button.blit(quit_button_text, quit_button_text_rect)

    # create the how to play button
    howToPlay_button_rect = pygame.Rect(screen_width/10 - button_width/10, 530, button_width-150, button_height-20)
    howToPlay_button = pygame.Surface((button_width-150, button_height-20))
    howToPlay_button.fill(WHITE)
    howToPlay_button_text = afont(20).render("How To Play", True, BLACK)
    howToPlay_button_text_rect = howToPlay_button_text.get_rect(center=howToPlay_button.get_rect().center)
    howToPlay_button.blit(howToPlay_button_text, howToPlay_button_text_rect)


    pygame.display.update()

    # game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close_game()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  #check if left mouse button was pressed
                    if quit_button_rect.collidepoint(event.pos):  #check if mouse clicked on button
                        close_game()
                    if start_button_rect.collidepoint(event.pos):
                        return #return function to go to next screen
                    if howToPlay_button_rect.collidepoint(event.pos):
                        return "howToPlay"
            elif event.type == pygame.MOUSEMOTION:
                # if the mouse is hovering over the button then change the colour 
                if start_button_rect.collidepoint(event.pos):
                    start_button.fill(LIGHT_BLUE)
                    start_button.blit(start_button_text, start_button_text_rect)
                else: 
                    start_button.fill(WHITE)
                    start_button.blit(start_button_text, start_button_text_rect)
                if quit_button_rect.collidepoint(event.pos):
                    quit_button.fill(LIGHT_BLUE)
                    quit_button.blit(quit_button_text, quit_button_text_rect)
                else:
                    quit_button.fill(WHITE)
                    quit_button.blit(quit_button_text, quit_button_text_rect)
                if howToPlay_button_rect.collidepoint(event.pos):
                    howToPlay_button.fill(LIGHT_BLUE)
                    howToPlay_button.blit(howToPlay_button_text, howToPlay_button_text_rect)
                else:
                    howToPlay_button.fill(WHITE)
                    howToPlay_button.blit(howToPlay_button_text, howToPlay_button_text_rect)

        #draw the background, title text, subtitle text, and buttons
        startScreenLevel.update(screen)
        screen.blit(title_text, (screen_width/2 - title_text.get_width()/2, 80))
        screen.blit(title_text2, (screen_width/2 - title_text2.get_width()/2, 150))
        screen.blit(start_button, start_button_rect)
        screen.blit(quit_button, quit_button_rect)
        screen.blit(howToPlay_button, howToPlay_button_rect)
        
        #draw button borders
        pygame.draw.rect(screen, BLACK, start_button_rect, 2)
        pygame.draw.rect(screen, BLACK, quit_button_rect, 2)
        pygame.draw.rect(screen, BLACK, howToPlay_button_rect, 2)


        # Update the display
        pygame.display.update()

    return

def finish(result):
    pygame.display.set_caption(f"Exit Window")
    screen = pygame.display.set_mode((screen_width, screen_height))
    #when character loses and dies
    if (result == 0):
        trans = BackgroundObjects.Levels(screen, "finishLose")
    #win the whole game
    if (result == 1):
        trans = BackgroundObjects.Levels(screen, "finishWin")
        #create title text title text
        title_text = afont(100).render("Congratulation!", True, BLACK)
        title_text2 = afont(70).render("You Finished the Game", True, BLACK)

    # Create start button
    button_width = 300
    button_height = 50

    # create the start button
    restart_button_rect = pygame.Rect(screen_width/10 - button_width/10, 400, button_width, button_height)
    restart_button = pygame.Surface((button_width, button_height))
    restart_button.fill(WHITE)
    restart_button_text = afont(50).render("Restart Game", True, BLACK)
    restart_button_text_rect = restart_button_text.get_rect(center=restart_button.get_rect().center)
    restart_button.blit(restart_button_text, restart_button_text_rect)

    # creating the quit button
    quit_button_rect = pygame.Rect(screen_width/10 - button_width/10, 465, button_width, button_height)
    quit_button = pygame.Surface((button_width, button_height))
    quit_button.fill(WHITE)
    quit_button_text = afont(50).render("Quit Game", True, BLACK)
    quit_button_text_rect = quit_button_text.get_rect(center=quit_button.get_rect().center)
    quit_button.blit(quit_button_text, quit_button_text_rect)

    pygame.display.update()

    running = True
    while running:
        for event in pygame.event.get():
            #when quit close the game
            if event.type == pygame.QUIT:
                close_game()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  #check if left mouse button was pressed
                    if quit_button_rect.collidepoint(event.pos):  #check if mouse clicked on button
                        close_game()
                    if restart_button_rect.collidepoint(event.pos):
                        return "restart" #return function to go to next screen
            elif event.type == pygame.MOUSEMOTION:
                # if the mouse is hovering over the button then change the colour 
                if restart_button_rect.collidepoint(event.pos):
                    restart_button.fill(LIGHT_BLUE)
                    restart_button.blit(restart_button_text, restart_button_text_rect)
                else: 
                    restart_button.fill(WHITE)
                    restart_button.blit(restart_button_text, restart_button_text_rect)
                if quit_button_rect.collidepoint(event.pos):
                    quit_button.fill(LIGHT_BLUE)
                    quit_button.blit(quit_button_text, quit_button_text_rect)
                else:
                    quit_button.fill(WHITE)
                    quit_button.blit(quit_button_text, quit_button_text_rect)
        
        screen.blit(restart_button, restart_button_rect)
        screen.blit(quit_button, quit_button_rect)
        
        #draw button borders
        pygame.draw.rect(screen, BLACK, restart_button_rect, 2)
        pygame.draw.rect(screen, BLACK, quit_button_rect, 2)

        if (result == 1):
            screen.blit(title_text, (screen_width/5 - title_text.get_width()/3, screen_height - 600))
            screen.blit(title_text2, (screen_width/5 - title_text.get_width()/3 + 10, screen_height - 525))
        #keep updating screen
        pygame.display.update() 

    return
