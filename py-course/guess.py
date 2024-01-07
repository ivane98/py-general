import sys
import random
from enum import Enum


def guess(name='PlayerOne'):
    game_count = 0
    player_wins = 0
    win_percent = 100

    def play_guess():
        nonlocal name
        nonlocal player_wins
        nonlocal win_percent

        playerchoice = input(
            f"\n{name}, guess which number i'm thinking of... 1, 2 or 3\n\n")

        if playerchoice not in ["1", "2", "3"]:
            print(f"{name}, please enter 1, 2, or 3.")
            return play_guess()

        player = int(playerchoice)

        computerchoice = random.choice("123")

        computer = int(computerchoice)

        print(f"\n{name}, you chose {player}.")
        print(
            f"I was thinking about the number {computer}\n"
        )

        nonlocal game_count
        game_count += 1

        def decide_winner(player, computer):
            nonlocal name
            nonlocal player_wins
            nonlocal win_percent
            if player == computer:
                player_wins += 1
                return f"🎉 {name}, you win!"
            else:
                win_percent = game_count / player_wins
                return f"Sorry, {name}. better luck next time"

        game_result = decide_winner(player, computer)

        print(game_result)

        print(f"\nGame count: {game_count}")
        print(f"\n{name}'s wins: {player_wins}")
        print(f"\nYour winning percentage: {win_percent}%")

        print(f"\nPlay again, {name}?")

        while True:
            playagain = input("\nY for Yes or \nQ to Quit\n")
            if playagain.lower() not in ["y", "q"]:
                continue
            else:
                break

        if playagain.lower() == "y":
            return play_guess()
        else:
            print("\n🎉🎉🎉🎉")
            print("Thank you for playing!\n")
            sys.exit(f"Bye {name}! 👋")

    return play_guess


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personalized game experience."
    )

    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="The name of the person playing the game."
    )

    args = parser.parse_args()

    guessing_game = guess(args.name)
    guessing_game()
