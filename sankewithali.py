import pygame
import random
pygame.init()

#gamewindow
set_width = 400
set_height = 600
game_window = pygame.display.set_mode((set_width, set_height))
pygame.display.set_caption("SnakeWithAli")

#definingcolors
white = 255, 255, 255
red = 255, 0, 0
black = 0,0,0


#game specific variables
exit_game=False
quit_game=False
#snakeshead size and position
snake_x = 45
snake_y = 55
snakesize = 20
fps = 30
velocity_x = 0
velocity_y = 0
init_vel = 5 #by which the snake moves
sensitivity = 10 #distance below which the food will be eaten

score = 0
snake_speed = 5 #to display snake speed on screen just for fun
print("Score", score)
print("Snake Speed", snake_speed)

food_x = random.randint(10, set_width-10) 
food_y = random.randint(10, set_height-10)
clock = pygame.time.Clock() #defining game clock, clock means that we have to define the speed of the gameloop to run in a single second
font = pygame.font.SysFont(None, 55) #it is a pygame internal feature for fonts selection
def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    game_window.blit(screen_text,[x,y]) #Blit function does print all the strings defined in the variable
    #Text should be a string if you have your string in a varibale then typecast it

#gameloop
while not exit_game:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit_game=True
        # defining movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                velocity_x=init_vel
                velocity_y = 0
                
            if event.key == pygame.K_LEFT:
                velocity_x=-init_vel
                velocity_y = 0
                
            if event.key == pygame.K_UP:
                velocity_y=-init_vel
                velocity_x = 0
                
            if event.key == pygame.K_DOWN:
                velocity_y=init_vel
                velocity_x = 0
    
    #our game objects reside like this

    #this velocity keeps of adding
    snake_x += velocity_x
    snake_y += velocity_y

    #eating food and changing position of food
    if abs(snake_x-food_x)<sensitivity and abs(snake_y-food_y)<sensitivity:
        food_x = random.randint(10, set_width-30) 
        food_y = random.randint(10, set_height-30)
        score += 10
        #print("Score", score)
        snake_speed += 5
        print("Snake Speed", snake_speed)
        init_vel += 0.2

    game_window.fill(white)
    text_screen("Score:"+str(score), red, 5,5)
    #creating rectangle for snakes head
    pygame.draw.rect(game_window, red, [food_x, food_y, snakesize, snakesize])
    pygame.draw.rect(game_window, black, [snake_x, snake_y, snakesize, snakesize])
    pygame.display.update() #this funtion here updates our pygame window with each loop
    
    clock.tick(fps)
