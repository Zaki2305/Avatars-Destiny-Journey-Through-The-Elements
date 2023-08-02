import pygame,random

def afont(size):
    avatarFont = "fonts/Avatar_Airbender.ttf"
    afont = pygame.font.Font(avatarFont,size)
    return afont

# class character acting as a parent for hero, boss, mini boss, and monsters
class Character(pygame.sprite.Sprite):
    def __init__(self,screen,strengthP,healthP,speed):
        super().__init__()
        self.strengthP = strengthP
        self.healthP = healthP
        self.speed = speed
        self.screen = screen
        self.screen_rect = screen.get_rect()

    def update(self):
        pass


# class User for the character the user controls
class MainCharacter(Character):
    def __init__(self,screen,pos,folder_path,character_attributes,onFinalBoss=False):
        self.coins = character_attributes["coins"]
        self.strengthP = character_attributes["strength"]
        self.healthP = character_attributes["health"]
        self.speed = character_attributes["speed"]

        self.maxHP = self.healthP

        self.onFinalBoss = onFinalBoss

        super().__init__(screen,self.strengthP,self.healthP,self.speed)
        self.is_blocking=False;
        self.x = pos[0]
        self.y = pos[1]

        # loading images for the various positions the character will be in 
        self.images = {}
        self.folder_path = folder_path
        self.images["idle"] = pygame.image.load(folder_path + "idle.png").convert_alpha()
        self.images["attack"] = pygame.image.load(folder_path + "attack.png").convert_alpha()
        self.images["back"] = pygame.image.load(folder_path + "back.png").convert_alpha()
        self.images["block"] = pygame.image.load(folder_path + "block.png").convert_alpha()
        self.images["dead"] = pygame.image.load(folder_path + "dead.png").convert_alpha()
        self.images["hurt"] = pygame.image.load(folder_path + "hurt.png").convert_alpha()
        self.images["jump"] = pygame.image.load(folder_path + "jump.png").convert_alpha()

        if (onFinalBoss == True):
            self.images["attack"] = pygame.transform.flip(self.images["attack"], True, False)
            self.images["back"] = pygame.transform.flip(self.images["back"], True, False)
            self.images["block"] = pygame.transform.flip(self.images["block"], True, False)
            self.images["jump"] = pygame.transform.flip(self.images["jump"], True, False)
            self.images["idle"] = pygame.transform.flip(self.images["idle"], True, False)
            self.images["dead"] = pygame.transform.flip(self.images["dead"], True, False)
            self.images["hurt"] = pygame.transform.flip(self.images["hurt"], True, False)
            
        # idle stance of the character
        self.current_pose = "idle"
        self.image = self.images[self.current_pose]
        self.rect = self.image.get_rect(center=pos)

        self.monster_collision_flag = False

        #For Jumping
        self.jump_height = 10
        self.jump_speed = 15
        self.jumping = False
        self.jump_count = 0
        self.jump_acceleration = 2
        self.gravity = 4

        # Health Bar
        self.health_bar_length = 200
        self.health_bar_height = 10
        self.health_bar_pos = (self.screen.get_width() // 2 - self.health_bar_length // 2, 10)
        self.health_bar_color = (255, 0, 0)
    
    def set_pose(self,pose):
        #Set the character's current pose
        if pose not in self.images:
            raise ValueError(f"Pose '{pose}' not found in images.")
        self.current_pose = pose
        self.image = self.images[self.current_pose]
    
    # setting the pose based off the various movements 
    def move(self,direction):
        if direction == "up":
            self.set_pose("jump")
            self.jump()
        elif direction == "left":
            self.x -= self.speed
            self.set_pose("back")
        elif direction == "right":
            self.x += self.speed
            self.set_pose("idle")

    # setting pose if the character jumps
    def jump(self):
        if not self.jumping:
            self.set_pose("jump")
            self.jumping = True
            self.jump_count = 0

    # setting pose if the character attacks
    def attack(self):
        self.set_pose("attack")
        if self.onFinalBoss: self.updateBoss()
        else: self.update()
        return self.strengthP
    
    # setting pose if the character is idle
    def idle(self):
        self.set_pose("idle")

    # setting pose if the character gets hurt
    def attacked(self,strengthP):
        self.set_pose("hurt")
        self.healthP -= strengthP
        if self.onFinalBoss: self.updateBoss()
        else: self.update()
    
    # setting the pose when the character blocks 
    def block(self):
        self.is_blocking = True
        self.set_pose("block")
        if self.onFinalBoss: self.updateBoss()
        else: self.update()

    # setting the pose when the character unblocks (idle)
    def unblock(self):
        self.is_blocking=False
        self.set_pose("idle")
        if self.onFinalBoss: self.updateBoss()
        else: self.update()
    
    # setting the pose when the character dies
    def die(self):
        self.set_pose("dead")

    def update(self):
        #move the character horizontally
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.x > 0:
            self.move("left")
        if keys[pygame.K_RIGHT] and self.x < self.screen.get_width() - self.image.get_width():
            self.move("right")
        if keys[pygame.K_UP] and self.y > 0:
            self.move("up")

        #handle jumping and gravity
        if self.jumping:
            if self.jump_count < self.jump_height:
                if self.y < 0:
                    self.y = 0
                self.y -= self.jump_speed
                self.jump_speed -= self.jump_acceleration
                self.jump_count += 1.5
            else:
                self.jumping = False
                self.jump_count = 0
                self.jump_speed = 15
        elif self.y < self.screen.get_height() - (self.screen.get_height()/10) - self.image.get_height():
            self.y += self.gravity
                #self.y = self.screen.get_height() - (self.screen.get_height()/9) - 100

        self.rect.topleft = (self.x, self.y)
        self.draw()


    #draw character on the screen
    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))

        # draw the health bar on the top of the screen
        redBar = pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect(10, 10, 250, 20))
        greenBar = pygame.draw.rect(self.screen, (0, 255, 0), pygame.Rect(10, 10, (self.healthP/self.maxHP)*250, 20))

        #Draw Health Info
        health_img = pygame.image.load("objectsImages/health.png")
        health_img = pygame.transform.scale(health_img, (35,35))
        self.screen.blit(health_img,(redBar.right+2,redBar.top-9))
        health_text = afont(45).render(f"{self.healthP}", True, (255,255,255))
        self.screen.blit(health_text,(redBar.right+health_img.get_width(),redBar.top-6))
        buffer = redBar.right+health_img.get_width()+85

        #Draw Health Icon
        health_icon = pygame.image.load(self.folder_path + "healthIcon.png")
        health_icon = pygame.transform.scale(health_icon, (35,35))
        self.screen.blit(health_icon,(redBar.left,redBar.top-9))

        #Draw strengthP Info
        strength_img = pygame.image.load("objectsImages/strength.png")
        strength_img = pygame.transform.scale(strength_img, (35, 35))
        self.screen.blit(strength_img,(buffer,redBar.top-9))
        attack_text = afont(45).render(f"{self.strengthP}", True, (255,255,255))
        self.screen.blit(attack_text,(buffer+strength_img.get_width(),redBar.top-6))
        buffer = buffer+strength_img.get_width()+75

        #Draw Speed Info
        speed_img = pygame.image.load("objectsImages/speed.png")
        speed_img = pygame.transform.scale(speed_img, (35, 35))
        self.screen.blit(speed_img,(buffer,redBar.top-9))
        attack_text = afont(45).render(f"{self.speed}", True, (255,255,255))
        self.screen.blit(attack_text,(buffer+speed_img.get_width(),redBar.top-6))

        #Draw Coin Text
        coin_text = afont(70).render(f"{self.coins}", True, (255,255,255))
        self.screen.blit(coin_text,(self.screen.get_width()-120,self.health_bar_pos[1]-6))

    def updateBoss(self):
        #handle jumping and gravity
        if self.jumping:
            if self.jump_count < self.jump_height:
                if self.y < 0:
                    self.y = 0
                self.y -= self.jump_speed
                self.jump_speed -= self.jump_acceleration
                self.jump_count += 1.5
            else:
                self.jumping = False
                self.jump_count = 0
                self.jump_speed = 15
        elif self.y < self.screen.get_height() - (self.screen.get_height()/10) - self.image.get_height():
            self.y += self.gravity
                #self.y = self.screen.get_height() - (self.screen.get_height()/9) - 100

        self.rect.topleft = (self.x, self.y)
        self.drawBoss()


    #draw character on the screen
    def drawBoss(self):
        self.screen.blit(self.image, (self.x, self.y))

        # draw the health bar on the top of the screen
        redBar = pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect(10, 50, 250, 20))
        greenBar = pygame.draw.rect(self.screen, (0, 255, 0), pygame.Rect(10, 50, (self.healthP/self.maxHP)*250, 20))

        #Draw Health Info
        health_img = pygame.image.load("objectsImages/health.png")
        health_img = pygame.transform.scale(health_img, (35,35))
        self.screen.blit(health_img,(redBar.right+2,redBar.top-9))
        health_text = afont(45).render(f"{self.healthP}", True, (255,255,255))
        self.screen.blit(health_text,(redBar.right+health_img.get_width(),redBar.top-6))
        buffer = redBar.right+health_img.get_width()+85

        #Draw Health Icon
        health_icon = pygame.image.load(self.folder_path + "healthIcon.png")
        health_icon = pygame.transform.scale(health_icon, (35,35))
        self.screen.blit(health_icon,(redBar.left,redBar.top-9))


        #Draw strengthP Info
        strength_img = pygame.image.load("objectsImages/strength.png")
        strength_img = pygame.transform.scale(strength_img, (35, 35))
        self.screen.blit(strength_img,(buffer,redBar.top-9))
        attack_text = afont(45).render(f"{self.strengthP}", True, (255,255,255))
        self.screen.blit(attack_text,(buffer+strength_img.get_width(),redBar.top-6))
        buffer = buffer+strength_img.get_width()+75

        #Draw Speed Info
        speed_img = pygame.image.load("objectsImages/speed.png")
        speed_img = pygame.transform.scale(speed_img, (35, 35))
        self.screen.blit(speed_img,(buffer,redBar.top-9))
        attack_text = afont(45).render(f"{self.speed}", True, (255,255,255))
        self.screen.blit(attack_text,(buffer+speed_img.get_width(),redBar.top-6))
        

