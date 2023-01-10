from dataclasses import dataclass


@dataclass
class Scoreboard:
    """Class to keep track of scores"""

    computer: int = 0
    user: int = 0

    def handle_score(self, winner: int) -> None:
        """Prints who wins and the score

        Args:
            winner (int): The winner of the round, 0 = tie, 1 = user, 2 = computer
        """
        if winner == 0:
            print("Tie.")
        elif winner == 1:
            self.user += 1
            print("Good job, you win!")
        else:
            self.computer += 1
            print("Computer wins.")

        print(f"Score is {self.user}-{self.computer}")

    def print_final_score(self) -> None:
        """Prints who won the game and the final score"""
        if self.user > self.computer:
            print("Congratulations! You won!")
        elif self.user < self.computer:
            print("Computer won. Good luck next time!")
        else:
            print("Draw.")

        print(f"The final score is {self.user}-{self.computer}")
