import pygame
#Initializing pygame is very important
pygame.init()

#This is a game window size
gamewindow = pygame.display.set_mode((1200, 600))
#This is a game window name
pygame.display.set_caption('My First Game')

#Game specific variables
exit_game = False
game_over = False

#creating loop our entire game lies in this while loop
#the condition for while loop will be, until our exit game condition is false keep running this loop
#our complete game will reside here in this loop    
while not exit_game:
    
    #this is the loop which handles all the events in the game like mouse movement, key presses etc
    for event in pygame.event.get(): #the event variabe takes all the events that user performs during the execution of this program
        if event.type == pygame.QUIT: #this condition checks the type of the event if it is QUIT which means clicking the close button from top
            exit_game = True #it will make the exit_game condition true and our program will come out of the loop
        if event.type == pygame.KEYDOWN: #if type of the event is keydown
            if event.key == pygame.K_RIGHT: #and the pressed key is pygame.K_Right
                print('You have pressed the right arrow key') #print this

                

#if our loop ends the pygame will quit & our python program will also quit
pygame.quit()
quit()
