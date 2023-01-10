from random import choice

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


def simulate_game(user_input: str) -> int:
    """Simulates game and decides who wins

    Args:
        user_choice (int): User's choice

    Returns:
        int: Which player won, 0 = tie, 1 = user, 2 = computer
    """
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = choice(choices)
    user_choice = choice(int(user_input) - 1)

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
