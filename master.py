import random


def roll():
    """
    Rolls a six-sided die and returns the value.

    Returns:
        int: A random integer between 1 and 6, inclusive.
    """
    return random.randint(1, 6)


def print_player_turn(player_idx, player_scores):
    """
    Prints the beginning of the player's turn and their current total score.

    Parameters:
        player_idx (int): The index of the current player.
        player_scores (list): A list containing the scores of all players.
    """
    print(f"\nPlayer {player_idx + 1} turn has just started!\n")
    print(f"Your total score is {player_scores[player_idx]}\n")


def get_players_count():
    """
    Prompts the user for the number of players (between 2 and 4) and validates input.

    Returns:
        int: The number of players, confirmed to be between 2 and 4.
    """
    while True:
        try:
            players = int(input("Enter the number of players (2 - 4): "))
            if 2 <= players <= 4:
                return players
            else:
                print("Must be between 2 - 4 players.")
        except ValueError:
            print("Invalid input, try again.")


def handle_roll(current_score):
    """
    Handles a die roll for the player, including calculating and updating the score based on the roll.

    Parameters:
        current_score (int): The player's current score before the roll.

    Returns:
        int: The player's updated score after the roll.
    """
    value = roll()
    if value == 1:
        print("You rolled a 1! Turn done!")
        return 0
    else:
        current_score += value
        print(f"You rolled a: {value}")
        current_score *= 2 if current_score % 2 == 0 else 1
        print(f"Your score is now: {current_score}")
        return current_score


def main():
    """
    The main function to execute the game logic. It initializes player scores, handles each player's turn,
    and determines the game winner.
    """
    players = get_players_count()
    max_score = 50
    player_scores = [0] * players

    while max(player_scores) < max_score:
        for player_idx, score in enumerate(player_scores):
            print_player_turn(player_idx, player_scores)
            current_score = 0

            while True:
                should_roll = input("Would you like to roll (y)? ")
                if should_roll.lower() != "y":
                    break
                current_score = handle_roll(current_score)

            player_scores[player_idx] += int(current_score)
            print(f"Your total score is: {player_scores[player_idx]}")

    max_score = max(player_scores)
    winning_idx = player_scores.index(max_score)
    print(f"Player {winning_idx + 1} is the winner with a score of {max_score}")


if __name__ == "__main__":
    main()
