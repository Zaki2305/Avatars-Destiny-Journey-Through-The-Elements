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
GREEN = (0,255,0)

def afont(size):
    avatarFont = "fonts/Avatar_Airbender.ttf"
    afont = pygame.font.Font(avatarFont,size)
    return afont



# pick character function, for the pick character screen
def pickCharacter():
    pygame.display.set_caption("Character Picking Window")
    # setting background
    screen = pygame.display.set_mode((screen_width, screen_height))
    bg = BackgroundObjects.Levels(screen, "pickChar")

    # text to display to user
    title_text = afont(100).render("PICK A CHARACTER", True, WHITE)

    def imageChange(pathImage1,pathImage2):
        # Load the images
        image1 = pygame.image.load(pathImage1) # 373 x 271
        image2 = pygame.image.load(pathImage2)

        # Define the initial position and size of the images
        image1_rect = image1.get_rect()
        image1_rect.center = (385, 350)
        original_size1 = image1_rect.size

        image2_rect = image2.get_rect()
        image2_rect.center = (850, 350)
        original_size2 = image2_rect.size

        return [image1,image1_rect,original_size1,image2,image2_rect,original_size2]

    image1,image1_rect, original_size1,image2,image2_rect, original_size2 = imageChange("characterImages/aangIcon.png","characterImages/kataraIcon.png")

    # Define the maximum and minimum scaling factors
    max_scale = 1.5
    min_scale = 1.0
    SCALE_SPEED = 0.01

    # Create a clock object to manage the frame rate
    clock = pygame.time.Clock()

    # Create start button
    button_width = 100
    button_height = 40

    # creating the start button
    start_button_rect = pygame.Rect(screen_width/25 - button_width/25, 565, button_width, button_height)
    start_button = pygame.Surface((button_width, button_height))
    start_button.fill(WHITE)
    start_button_text = afont(20).render("Start Game", True, BLACK)
    start_button_text_rect = start_button_text.get_rect(center=start_button.get_rect().center)
    start_button.blit(start_button_text, start_button_text_rect)

    # creating the quit button
    quit_button_rect = pygame.Rect(screen_width/7 - button_width/7, 565, button_width, button_height)
    quit_button = pygame.Surface((button_width, button_height))
    quit_button.fill(WHITE)
    quit_button_text = afont(20).render("Quit Game", True, BLACK)
    quit_button_text_rect = quit_button_text.get_rect(center=quit_button.get_rect().center)
    quit_button.blit(quit_button_text, quit_button_text_rect)

    bg.update(screen)
    pygame.display.update()

    image1_clicked=False
    image2_clicked=False

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close_game()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  #check if left mouse button was pressed
                    if quit_button_rect.collidepoint(event.pos):  #check if mouse clicked on button
                        close_game()
                    if image1_rect.collidepoint(event.pos):
                        image1_clicked = True
                        image2_clicked = False
                    if image2_rect.collidepoint(event.pos):
                        image1_clicked = False
                        image2_clicked = True
                    if start_button_rect.collidepoint(event.pos):
                        if image1_clicked or image2_clicked:
                            if image1_clicked:
                                return "aang"   #return function to go to next screen
                            else:
                                return "katara"  #return function to go to next screen
            elif event.type == pygame.MOUSEMOTION:
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

        bg.update(screen)
        # Get the current position of the mouse
        mouse_pos = pygame.mouse.get_pos()

        if image1_clicked:
                image1,image1_rect, original_size1,image2,image2_rect, original_size2 = imageChange("characterImages/aangSelect.png","characterImages/kataraIcon.png")
        if image2_clicked: 
            image1,image1_rect, original_size1,image2,image2_rect, original_size2 = imageChange("characterImages/aangIcon.png","characterImages/kataraSelect.png")

        # Scale image1 based on the distance from the mouse position
        if image1_rect.collidepoint(mouse_pos):
            if not image1_clicked:
                # Calculate the scaling factor based on the distance from the center of the image
                distance_from_center = pygame.math.Vector2(mouse_pos) - pygame.math.Vector2(image1_rect.center)
                distance_factor = distance_from_center.length() / (image1_rect.width / 2)
                scaling_factor = max_scale + (min_scale - max_scale) * distance_factor

                # Scale up the image
                scaled_size = (int(original_size1[0] * scaling_factor), int(original_size1[1] * scaling_factor))
                scaled_image1 = pygame.transform.smoothscale(image1, scaled_size)
                scaled_image1_rect = scaled_image1.get_rect(center=image1_rect.center)

                # Fill the screen with the background img
                bg.update(screen)

                # Blit the scaled image
                screen.blit(scaled_image1, scaled_image1_rect)
            else:
                # Fill the screen with the background img
                bg.update(screen)
                # Blit the original image
                screen.blit(image1, image1_rect)
        else:
            # Fill the screen with the background color
            bg.update(screen)

            # Blit the original image
            screen.blit(image1, image1_rect)

        # Scale image2 based on the distance from the mouse position
        if image2_rect.collidepoint(mouse_pos):
            if not image2_clicked:
                # Calculate the scaling factor based on the distance from the center of the image
                distance_from_center = pygame.math.Vector2(mouse_pos) - pygame.math.Vector2(image2_rect.center)
                distance_factor = distance_from_center.length() / (image2_rect.width / 2)
                scaling_factor = max_scale + (min_scale - max_scale) * distance_factor

                # Scale up the image
                scaled_size = (int(original_size2[0] * scaling_factor), int(original_size2[1] * scaling_factor))
                scaled_image2 = pygame.transform.smoothscale(image2, scaled_size)
                scaled_image2_rect = scaled_image2.get_rect(center=image2_rect.center)

                # Blit the scaled image
                screen.blit(scaled_image2, scaled_image2_rect)
            else:
                screen.blit(image2, image2_rect)
        else:
            screen.blit(image2, image2_rect)   

             

        screen.blit(title_text, (screen_width/2 - title_text.get_width()/2, 50))

        screen.blit(start_button, start_button_rect)
        screen.blit(quit_button, quit_button_rect)
        
        #draw button borders
        pygame.draw.rect(screen, BLACK, start_button_rect, 2)
        pygame.draw.rect(screen, BLACK, quit_button_rect, 2)

        #update the display
        pygame.display.update()
        clock.tick(60)

    return

