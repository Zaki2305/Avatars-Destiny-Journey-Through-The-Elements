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
pygame.display.set_caption(f"Shop")

#set color index
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_BLUE = (173, 216, 230)

def afont(size):
    avatarFont = "fonts/Avatar_Airbender.ttf"
    afont = pygame.font.Font(avatarFont,size)
    return afont

counter = 0
counter1 = 0
counter2 = 0

def shop(character_attributes):
    global counter,counter1, counter2
    strength = character_attributes["strength"]
    speed = character_attributes["speed"]
    maxHP = character_attributes["health"]
    coins = character_attributes["coins"]
    screen = pygame.display.set_mode((screen_width, screen_height))
    screen.fill(BLACK)
    title_text = afont(100).render("SHOP", True, WHITE)
    #CHANGE THIS WHEN COIN FUNCTION IS MADE (FOR TESTING RN)

    def buy_item(item,price):
        #print line for testing
        print(f"Bought {item} for {price} coins.")
        #coin deduction goes here

    #item button 1
    item_button_rect = pygame.Rect(50, 200, 400, 80)
    item_button = pygame.Surface((400, 80))
    item_button.fill(WHITE)
    item_text = afont(50).render("Strength - 10 coins", True, BLACK)
    item_text_rect = item_text.get_rect(center=item_button.get_rect().center)
    item_text_max = afont(50).render("Max Strength", True, BLACK)
    item_text_rect_max = item_text_max.get_rect(center=item_button.get_rect().center)
    item_button.blit(item_text, item_text_rect)

    #second item button
    item_button_rect2 = pygame.Rect(50, 300, 400, 80)
    item_button2 = pygame.Surface((400, 80))
    item_button2.fill(WHITE)
    item_text2 = afont(50).render("Speed - 10 coins", True, BLACK)
    item_text_rect2 = item_text2.get_rect(center=item_button2.get_rect().center)
    item_text_max2 = afont(50).render("Max Speed", True, BLACK)
    item_text_rect_max2 = item_text_max2.get_rect(center=item_button2.get_rect().center)
    item_button2.blit(item_text2, item_text_rect2)

    #third item button
    item_button_rect3 = pygame.Rect(50, 400, 400, 80)
    item_button3 = pygame.Surface((400, 80))
    item_button3.fill(WHITE)
    item_text3 = afont(50).render("Max HP - 10 coins", True, BLACK)
    item_text_rect3 = item_text3.get_rect(center=item_button3.get_rect().center)
    item_text_max3 = afont(50).render("Max HP", True, BLACK)
    item_text_rect_max3 = item_text_max3.get_rect(center=item_button3.get_rect().center)
    item_button3.blit(item_text3, item_text_rect3)

    # Create a back button
    back_button_rect = pygame.Rect(50, 500, 400, 80)
    back_button = pygame.Surface((400, 80))
    back_button.fill(WHITE)
    back_button_text = afont(50).render("Leave Shop", True, BLACK)
    back_button_text_rect = back_button_text.get_rect(center=back_button.get_rect().center)
    back_button.blit(back_button_text, back_button_text_rect)

    max_text = afont(50).render("No Funds Remaining", True, BLACK)
    max_text_rect = max_text.get_rect(center=item_button.get_rect().center)
    max_text_rect2 = max_text.get_rect(center=item_button2.get_rect().center)
    max_text_rect3 = max_text.get_rect(center=item_button3.get_rect().center)

    #background image rescale to screen size
    bg = BackgroundObjects.Levels(screen,"shop")

    strengthbg = pygame.image.load("objectsImages/strength.png")
    strengthbg = pygame.transform.scale(strengthbg, (32, 32))

    speedbg = pygame.image.load("objectsImages/speed.png")
    speedbg = pygame.transform.scale(speedbg, (32, 32))

    healthbg = pygame.image.load("objectsImages/health.png")
    healthbg = pygame.transform.scale(healthbg, (32, 32))

    #colour for max button
    GRAY = (211,211,211)
    RED = (255,0,0)
    #counters for button pressed action
    pygame.display.update()

    # game loop
    running = True
    while running:
        #blit the background onto the screen
        bg.update(screen)

        screen.blit(strengthbg,(250,43))
        strength_amt_text = afont(45).render(f"{strength}", True, WHITE)
        screen.blit(strength_amt_text,(250+strengthbg.get_width(),43))

        screen.blit(speedbg,(247,73))
        speed_amt_text = afont(45).render(f"{speed}", True, WHITE)
        screen.blit(speed_amt_text,(247+speedbg.get_width(),73))

        screen.blit(healthbg,(250,103))
        maxHP_amt_text = afont(45).render(f"{maxHP}", True, WHITE)
        screen.blit(maxHP_amt_text,(250+healthbg.get_width(),103))

        coin_amt_text = afont(100).render(f"{coins}", True, WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  #check if left mouse button was pressed
                    #make the button gray and blit the new message for max 
                    if counter > 2:
                        item_button.fill(GRAY)
                        item_button.blit(item_text_max, item_text_rect_max)
                    if item_button_rect.collidepoint(event.pos) and coins >= 10:
                        buy_item("strengh",10)
                        strength += 10
                        coins -= 10
                        print(coins)
                        counter += 1 #increment counter

                    #make the button gray and blit the new message for max 
                    if counter1 > 2:
                        item_button2.fill(GRAY)
                        item_button2.blit(item_text_max2, item_text_rect_max2)
                    if item_button_rect2.collidepoint(event.pos) and coins >= 10:
                        buy_item("speed",10)
                        speed += 1
                        coins -= 10
                        print(coins)
                        counter1 += 1 #increment counter
                    
                    #make the button gray and blit the new message for max 
                    if counter2 > 2:
                        item_button3.fill(GRAY)
                        item_button3.blit(item_text_max3, item_text_rect_max3)
                    if item_button_rect3.collidepoint(event.pos) and coins >= 10:
                        buy_item("max HP",10)
                        maxHP += 20
                        coins -= 10
                        print(coins)
                        counter2 += 1 #increment counter
                    #return to the previous window when the back button is pressed
                    if back_button_rect.collidepoint(event.pos):
                        return {"coins":coins,"strength":strength,"health":maxHP,"speed":speed}
            elif event.type == pygame.MOUSEMOTION:
                # if the mouse is hovering over the button then change the colour to blue
                if back_button_rect.collidepoint(event.pos):
                    back_button.fill(LIGHT_BLUE)
                    back_button.blit(back_button_text, back_button_text_rect)
                #when the mouse is not hovering over the button it will be white
                else: 
                    back_button.fill(WHITE)
                    back_button.blit(back_button_text, back_button_text_rect)

                if item_button_rect.collidepoint(event.pos):
                    item_button.fill(LIGHT_BLUE)
                    item_button.blit(item_text, item_text_rect)
                    if counter > 3:
                        item_button.fill(GRAY)
                        item_button.blit(item_text_max, item_text_rect_max)
                    elif coins < 10:
                        item_button.fill(RED)
                        item_button.blit(max_text, max_text_rect)
                else: 
                    item_button.fill(WHITE)
                    item_button.blit(item_text, item_text_rect)
                    if counter > 3:
                        item_button.fill(GRAY)
                        item_button.blit(item_text_max, item_text_rect_max)
                        

                if item_button_rect2.collidepoint(event.pos):
                    item_button2.fill(LIGHT_BLUE)
                    item_button2.blit(item_text2, item_text_rect2)
                    if counter1 > 3:
                        item_button2.fill(GRAY)
                        item_button2.blit(item_text_max2, item_text_rect_max2)
                    elif coins < 10:
                        item_button2.fill(RED)
                        item_button2.blit(max_text, max_text_rect2)
                else: 
                    item_button2.fill(WHITE)
                    item_button2.blit(item_text2, item_text_rect2)
                    if counter1 > 3:
                        item_button2.fill(GRAY)
                        item_button2.blit(item_text_max2, item_text_rect_max2)

                if item_button_rect3.collidepoint(event.pos):
                    item_button3.fill(LIGHT_BLUE)
                    item_button3.blit(item_text3, item_text_rect3)
                    if counter2 > 3:
                        item_button3.fill(GRAY)
                        item_button3.blit(item_text_max3, item_text_rect_max3)
                    elif coins < 10:
                        item_button3.fill(RED)
                        item_button3.blit(max_text, max_text_rect3)
                else: 
                    item_button3.fill(WHITE)
                    item_button3.blit(item_text3, item_text_rect3)
                    if counter2 > 3:
                        item_button3.fill(GRAY)
                        item_button3.blit(item_text_max3, item_text_rect_max3)

        # Define the dimensions and position of the progress bars
        progress_bar_width = 200
        progress_bar_height = 20
        progress_bar_y_spacing = 30
        progress_bars_rects = [pygame.Rect(50, 50 + i * progress_bar_y_spacing +1, progress_bar_width, progress_bar_height) for i in range(3)]
        border_color = pygame.Color('black')
        fill_colors = [pygame.Color('green'), pygame.Color('blue'), pygame.Color('red')]

        #Progress bar updates
        strength_progress = {0:0, 1: 0.25, 2: 0.5, 3: 0.75, 4:1}
        if counter in strength_progress:
            strengthProgress = strength_progress[counter]
        else:
            strengthProgress = 1
        
        speedProgress = {0:0, 1: 0.25, 2: 0.5, 3: 0.75, 4:1}
        if counter1 in speedProgress:
            speedProgress = speedProgress[counter1]
        else:
            speedProgress = 1

        hpProgress = {0:0, 1: 0.25, 2: 0.5, 3: 0.75, 4:1}
        if counter2 in hpProgress:
            hpProgress = hpProgress[counter2]
        else:
            hpProgress = 1

        current_progresses = [strengthProgress, speedProgress, hpProgress]

        # Draw the progress bars
        for i in range(3):
            current_progress = current_progresses[i]
            fill_color = fill_colors[i]
            progress_bar_rect = progress_bars_rects[i]
            fill_width = int(progress_bar_rect.width * current_progress)
            filled_rect = pygame.Rect(progress_bar_rect.left, progress_bar_rect.top, fill_width, progress_bar_rect.height)
            unfilled_rect = pygame.Rect(filled_rect.right, progress_bar_rect.top, progress_bar_rect.width - fill_width, progress_bar_rect.height)

            pygame.draw.rect(screen, border_color, progress_bar_rect, 2)  # Draw the border
            pygame.draw.rect(screen, fill_color, filled_rect)  # Draw the filled rectangle
            pygame.draw.rect(screen, border_color, unfilled_rect, 2)  # Draw the unfilled rectangle

        # Draw the background, title text, and buttons
        screen.blit(title_text, (screen_width/2 - title_text.get_width()/2, 80))
        screen.blit(coin_amt_text, (990, 17))
        screen.blit(item_button, item_button_rect)
        pygame.draw.rect(screen, BLACK, item_button_rect, 2)
        screen.blit(item_button2, item_button_rect2)
        pygame.draw.rect(screen, BLACK, item_button_rect2, 2)
        screen.blit(item_button3, item_button_rect3)
        pygame.draw.rect(screen, BLACK, item_button_rect3, 2)
        screen.blit(back_button, back_button_rect)
        pygame.draw.rect(screen, BLACK, back_button_rect, 2)
        pygame.display.update()

    return {"coins":coins,"strength":strength,"health":maxHP,"speed":speed}
