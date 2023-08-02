import pygame 
import charCustomWindows,entryExitWindows,gameLevels,informativeWindows,shop,transitionWindow



def startGame():
    # function to navigate through the levels and shop from the transition windowz
    def loop_between_levels(lvl,character,character_att,finalBoss_att = None):
        while True:
            trans = transitionWindow.transitionWindow()
            if trans == "shop":
                character_att = shop.shop(character_att)
            elif trans == "howToPlay":
                informativeWindows.howToPlayWindow()
            elif trans == "next":
                if lvl=="finalBoss":
                    informativeWindows.finalBossText()
                    character = charCustomWindows.customCharacter(character)
                    character_att = gameLevels.finalBossLevel(character,character_att, finalBoss_att)
                else:
                    character_att = gameLevels.level(lvl,character,character_att)
                if character_att == "L":
                    end = entryExitWindows.finish(0)
                    if end == "restart":
                        startGame()
                break       
        return character_att


    pygame.init()
    # creating the start window
    while True:
        howToPlay = entryExitWindows.createStartWindow()
        if howToPlay == "howToPlay":
            informativeWindows.howToPlayWindow()
        else:
            break
    
    
    informativeWindows.GameIntro()
    # creating the character window and defining the character
    character = charCustomWindows.pickCharacter()
    # starting the game at level one with the character and 1st level
    character_attributes = {"coins":0,"strength":10,"health":100,"speed":10}
    finalBoss_attributes = {"coins":0,"strength":30,"health":250,"speed":14}
    character_attributes = gameLevels.level(1,character,character_attributes)
    if character_attributes == "L":
        end = entryExitWindows.finish(0)
        if end == "restart":
            startGame()
    # creating the other levels for navigation
    character_attributes = loop_between_levels(2,character,character_attributes)
    character_attributes = loop_between_levels(3,character,character_attributes)
    character_attributes = loop_between_levels(4,character,character_attributes)
    character_attributes = loop_between_levels("finalBoss",character,character_attributes,finalBoss_attributes)

    end = entryExitWindows.finish(1)
    if end == "restart":
        startGame()

    pygame.quit()


startGame()