def customCharacter(character):
    pygame.display.set_caption("Character Customization Window")
    # setting background
    screen = pygame.display.set_mode((screen_width, screen_height))
    bg = BackgroundObjects.Levels(screen, "charCustom")

    # text to display to user
    title_text = afont(100).render("CHOOSE A SKIN", True, WHITE)

    def imageChange(pathImage1,pathImage2):
        # Load the images
        image1 = pygame.image.load(pathImage1) # 373 x 271
        image2 = pygame.image.load(pathImage2)

        # Define the initial position and size of the images
        image1_rect = image1.get_rect()
        image1_rect.center = (385, 350)
        original_size1 = image1_rect.size

        image2_rect = image2.get_rect()
        image2_rect.center = (850, 350)
        original_size2 = image2_rect.size

        return [image1,image1_rect,original_size1,image2,image2_rect,original_size2]

    skin1_path,skin2_path = "",""
    skin1Select_path,skin2Select_path = "",""
    if character == "aang":
        skin1_path,skin2_path = "characterImages/aangSk1Icon.png","characterImages/aangSk2Icon.png"
        skin1Select_path,skin2Select_path = "characterImages/aangSk1Select.png","characterImages/aangSk2Select.png"
    elif character == "katara":
        skin1_path,skin2_path = "characterImages/kataraSk1Icon.png","characterImages/kataraSk2Icon.png"
        skin1Select_path,skin2Select_path = "characterImages/kataraSk1Select.png","characterImages/kataraSk2Select.png"
    
    image1,image1_rect, original_size1,image2,image2_rect, original_size2 = imageChange(skin1_path,skin2_path)

    # Define the maximum and minimum scaling factors
    max_scale = 1.5
    min_scale = 1.0
    SCALE_SPEED = 0.01

    # Create a clock object to manage the frame rate
    clock = pygame.time.Clock()

    # Create start button
    button_width = 100
    button_height = 40

    # creating the start button
    start_button_rect = pygame.Rect(screen_width/25 - button_width/25, 565, button_width, button_height)
    start_button = pygame.Surface((button_width, button_height))
    start_button.fill(WHITE)
    start_button_text = afont(20).render("Start Game", True, BLACK)
    start_button_text_rect = start_button_text.get_rect(center=start_button.get_rect().center)
    start_button.blit(start_button_text, start_button_text_rect)

    # creating the quit button
    quit_button_rect = pygame.Rect(screen_width/7 - button_width/7, 565, button_width, button_height)
    quit_button = pygame.Surface((button_width, button_height))
    quit_button.fill(WHITE)
    quit_button_text = afont(20).render("Quit Game", True, BLACK)
    quit_button_text_rect = quit_button_text.get_rect(center=quit_button.get_rect().center)
    quit_button.blit(quit_button_text, quit_button_text_rect)

    # creating the keep current skin button
    keep_button_rect = pygame.Rect(screen_width/4 - button_width/4, 565, button_width*6, button_height)
    keep_button = pygame.Surface((button_width*6, button_height))
    keep_button.fill(WHITE)
    keep_button_text = afont(30).render("Keep Current Skin", True, BLACK)
    keep_button_text_rect = keep_button_text.get_rect(center=keep_button.get_rect().center)
    keep_button.blit(keep_button_text, keep_button_text_rect)

    pygame.display.update()

    image1_clicked=False
    image2_clicked=False
    keep_button_clicked = True

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close_game()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  #check if left mouse button was pressed
                    if quit_button_rect.collidepoint(event.pos):  #check if mouse clicked on button
                        close_game()
                    if image1_rect.collidepoint(event.pos):
                        image1_clicked = True
                        image2_clicked = False
                        keep_button_clicked = False
                    if image2_rect.collidepoint(event.pos):
                        image1_clicked = False
                        image2_clicked = True
                        keep_button_clicked = False
                    if keep_button_rect.collidepoint(event.pos):
                        image1_clicked = False
                        image2_clicked = False
                        keep_button_clicked = True
                    if start_button_rect.collidepoint(event.pos):
                        if image1_clicked or image2_clicked or keep_button_clicked:
                            if image1_clicked:
                                return str(character+"sk1")   #return function to go to next screen
                            elif image2_clicked:
                                return str(character+"sk2")  #return function to go to next screen
                            else:
                                return character
                        

            elif event.type == pygame.MOUSEMOTION:
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
                if keep_button_rect.collidepoint(event.pos):
                    keep_button.fill(LIGHT_BLUE)
                    keep_button.blit(keep_button_text, keep_button_text_rect)
                else:
                    keep_button.fill(WHITE)
                    keep_button.blit(keep_button_text, keep_button_text_rect)

        bg.update(screen)
       
        # Get the current position of the mouse
        mouse_pos = pygame.mouse.get_pos()

        if image1_clicked:
            image1,image1_rect, original_size1,image2,image2_rect, original_size2 = imageChange(skin1Select_path,skin2_path)
            keep_button.fill(WHITE)
        if image2_clicked: 
            image1,image1_rect, original_size1,image2,image2_rect, original_size2 = imageChange(skin1_path,skin2Select_path)
            keep_button.fill(WHITE)
        if keep_button_clicked:
            image1,image1_rect, original_size1,image2,image2_rect, original_size2 = imageChange(skin1_path,skin2_path)
            keep_button.fill(GREEN)


        # Scale image1 based on the distance from the mouse position
        if image1_rect.collidepoint(mouse_pos):
            if not image1_clicked:
                # Calculate the scaling factor based on the distance from the center of the image
                distance_from_center = pygame.math.Vector2(mouse_pos) - pygame.math.Vector2(image1_rect.center)
                distance_factor = distance_from_center.length() / (image1_rect.width / 2)
                scaling_factor = max_scale + (min_scale - max_scale) * distance_factor

                # Scale up the image
                scaled_size = (int(original_size1[0] * scaling_factor), int(original_size1[1] * scaling_factor))
                scaled_image1 = pygame.transform.smoothscale(image1, scaled_size)
                scaled_image1_rect = scaled_image1.get_rect(center=image1_rect.center)

                # Fill the screen with the background img
                bg.update(screen)

                # Blit the scaled image
                screen.blit(scaled_image1, scaled_image1_rect)
            else:
                # Fill the screen with the background img
                bg.update(screen)
                # Blit the original image
                screen.blit(image1, image1_rect)
        else:
            # Fill the screen with the background img
            bg.update(screen)

            # Blit the original image
            screen.blit(image1, image1_rect)

        # Scale image2 based on the distance from the mouse position
        if image2_rect.collidepoint(mouse_pos):
            if not image2_clicked:
                # Calculate the scaling factor based on the distance from the center of the image
                distance_from_center = pygame.math.Vector2(mouse_pos) - pygame.math.Vector2(image2_rect.center)
                distance_factor = distance_from_center.length() / (image2_rect.width / 2)
                scaling_factor = max_scale + (min_scale - max_scale) * distance_factor

                # Scale up the image
                scaled_size = (int(original_size2[0] * scaling_factor), int(original_size2[1] * scaling_factor))
                scaled_image2 = pygame.transform.smoothscale(image2, scaled_size)
                scaled_image2_rect = scaled_image2.get_rect(center=image2_rect.center)

                # Blit the scaled image
                screen.blit(scaled_image2, scaled_image2_rect)
            else:
                screen.blit(image2, image2_rect)
        else:
            screen.blit(image2, image2_rect)

        if keep_button_rect.collidepoint(mouse_pos):
            if not keep_button_clicked:
                keep_button.fill(LIGHT_BLUE)
                keep_button.blit(keep_button_text,keep_button_text_rect)   
            else:
                keep_button.fill(GREEN)
                keep_button.blit(keep_button_text,keep_button_text_rect)
        else:
            keep_button.blit(keep_button_text,keep_button_text_rect)


             

        screen.blit(title_text, (screen_width/2 - title_text.get_width()/2, 50))

        screen.blit(start_button, start_button_rect)
        screen.blit(quit_button, quit_button_rect)
        screen.blit(keep_button,keep_button_rect)
        
        #draw button borders
        pygame.draw.rect(screen, BLACK, start_button_rect, 2)
        pygame.draw.rect(screen, BLACK, quit_button_rect, 2)

        #update the display
        pygame.display.update()
        clock.tick(60)

    return character
