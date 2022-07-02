# WELCOME TO MY PROGRAM
# All comments are in French, if need, contact me at: mycn18.dev@gmail.com

import time
import random

# function asking for solo IA level choose
def IA_choose():
    print("Hi, are you playing solo ? You have no choice as well, so which IA level do you take for shi fu mi? ('1', '2', '3' ?)")
    level = input("--> ")
    # securité :
    while not(level in ['1', '2', '3']):
        print("HEY YOU MADE AN ERROR PLEASE DON'T DO THAT AGAIN")
        level = input("So please retry... -->")

    print("Okay, lets go for IA level", level, ";)")
    game_start(int(level))

def AI_plays(level, L):
    if level == 1:
        return AI1(L)
    if level == 2:
        return AI2(L)
    if level == 3:
        return AI2(L)

def AI1(L):
    possibilities = ['S', 'P', 'C']
    return possibilities[random.randint(0, 2)]

def AI2(L):
    if L != []:
        return L[-1]
    return AI1(L)

def AI3(L):
    if L != []:
        return L[random.randint(0, len(L)-1)]
    return AI1(L)

def compare(player, IA):
    dict = {"SP":False, "SC":True, "PS":True, "PC":False, "CS":False, "CP":True}

    if IA == player:
        return "draw"
    else:
        if dict[player+IA]:
            return "win"
        else:
            return "lose"

def game_start(IA_level):
    L = []
    results = [0, 0]
    round = 1
    while results[0] < 2 and results[1] < 2:
        time.sleep(1)
        print("\n--Round" + str(round) + "--")
        time.sleep(1)
        print("Shi...")
        time.sleep(1)
        print("Fu...")
        time.sleep(1)
        print("Mi !")
        time.sleep(1)
        print("Choose between 'S', 'P', 'C'")
        player_input = input("--> ")

        while not(player_input in ['S', 'P', 'C']):
            print("... not a good answer...")
            player_input = input("Try again --> ")

        AI_play = AI_plays(int(IA_level), L)

        L.append(player_input)

        print("AI is playing " + AI_play)
        res = compare(player_input, AI_play)
        time.sleep(1)
        if res == "draw":
            print("It's draw !")
        elif res == "win":
            print("You won this round")
            results[0] += 1
        else:
            print("I won ^^")
            results[1] += 1
        time.sleep(1)
        print("\nscore: " + str(results[0]) + " - " + str(results[1]))
        time.sleep(1)
        round+=1


IA_choose()
