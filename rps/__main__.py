from rps import rps
from rps.scoreboard import Scoreboard


def main() -> None:
    """Main code for the game"""
    rps.clear_screen()
    input(rps.start_screen)
    rps.clear_screen()
    input(rps.rules)
    rps.clear_screen()
    input(rps.how_to)
    rps.clear_screen()

    score = Scoreboard()

    while True:
        user_input = input(rps.game_prompt)

        match user_input:
            case "1" | "2" | "3":
                winner = rps.simulate_game(user_input)
                print()
                score.handle_score(winner)
                print()
            case "Q" | "q":
                rps.clear_screen()
                score.print_final_score()
                return
            case _:
                print("Invalid input. Try again.\n")


if __name__ == "__main__":
    main()
