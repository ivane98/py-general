import sys
import random
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


print('')
player_choice = input("choose 1 for Rock\n 2 for Paper \n 3 for Scissors")

player = int(player_choice)

if player < 1 or player > 3:
    sys.exit("Not a valid num")

computer_choice = random.choice("123")

computer = int(computer_choice)

print(f"you chose {str(RPS(player)).replace('RPS.', '')}")

print(f"computer chose {str(RPS(computer)).replace('RPS.', '')}")

if player == 1 and computer == 3:
    print("👏 You won")
elif player == 2 and computer == 1:
    print("👏 You won")
elif player == 3 and computer == 2:
    print("👏 You won")
else:
    print("🐍Computer won")
