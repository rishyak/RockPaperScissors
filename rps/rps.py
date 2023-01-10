from random import choice


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
