import os
from random import choice
from RockPaperScissors.scoreboard import Scoreboard
from RockPaperScissors.prompts import start, rules, how_to, game_prompt


def clear_screen() -> None:
    """Clears terminal screen"""
    os.system("cls" if os.name == "nt" else "clear")


def start_screen() -> None:
    """Show start screen prompts"""
    clear_screen()
    input(start)
    clear_screen()
    input(rules)
    clear_screen()
    input(how_to)
    clear_screen()


def simulate_game(user_input: str) -> int:
    """Simulates game and decides who wins

    Args:
        user_choice (int): User's choice

    Returns:
        int: Which player won, 0 = tie, 1 = user, 2 = computer
    """
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = choice(choices)
    user_choice = choices[int(user_input) - 1]

    print(f"You chose {user_choice}")
    print(f"Computer chose {computer_choice}")

    if user_choice == computer_choice:
        return 0
    elif user_choice == "Rock" and computer_choice == "Scissors":
        return 1
    elif user_choice == "Paper" and computer_choice == "Rock":
        return 1
    elif user_choice == "Scissors" and computer_choice == "Paper":
        return 1
    else:
        return 2


def play():
    """Function to repeatedly play rock paper scissors"""
    start_screen()

    score = Scoreboard()

    while True:
        user_input = input(game_prompt)

        match user_input:
            case "1" | "2" | "3":
                winner = simulate_game(user_input)
                print()
                score.handle_score(winner)
                print()
            case "Q" | "q":
                clear_screen()
                score.print_final_score()
                return
            case _:
                print("Invalid input. Try again.\n")
