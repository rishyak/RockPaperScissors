from RockPaperScissors import game
from RockPaperScissors.scoreboard import Scoreboard


def main() -> None:
    """Main code for the game"""
    game.start_screen()

    score = Scoreboard()

    while True:
        user_input = input(game.game_prompt)

        match user_input:
            case "1" | "2" | "3":
                winner = game.simulate_game(user_input)
                print()
                score.handle_score(winner)
                print()
            case "Q" | "q":
                game.clear_screen()
                score.print_final_score()
                return
            case _:
                print("Invalid input. Try again.\n")


if __name__ == "__main__":
    main()
