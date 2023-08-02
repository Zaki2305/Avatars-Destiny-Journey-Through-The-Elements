import pygame,random

def afont(size):
    avatarFont = "fonts/Avatar_Airbender.ttf"
    afont = pygame.font.Font(avatarFont,size)
    return afont

# class to backgrounds depending on the screen
class Background():
    def __init__(self, screen, img_path):
        bg_img = pygame.image.load(img_path)
        self.bg_img = pygame.transform.scale(bg_img, (screen.get_width(), screen.get_height()))
        screen.blit(self.bg_img, (0, 0))

class Ground():
    def __init__(self,screen,img_path):
        gr_img = pygame.image.load(img_path)
        self.gr_img = pygame.transform.scale(gr_img,(screen.get_width(),screen.get_height()/8))
        self.gr_img_rect = self.gr_img.get_rect()
        self.gr_img_rect.bottomleft = (0,screen.get_height())
        screen.blit(self.gr_img,(screen.get_width(),screen.get_height()))

# Levels class for all of the different backgrounds to be updated 
class Levels():
    def __init__(self,screen,lvl):
        lvl = str(lvl)
        self.ground = None
        self.coin_banner_image = pygame.image.load("objectsImages/coin_banner.png")
        self.coin_banner_image = pygame.transform.scale(self.coin_banner_image,(screen.get_width()/5,screen.get_height()/11))
        self.coin_banner_rect = self.coin_banner_image.get_rect()
        self.coin_banner_rect.topright = (screen.get_width(),0)

        #startWindow
        if (lvl=="start"):
            self.background = Background(screen,"backgroundImages/avatarStartScreen.png")

        #lvlOne = earth
        elif (lvl=="1"):
            self.background = Background(screen,"backgroundImages/earthBackground.jpg")
            self.ground = Ground(screen,"groundImages/earthGround.png")

        #lvlTwo = water
        elif (lvl=="2"):
            self.background = Background(screen,"backgroundImages/waterBackground.jpg")
            self.ground = Ground(screen,"groundImages/waterGround.png")

        #lvlThree = fire
        elif (lvl=="3"):
            self.background = Background(screen,"backgroundImages/firebackground.jpg")
            self.ground = Ground(screen,"groundImages/fireGround.png")

        #lvlFour = air
        elif (lvl=="4"):
            self.background = Background(screen,"backgroundImages/airbackground.jpg")
            self.ground = Ground(screen,"groundImages/airGround.png")

        #lvlFive = spirit
        elif (lvl=="finalBoss"):
            self.background = Background(screen,"backgroundImages/spiritBackground.png")
            self.ground = Ground(screen,"groundImages/spiritGround.png")

        elif (lvl=="howToPlay"):
            self.background = Background(screen,"backgroundImages/howToPlay.png")

        #shop
        elif (lvl=="shop"):
            self.background = Background(screen,"backgroundImages/shop.png")

        #pick character
        elif (lvl=="pickChar"):
            self.background = Background(screen,"backgroundImages/pickCharacter.jpg")

        #character customization
        elif (lvl=="charCustom"):
            self.background = Background(screen,"backgroundImages/characterCustom.jpg")


        #transitionWindow
        elif (lvl=="transition"):
            self.background = Background(screen,"backgroundImages/transitionwindow.jpg")

        #finishWin
        elif (lvl=="finishWin"):
            self.background = Background(screen,"backgroundImages/finalBackground.png")
        
        #finishLose
        elif (lvl=="finishLose"):
            self.background = Background(screen,"backgroundImages/gameOver.jpg")

        #introText
        elif (lvl=="introText"):
            self.background = Background(screen,"backgroundImages/introBackground.png")

        #finalText
        elif (lvl=="finalText"):
            self.background = Background(screen,"backgroundImages/finalText.jpg")
        


    def update(self, screen):
        screen.blit(self.background.bg_img, self.background.bg_img.get_rect())
    
    def updateLevel(self,screen):
        screen.blit(self.background.bg_img, self.background.bg_img.get_rect())
        screen.blit(self.ground.gr_img, self.ground.gr_img_rect)
        screen.blit(self.coin_banner_image,self.coin_banner_rect)

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, screen,lvl,obstacle_attributes):
        super().__init__()
        self.image = pygame.image.load("objectsImages/waterObstacle.png")

        #lvlThree = fire
        if (lvl==3):
            self.image = pygame.image.load("objectsImages/fireObstacle.png")

        #lvlFour = air
        elif (lvl==4):
            self.image = pygame.image.load("objectsImages/airObstacle.png")
        self.screen = screen

        self.speed = obstacle_attributes["speed"]
        self.strengthP = obstacle_attributes["strength"]
        
        self.screen_rect = screen.get_rect()
        self.x = random.randint(self.screen.get_width() - 100, self.screen.get_width()-self.image.get_width())
        self.y = random.randint(self.image.get_height(),self.screen.get_height()- int(self.image.get_height()/2) - int(self.screen.get_height()/6.7))
        self.pos = (self.x, self.y)
        self.rect = self.image.get_rect()

        self.attacked_this_collision = False

    # setting pose if the character attacks
    def attack(self):
        self.update()
        return self.strengthP

    def update(self):
        self.pos = (self.pos[0] - self.speed, self.pos[1])
        self.rect = self.image.get_rect(center=self.pos)

        if not self.screen_rect.contains(self.rect):
            self.kill()
