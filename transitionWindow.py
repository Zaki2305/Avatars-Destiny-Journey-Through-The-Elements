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
pygame.display.set_caption(f"Level Cleared! Move To Next Level")

#set color index
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_BLUE = (173, 216, 230)

def afont(size):
    avatarFont = "fonts/Avatar_Airbender.ttf"
    afont = pygame.font.Font(avatarFont,size)
    return afont

def transitionWindow():
    #set to clear screen with background
    screen = pygame.display.set_mode((screen_width, screen_height))
    trans = BackgroundObjects.Levels(screen, "transition")

    #create button size
    button_width = 500
    button_height = 100

    #create title text title text
    title_text = afont(100).render("Level", True, WHITE)
    title_text2 = afont(100).render("Cleared", True, WHITE)

    #shop button placed
    shop_button_rect = pygame.Rect(screen_width/2 - button_width/10, 270, button_width, button_height)
    shop_button = pygame.Surface((button_width, button_height))
    shop_button.fill(WHITE)
    shop_button_text = afont(50).render("Shop", True, BLACK)
    shop_button_text_rect = shop_button_text.get_rect(center=shop_button.get_rect().center)
    shop_button.blit(shop_button_text, shop_button_text_rect)

    #quit game button placed
    quit_button_rect = pygame.Rect(screen_width/2 - button_width/10, 450, button_width, button_height)
    quit_button = pygame.Surface((button_width, button_height))
    quit_button.fill(WHITE)
    quit_button_text = afont(50).render("Quit Game", True, BLACK)
    quit_button_text_rect = quit_button_text.get_rect(center=quit_button.get_rect().center)
    quit_button.blit(quit_button_text, quit_button_text_rect)

    #next level button placed
    next_button_rect = pygame.Rect(screen_width/2 - button_width/10, 90, button_width, button_height)
    next_button = pygame.Surface((button_width, button_height))
    next_button.fill(WHITE)
    next_button_text = afont(50).render("Next Level", True, BLACK)
    next_button_text_rect = next_button_text.get_rect(center=next_button.get_rect().center)
    next_button.blit(next_button_text, next_button_text_rect)

    # create the how to play button
    howToPlay_button_rect = pygame.Rect(screen_width/10 - 30, 530, 150, 30)
    howToPlay_button = pygame.Surface((150, 30))
    howToPlay_button.fill(WHITE)
    howToPlay_button_text = afont(20).render("How To Play", True, BLACK)
    howToPlay_button_text_rect = howToPlay_button_text.get_rect(center=howToPlay_button.get_rect().center)
    howToPlay_button.blit(howToPlay_button_text, howToPlay_button_text_rect)


    pygame.display.update()
    running = True
    while running:
        for event in pygame.event.get():
            #when quit close the game
            if event.type == pygame.QUIT:
                close_game()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    #action if any button is clicked
                    if quit_button_rect.collidepoint(event.pos):
                        close_game()
                    if next_button_rect.collidepoint(event.pos):
                        return "next"
                    if shop_button_rect.collidepoint(event.pos):
                        return "shop"
                    if howToPlay_button_rect.collidepoint(event.pos):
                        return "howToPlay"
            #highlight button when mouse on button on action
            elif event.type == pygame.MOUSEMOTION:
                if quit_button_rect.collidepoint(event.pos):
                    quit_button.fill(LIGHT_BLUE)
                    quit_button.blit(quit_button_text, quit_button_text_rect)
                else:
                    quit_button.fill(WHITE)
                    quit_button.blit(quit_button_text, quit_button_text_rect)
                if next_button_rect.collidepoint(event.pos):
                    next_button.fill(LIGHT_BLUE)
                    next_button.blit(next_button_text, next_button_text_rect)
                else:
                    next_button.fill(WHITE)
                    next_button.blit(next_button_text, next_button_text_rect)
                if shop_button_rect.collidepoint(event.pos):
                    shop_button.fill(LIGHT_BLUE)
                    shop_button.blit(shop_button_text, shop_button_text_rect)
                else:
                    shop_button.fill(WHITE)
                    shop_button.blit(shop_button_text, shop_button_text_rect)
                if howToPlay_button_rect.collidepoint(event.pos):
                    howToPlay_button.fill(LIGHT_BLUE)
                    howToPlay_button.blit(howToPlay_button_text, howToPlay_button_text_rect)
                else:
                    howToPlay_button.fill(WHITE)
                    howToPlay_button.blit(howToPlay_button_text, howToPlay_button_text_rect)
                    
        #draw the background, title text, subtitle text, and buttons
        trans.update(screen)
        screen.blit(next_button, next_button_rect)
        screen.blit(shop_button, shop_button_rect)
        screen.blit(quit_button, quit_button_rect)
        screen.blit(howToPlay_button, howToPlay_button_rect)
        screen.blit(title_text, (screen_width/6 - title_text.get_width()/3, screen_height/2 - 100))
        screen.blit(title_text2, (screen_width/6 - title_text.get_width()/3, screen_height/2))
        
        #draw button borders
        pygame.draw.rect(screen, BLACK, shop_button_rect, 2)
        pygame.draw.rect(screen, BLACK, quit_button_rect, 2)
        pygame.draw.rect(screen, BLACK, next_button_rect, 2)

        #keep updating screen
        pygame.display.update()
        
    return
