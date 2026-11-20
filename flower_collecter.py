# let duck/flower collect s to get score, if 
import pgzrun
import time
from random import randint
#set the screen size
WIDTH = 500
HEIGHT = 500

#set the characters
duck = Actor("duck")
gameover_img = Actor("gameover")
wizard_img = Actor("wizard")
flower = Actor("flower")
flower.x = randint(50 , WIDTH-50)
flower.y = randint(50 , HEIGHT-50)

#creating variables used in the games
score = 0
character = 0
start_time = 0
total_time= 5
time_left = total_time
time_passed = 0
game_over = False
menu = True
character_name = duck

#initial function that draw things on the screen
def draw():
    global game_over,menu,character_name

    #changing of screen between menu, gameover and in game
    if menu == True:
        screen.fill("white")
        screen.draw.text("choose your character", color = "black", topleft=(150, 150))
        duck.draw()
        duck.x = 100
        duck.y = 100
        wizard_img.draw()
        wizard_img.x = 200
        wizard_img.y = 100

    elif game_over: #To do : delete the gameover text and move the score text
        screen.fill("white")
        screen.draw.text("game over", color = "black", topleft=(150, 150))
        screen.draw.text("Score: " + str(score), color = "black", topleft=(150, 180))
        screen.draw.text("press left to menu", color = "black", topleft=(150, 210))
        gameover_img.draw()
    else:
        screen.fill("orange")
        screen.draw.text("Score: " + str(score), color = "black", topleft=(10, 10))
        screen.draw.text("time: " + str(round(time_left,1)), color = "black", topleft=(10, 30))
        if character == 1:
            character_name = wizard_img
        elif character == 2:
            character_name = duck
        character_name.draw()
        flower.draw()

#control characters movement and keep track of the score
def update():
    global score, start_time, time_left, time_passed,game_over,menu,character_name
    time_passed = time.time() - start_time
    time_left = total_time - time_passed

    if game_over == False and menu == False:
        if keyboard.left :
            character_name.x = character_name.x - 10
        if keyboard.right :
            character_name.x = character_name.x + 10
        if keyboard.down :
            character_name.y = character_name.y + 10
        if keyboard.up:
            character_name.y = character_name.y - 10
    else:
        if keyboard.left :
            menu = True

    character_name.x = max(20, min(WIDTH-20, character_name.x))
    character_name.y = max(20, min(HEIGHT-20, character_name.y))

    if character_name.colliderect(flower):
        flower.x = randint(50 , WIDTH-50)
        flower.y = randint(50 , HEIGHT-50)
        score = score + 10
        reset_time()
    if time_left > 0:
        game_over = False
    else:
        game_over = True

#reset the time 
def reset_time():
    global time_left, start_time, total_time
    start_time = time.time()
    time_left = total_time 

#choose the characters
def on_mouse_down(pos):
    global character,menu, game_over,score
    if menu == True:
        if (wizard_img.collidepoint(pos)):
            character = 1
            
        elif (duck.collidepoint(pos)):
            character = 2
        menu = False
        game_over = False
        score = 0
        reset_time()
reset_time()
pgzrun.go()