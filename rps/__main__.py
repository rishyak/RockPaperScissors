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


def main():
    pass


if __name__ == "__main__":
    main()
