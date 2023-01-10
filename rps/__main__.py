import os
from rps import rps

start_screen = """Welcome to Rock Paper Scissors!

Rock Paper Scissors is a simple game played between two players. 

It has three possible outcomes: Win, Loss, Draw.

The rules are quite simple. 

Press Enter to continue. 
"""

rules = """Both players make a choice and reveal their choices simultaneously.

All you need to remember is:
    - Rock beats Scissors
    - Paper beats Rock
    - Scissors beat Paper

The player with the winning object is awarded one point.

If both players play the same object, such as rock-rock, then it's a tie. 
No points are awarded in case of a tie.

Press Enter to continue.
"""

how_to = """Controls:
    - 1: Rock
    - 2: Paper
    - 3: Scissors
    - Q/q: Quit

To confirm your choice after selecting, press "Enter" or "Return".

Press Enter to start. Good luck!
"""

game_prompt = """Make your selection.
1: Rock
2: Paper
3: Scissors
Q/q: Quit

To confirm your choice after selecting, press "Enter" or "Return".

"""


def clear_screen() -> None:
    """Clears terminal screen"""
    os.system("cls" if os.name == "nt" else "clear")


scoreboard = {
    "User": 0,
    "Computer": 0,
}


def handle_score(winner: int) -> None:
    """Prints who wins and the score

    Args:
        winner (int): The winner of the round, 0 = tie, 1 = user, 2 = computer
    """
    if winner == 0:
        print("Tie.")
    elif winner == 1:
        scoreboard["User"] += 1
        print("Good job, you win!")
    else:
        scoreboard["Computer"] += 1
        print("Computer wins.")

    print(f"Score is {scoreboard['User']}-{scoreboard['Computer']}")


def print_final_score() -> None:
    """Prints who won the game and the final score"""
    if scoreboard["User"] > scoreboard["Computer"]:
        print("Congratulations! You won!")
    elif scoreboard["User"] < scoreboard["Computer"]:
        print("Computer won. Good luck next time!")
    else:
        print("Draw.")

    print(f"The final score is {scoreboard['User']}-{scoreboard['Computer']}")


def main() -> None:
    """Main code for the game"""
    clear_screen()
    input(start_screen)
    clear_screen()
    input(rules)
    clear_screen()
    input(how_to)
    clear_screen()

    while True:
        user_input = input(game_prompt)

        match user_input:
            case "1" | "2" | "3":
                winner = rps.simulate_game(user_input)
                print()
                handle_score(winner)
                print()
            case "Q" | "q":
                clear_screen()
                print_final_score()
                return
            case _:
                print("Invalid input. Try again.\n")


if __name__ == "__main__":
    main()
