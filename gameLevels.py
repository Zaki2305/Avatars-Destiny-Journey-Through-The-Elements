import pygame,sys,random,CharacterObjects,BackgroundObjects

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

def level(lvlNum,character,character_attributes):
    pygame.display.set_caption(f"Level {lvlNum}")
    #use the character object class to get main character and background image
    lvl_bg_img = BackgroundObjects.Levels(screen,str(lvlNum))    
    folder_path = "characterImages/" + str(character).lower() + "Images/"
    pos = (screen.get_rect().centerx,screen.get_rect().centery*3/4)
    main_character = CharacterObjects.MainCharacter(screen,pos,folder_path,character_attributes)

    waveNum = lvlNum;

    # Set up the clock
    clock = pygame.time.Clock()

    # Create start button
    button_width = 50
    button_height = 25

    #finish button to move through the levels
    finish_button_rect = pygame.Rect(screen_width - button_width, screen_height-button_height, button_width, button_height)
    finish_button = pygame.Surface((button_width, button_height))
    finish_button.fill(WHITE)
    finish_button_text = afont(10).render("Finish Level", True, BLACK)
    finish_button_text_rect = finish_button_text.get_rect(center=finish_button.get_rect().center)
    finish_button.blit(finish_button_text, finish_button_text_rect)

    def updateTitle():
        #Title Text
        title_text = afont(100).render(f"LEVEL {lvlNum}", True, WHITE)
        text_width, text_height = title_text.get_size()
        x_pos = (screen_width - text_width) // 2  # Calculate x-coordinate of top-left corner
        y_pos = screen_height // 9  # Calculate y-coordinate of top-left corner
        screen.blit(title_text, (x_pos, y_pos))  # Blit the text at the calculated position
            
        #Wave Text
        wave_text = afont(80).render(f"Wave {lvlNum-waveNum+1}/{lvlNum+1}", True, WHITE)
        wave_text_width, wave_text_height = wave_text.get_size()
        wave_x_pos = (screen_width - wave_text_width) // 2  # Calculate x-coordinate of top-left corner
        wave_y_pos = screen_height // 4  # Calculate y-coordinate of top-left corner
        screen.blit(wave_text, (wave_x_pos, wave_y_pos))  # Blit the text at the calculated position

    updateTitle()

    monster_group = pygame.sprite.Group()
    obstacle_group = pygame.sprite.Group()


    def mob_wave(no_of_monsters,no_of_obstacles):
        if lvlNum == 1: monsterType = "earth"
        elif lvlNum == 2: monsterType = "water"
        elif lvlNum == 3: monsterType = "fire"
        else: monsterType = "air"

        for i in range(no_of_monsters):
            monster_attributes = {"health":20,"strength":5,"speed":random.uniform(1,5)}
            monster_group.add(CharacterObjects.Monster(screen,monsterType,monster_attributes))

        for i in range(no_of_obstacles):
            obstacle_attributes = {"strength":5,"speed":random.uniform(2,5)}
            obstacle_group.add(BackgroundObjects.Obstacle(screen,lvlNum,obstacle_attributes))

    mob_wave(10,5)

    running = True
    # game loop
    while running:
        # handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close_game()

            #if mousebutton is clicked
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if finish_button_rect.collidepoint(event.pos):
                        return {"coins":main_character.coins,"strength":main_character.strengthP,"health":main_character.maxHP,"speed":main_character.speed}
            #if there is mouse hovering over button
            elif event.type == pygame.MOUSEMOTION:
                if finish_button_rect.collidepoint(event.pos):
                    finish_button.fill(LIGHT_BLUE)
                    finish_button.blit(finish_button_text, finish_button_text_rect)
                else:
                    finish_button.fill(WHITE)
                    finish_button.blit(finish_button_text, finish_button_text_rect)


            # Move character with arrow keys
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z:
                    main_character.attack()
                    main_character.rect.width *= 1.5
                elif event.key == pygame.K_x:
                    main_character.block()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_z:
                    main_character.idle()
                    main_character.rect.width /= 1.5
                elif event.key == pygame.K_x:
                    main_character.unblock()
                
        for monster in monster_group:
            if pygame.sprite.collide_rect(main_character, monster):
                if main_character.current_pose == "attack":
                    main_character.update()
                    if not main_character.monster_collision_flag:
                        monster.attacked(main_character.attack())
                        if monster.healthP <= 0:
                            monster_group.remove(monster)
                            main_character.coins += 2
                        main_character.monster_collision_flag = True

                        # Stun the monster for some time after it's attacked
                        monster.stunned_time = pygame.time.get_ticks() + 1000  # Stun for 1 second
                else:
                    if not monster.attacked_this_collision:
                        if main_character.current_pose == "block":
                            main_character.update()
                            main_character.attacked(monster.attack() / 2)
                        else:
                            main_character.attacked(monster.attack())
                        monster.attacked_this_collision = True
            else:
                # Check if the monster is still stunned
                if monster.stunned_time is None or pygame.time.get_ticks() > monster.stunned_time:
                    monster.idle()
                    monster.attacked_this_collision = False
                    main_character.monster_collision_flag = False

            # if not pygame.sprite.collide_rect(main_character, monster):
            #     monster.idle()
            #     monster.attacked_this_collision = False
            #     main_character.monster_collision_flag = False


        for obstacle in obstacle_group:
            if pygame.sprite.collide_rect(obstacle, main_character):
                if main_character.current_pose == "block":
                    main_character.attacked(obstacle.attack() / 2)
                else:
                    main_character.attacked(obstacle.attack())
                obstacle_group.remove(obstacle)


        if main_character.healthP <= 0:
            main_character.die()
            return "L"


        # Fill the screen with the background image
        lvl_bg_img.updateLevel(screen)

        # Draw the character on the screen

        monster_group.update()
        monster_group.draw(screen)

        main_character.update()
        main_character.draw()

        if (lvlNum >= 2):
            obstacle_group.update()
            obstacle_group.draw(screen)
        else:
            obstacle_group.empty()

        if len(monster_group.sprites())==0 and len(obstacle_group.sprites())==0 and waveNum:
            mob_wave(10,5)
            waveNum-=1

        if len(monster_group.sprites())==0 and len(obstacle_group.sprites())==0 and not waveNum:
            return {"coins":main_character.coins,"strength":main_character.strengthP,"health":main_character.maxHP,"speed":main_character.speed}


        screen.blit(finish_button, finish_button_rect)
        pygame.draw.rect(screen, BLACK, finish_button_rect, 2)

        updateTitle()

        # Update the screen
        pygame.display.update()

        # Limit the frame rate to 60 FPS
        clock.tick(60)

    return {"coins":main_character.coins,"strength":main_character.strengthP,"health":main_character.maxHP,"speed":main_character.speed}

