""" Rock, Paper, Scissors against computer """

import random
import os
import re
os.system('clear')

def game():
    choices = ["rock", "paper", "scissors", "r", "p", "s"]
    cpu_choices = choices[3::]
    score = [0,0]
    print_score(score)
    cont = "c"
    while cont != "q":
        turn = get_turn(choices)
        cpu_turn = cpu(cpu_choices)
        print(cpu_turn)

        won = winner(turn, cpu_turn)
        if won != 2:
            score[won] += 1

        print_score(score)
        cont = input("Type 'c' to continue or 'q' to quit: ")


def print_score(score):
    print(f"Score {score[0]} - {score[1]}")

def get_turn(choices):
    choice = ""
    msg = "Type rock (r), paper (p) or scissors (s):\n"
    while choice not in choices:
        choice = input(msg)
    return choice[0]

def cpu(choices):
    return random.choice(choices)

def winner(player, cpu):
    if player == cpu:
        print("Draw")
        return 2
    elif (player, cpu) in {("r","s"),("p","r"),("s","p")}:
        print("You won this round")
        return 0
    else:
        print("You lose this round")
        return 1

def main():
    print("Starting game...")
    game()
    print("Ending game...")

if __name__ == "__main__":
    main()