# class Monster for the monsters the user will be fighting 
class Monster(Character):
    def __init__(self,screen,monsterType,monster_attributes):
        self.speed = monster_attributes["speed"]
        self.strengthP = monster_attributes["strength"]
        self.healthP = monster_attributes["health"]
        self.screen = screen
        self.max_health = self.healthP

        self.images = {}
        self.images["idle"] = pygame.image.load("characterImages/"+monsterType+"Mob.png").convert_alpha()
        self.images["attack"] = pygame.image.load("characterImages/"+monsterType+"MobAttack.png").convert_alpha()

        self.current_pose = "idle"
        self.image = self.images[self.current_pose]

        self.x = random.randint(self.screen.get_width() - 100, self.screen.get_width()-self.image.get_width())
        self.y = random.randint(self.image.get_height(),self.screen.get_height()- int(self.image.get_height()/2) - int(self.screen.get_height()/6.7))
        self.pos = (self.x, self.y)

        self.rect = self.image.get_rect()

        #gather values for this set values
        super().__init__(screen, self.strengthP, self.healthP, self.speed)

        # create health bar
        self.health_bar_length = self.rect.width
        self.health_bar_height = 5
        self.health_bar_pos = (self.rect.x, self.rect.y - self.health_bar_height - 5)
        
        self.attacked_this_collision = False
        self.stunned_time = None

        
    def set_pose(self,pose):
        #Set the character's current pose
        if pose not in self.images:
            raise ValueError(f"Pose '{pose}' not found in images.")
        self.current_pose = pose
        self.image = self.images[self.current_pose]
    
    
     # setting pose if the character attacks
    def attack(self):
        self.set_pose("attack")
        self.update()
        return self.strengthP
    
    # setting pose if the character is idle
    def idle(self):
        self.set_pose("idle")

    # setting pose if the character gets hurt
    def attacked(self,damage):
        self.healthP -= damage
        if self.healthP < 0:
            self.healthP = 0
        self.healthBar = pygame.Surface((self.rect.width, 5))
        self.healthBar.fill((0, 255, 0))
        pygame.draw.rect(self.healthBar,(255,0,0),(0,0,self.rect.width*(self.healthP/self.max_health),5))


    #update monster movement
    def update(self):
        self.pos = (self.pos[0] - self.speed, self.pos[1])
        self.rect = self.image.get_rect(center=self.pos)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_q]:
            self.attacked(5)
        
        # Update health bar position
        self.health_bar_pos = (self.rect.x, self.rect.y - self.health_bar_height - 5)

        self.draw()
        # Remove monster if off-screen
        if not self.screen_rect.contains(self.rect):
            self.kill()

    #draw character on the screen
    def draw(self):
        #self.screen.blit(self.image, (self.x, self.y))
        pygame.draw.rect(self.screen, (255, 0, 0), (self.health_bar_pos[0], self.health_bar_pos[1], self.health_bar_length, self.health_bar_height))
        pygame.draw.rect(self.screen, (0, 255, 0), (self.health_bar_pos[0], self.health_bar_pos[1], self.healthP/self.max_health * self.health_bar_length, self.health_bar_height))