def finalBossLevel(character,character_attributes,boss_attributes):
    pygame.display.set_caption("Final Boss Level")
    #use the character object class to get main character and background image
    lvl_bg_img = BackgroundObjects.Levels(screen,"finalBoss")    
    folder_path = "characterImages/" + str(character).lower() + "Images/"
    folder_path_boss = "characterImages/zukoImages/"
    pos = (screen.get_rect().centerx-screen_width/4,screen.get_rect().centery*3/4)
    pos_boss = (screen.get_rect().centerx+screen_width/4,screen.get_rect().centery*3/4)
    main_character = CharacterObjects.MainCharacter(screen,pos,folder_path,character_attributes)
    final_boss = CharacterObjects.MainCharacter(screen,pos_boss,folder_path_boss,boss_attributes,True)

    # Set up the clock
    clock = pygame.time.Clock()

    # Create start button
    button_width = 50
    button_height = 25

    #finish button to move through the levels
    finish_button_rect = pygame.Rect(screen_width - button_width, screen_height-button_height, button_width, button_height)
    finish_button = pygame.Surface((button_width, button_height))
    finish_button.fill(WHITE)
    finish_button_text = afont(10).render("Finish Level", True, BLACK)
    finish_button_text_rect = finish_button_text.get_rect(center=finish_button.get_rect().center)
    finish_button.blit(finish_button_text, finish_button_text_rect)

    def updateTitle():
        #Title Text
        title_text = afont(100).render(f"FINAL BOSS LEVEL", True, WHITE)
        text_width, text_height = title_text.get_size()
        x_pos = (screen_width - text_width) // 2  # Calculate x-coordinate of top-left corner
        y_pos = screen_height // 9  # Calculate y-coordinate of top-left corner
        screen.blit(title_text, (x_pos, y_pos))  # Blit the text at the calculated position
            
    updateTitle()

    #attack, block
    #w = jump,a,s,d = back
    #make a list with all of these moves [] and then randomize which move zuko does
    #if zuko dies do return

    boss_list = ["attack", "block", "up", "left", "right","attack", "block", "left","attack", "block", "up", "left", "right","attack", "block", "left"]

    running = True
    # game loop
    while running:
        # handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close_game()

            #if mousebutton is clicked
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if finish_button_rect.collidepoint(event.pos):
                        return
            #if there is mouse hovering over button
            elif event.type == pygame.MOUSEMOTION:
                if finish_button_rect.collidepoint(event.pos):
                    finish_button.fill(LIGHT_BLUE)
                    finish_button.blit(finish_button_text, finish_button_text_rect)
                else:
                    finish_button.fill(WHITE)
                    finish_button.blit(finish_button_text, finish_button_text_rect)

            #boss_list = ["attack", "block", "up", "left", "right"] random_move
            random_move = random.choice(boss_list)
            if (random_move == "attack"):
                final_boss.attack()

            elif (random_move == "block"):
                final_boss.block()

            else:
                final_boss.move(random_move)

            # Move character with arrow keys
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z:
                    main_character.attack()
                    main_character.rect.width *= 1.5
                    #check if collision between characters
                    if main_character.rect.colliderect(final_boss.rect):
                        #if boss blocks pass 
                        if random_move == "block":
                            pass
                        #if boss does anything else do damage
                        else:
                            final_boss.attacked(main_character.attack())    
                            #while this if boss attacks take damage 
                        if random_move == "attack":
                            main_character.attacked(final_boss.attack())               
                if event.key == pygame.K_x:
                    main_character.block()
                    
            if event.type == pygame.KEYUP:
                #check if collision between characters
                if main_character.rect.colliderect(final_boss.rect):
                    #if boss attacks with no block do damage
                    if random_move == "attack":
                        main_character.attacked(final_boss.attack())
                if event.key == pygame.K_z:
                    main_character.idle()
                    main_character.rect.width /= 1.5
                if event.key == pygame.K_x:
                    main_character.unblock()

        if main_character.healthP <= 0:
            main_character.die()
            return "L"
        
        if final_boss.healthP <= 0:
            final_boss.die()
            return


        # Fill the screen with the background image
        lvl_bg_img.updateLevel(screen)

        # Draw the character on the screen
        main_character.update()
        main_character.draw()

        final_boss.updateBoss()
        final_boss.drawBoss()

        screen.blit(finish_button, finish_button_rect)
        pygame.draw.rect(screen, BLACK, finish_button_rect, 2)

        updateTitle()

        # Update the screen
        pygame.display.update()

        # Limit the frame rate to 60 FPS
        #clock.tick(60)

    return
