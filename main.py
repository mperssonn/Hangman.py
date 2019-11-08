import pygame
import sys
import time
from pygame.locals import K_q, K_w, K_e, K_r, K_t, K_y, K_u, K_i, K_o, K_p, K_a, K_s, K_d, K_f, K_g, \
    K_h, K_j, K_k, K_l, K_z, K_x, K_c, K_v, K_b, K_n, K_m

pygame.init()
pygame.mixer.init()
window_Width = 1150
window_Height = 600
windowSize = (window_Width, window_Height)
screen = pygame.display.set_mode(windowSize)
clock = pygame.time.Clock()

##########
# ASSETS #
##########

hangman_0_wrong_image = pygame.image.load("Hangman_assets/Hangman_0_Wrong.png")
hangman_1_wrong_image = pygame.image.load("Hangman_assets/hangman_1_Wrong.png")

hangman_startermenu = pygame.image.load("Hangman_assets/Hangman_Startermenu.png")
hangman_line = pygame.image.load("Hangman_assets/hangman_line.png")

#############
# VARIABLES #
#############

game_started = False
alive = False
guess_delay_activated = True
wrong_answers = 0
word_to_guess = ""
guess = ""
line_pos_y = window_Height - 60

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == 113:
                if not game_started and not alive:
                    word_to_guess += "q"
                guess = "q"
            if event.key == 119:
                if not game_started and not alive:
                    word_to_guess += "w"
                guess = "w"
            if event.key == 101:
                if not game_started and not alive:
                    word_to_guess += "e"
                guess = "e"
            if event.key == 114:
                if not game_started and not alive:
                    word_to_guess += "r"
                guess = "r"
            if event.key == 116:
                if not game_started and not alive:
                    word_to_guess += "t"
                guess = "t"
            if event.key == 121:
                if not game_started and not alive:
                    word_to_guess += "y"
                guess = "y"
            if event.key == 117:
                if not game_started and not alive:
                    word_to_guess += "u"
                guess = "u"
            if event.key == 105:
                if not game_started and not alive:
                    word_to_guess += "i"
                guess = "i"
            if event.key == 111:
                if not game_started and not alive:
                    word_to_guess += "o"
                guess = "o"
            if event.key == 112:
                if not game_started and not alive:
                    word_to_guess += "p"
                guess = "p"

            if event.key == 97:
                if not game_started and not alive:
                    word_to_guess += "a"
                guess = "a"
            if event.key == 115:
                if not game_started and not alive:
                    word_to_guess += "s"
                guess = "s"
            if event.key == 100:
                if not game_started and not alive:
                    word_to_guess += "d"
                guess = "d"
            if event.key == 102:
                if not game_started and not alive:
                    word_to_guess += "f"
                guess = "f"
            if event.key == 103:
                if not game_started and not alive:
                    word_to_guess += "g"
                guess = "g"
            if event.key == 104:
                if not game_started and not alive:
                    word_to_guess += "h"
                guess = "h"
            if event.key == 106:
                if not game_started and not alive:
                    word_to_guess += "j"
                guess = "j"
            if event.key == 107:
                if not game_started and not alive:
                    word_to_guess += "k"
                guess = "k"
            if event.key == 108:
                if not game_started and not alive:
                    word_to_guess += "l"
                guess = "l"

            if event.key == 122:
                if not game_started and not alive:
                    word_to_guess += "z"
                guess = "z"
            if event.key == 120:
                if not game_started and not alive:
                    word_to_guess += "x"
                guess = "x"
            if event.key == 99:
                if not game_started and not alive:
                    word_to_guess += "c"
                guess = "c"
            if event.key == 118:
                if not game_started and not alive:
                    word_to_guess += "v"
                guess = "v"
            if event.key == 98:
                if not game_started and not alive:
                    word_to_guess += "b"
                guess = "b"
            if event.key == 110:
                if not game_started and not alive:
                    word_to_guess += "n"
                guess = "n"
            if event.key == 109:
                if not game_started and not alive:
                    word_to_guess += "m"
                guess = "m"

            if event.key == 13:
                game_started = True
                alive = True






    ####################
    # CALC WORD LENGTH #
    ####################

    word_length = len(word_to_guess)


    #############
    # BLIT LINE #
    #############

    def print_line(line_x):
        screen.blit(hangman_line, (line_x, line_pos_y))


    ###############
    # CHECK GUESS #
    ###############
    if game_started and alive:
        if guess_delay_activated:
            guess = "!!!"
            guess_delay_activated = False
        if guess == "!!!":
            pass
        elif guess in word_to_guess:
            print("Correct!")
        elif guess not in word_to_guess:
            print("Wrong!")
            wrong_answers = 1
        elif guess == "!!!":
            pass


    ############
    # GRAPHICS #
    ############

    screen.fill(0)

    if not game_started and not alive:
        screen.blit(hangman_startermenu, (0, 0))

    elif game_started and alive:
        if wrong_answers == 0:
            screen.blit(hangman_0_wrong_image, (0, 0))
        elif wrong_answers == 1:
            screen.blit(hangman_1_wrong_image, (0, 0))


        if word_length == 1:
            print_line(60)
        elif word_length == 2:
            print_line(60)
            print_line(120)
        elif word_length == 3:
            print_line(60)
            print_line(120)
            print_line(180)
        elif word_length == 4:
            print_line(60)
            print_line(120)
            print_line(180)
            print_line(240)
        elif word_length == 5:
            print_line(60)
            print_line(120)
            print_line(180)
            print_line(240)
            print_line(300)
        elif word_length == 6:
            print_line(60)
            print_line(120)
            print_line(180)
            print_line(240)
            print_line(300)
            print_line(360)
        elif word_length == 7:
            print_line(60)
            print_line(120)
            print_line(180)
            print_line(240)
            print_line(300)
            print_line(360)
            print_line(420)
        elif word_length == 8:
            print_line(60)
            print_line(120)
            print_line(180)
            print_line(240)
            print_line(300)
            print_line(360)
            print_line(420)
            print_line(480)
        elif word_length == 9:
            print_line(60)
            print_line(120)
            print_line(180)
            print_line(240)
            print_line(300)
            print_line(360)
            print_line(420)
            print_line(480)
            print_line(540)
        elif word_length == 10:
            print_line(60)
            print_line(120)
            print_line(180)
            print_line(240)
            print_line(300)
            print_line(360)
            print_line(420)
            print_line(480)
            print_line(540)
            print_line(600)

        # print(pygame.mouse.get_pos())
        print(word_to_guess, wrong_answers, guess)


    pygame.display.update()
