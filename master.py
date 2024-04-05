import random


def roll():
    min_value = 1
    max_value = 6
    return random.randint(min_value, max_value)


def print_player_turn(player_idx, player_scores):
    print(f"\nPlayer {player_idx + 1} turn has just started!\n")
    print(f"Your total score is {player_scores[player_idx]}\n")


def get_players_count():
    while True:
        try:
            players = int(input("Enter the number of players (2 - 4): "))
            if 2 <= players <= 4:
                return players
            else:
                print("Must be between 2 - 4 players.")
        except ValueError:
            print("Invalid input, try again.")


def main():
    players = get_players_count()
    max_score = 50
    player_scores = [0 for _ in range(players)]

    while max(player_scores) < max_score:
        for player_idx in range(players):
            print_player_turn(player_idx, player_scores)
            current_score = 0

            while True:
                should_roll = input("Would you like to roll (y)? ")
                if should_roll.lower() != "y":
                    break

                value = roll()
                if value == 1:
                    print("You rolled a 1! Turn done!")
                    current_score = 0
                    break
                else:
                    current_score += value
                    print(f"You rolled a: {value}")

                if current_score % 2 == 0:
                    print("Bonus! Your score is doubled.")
                    current_score *= 2
                else:
                    print("Penalty! Your score is halved.")
                    current_score /= 2

            player_scores[player_idx] += int(current_score)
            print(f"Your total score is: {player_scores[player_idx]}")

    max_score = max(player_scores)
    winning_idx = player_scores.index(max_score)
    print(f"Player {winning_idx+ 1} is the winner with a score of {max_score}")


if __name__ == "__main__":
    main()
