import os
from rps import rps


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
    rps.clear_screen()
    input(rps.start_screen)
    rps.clear_screen()
    input(rps.rules)
    rps.clear_screen()
    input(rps.how_to)
    rps.clear_screen()

    while True:
        user_input = input(rps.game_prompt)

        match user_input:
            case "1" | "2" | "3":
                winner = rps.simulate_game(user_input)
                print()
                handle_score(winner)
                print()
            case "Q" | "q":
                rps.clear_screen()
                print_final_score()
                return
            case _:
                print("Invalid input. Try again.\n")


if __name__ == "__main__":
    main()
