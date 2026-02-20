import random

# Define snakes and ladders
snakes = {
    16: 6,
    47: 26,
    49: 11,
    56: 53,
    62: 19,
    64: 60,
    87: 24,
    93: 73,
    95: 75,
    98: 78
}

ladders = {
    1: 38,
    4: 14,
    9: 31,
    21: 42,
    28: 84,
    36: 44,
    51: 67,
    71: 91,
    80: 100
}

def play_game():
    print("===== SNAKE AND LADDER GAME =====")

    num_players = int(input("Enter number of players: "))
    players = {}

    for i in range(1, num_players + 1):
        name = input(f"Enter name for Player {i}: ")
        players[name] = 0

    move_history = {name: [] for name in players}

    winner = None

    while not winner:
        for player in players:
            input(f"\n{player}'s turn! Press Enter to roll dice...")
            dice = random.randint(1, 6)
            print(f"{player} rolled: {dice}")

            new_position = players[player] + dice

            # Exact win condition
            if new_position > 100:
                print("Move exceeds 100! Try again next turn.")
                continue

            print(f"{player} moves from {players[player]} to {new_position}")
            players[player] = new_position

            # Check for snake
            if new_position in snakes:
                print(f"🐍 Oh no! Bitten by snake! Down to {snakes[new_position]}")
                players[player] = snakes[new_position]

            # Check for ladder
            elif new_position in ladders:
                print(f"🪜 Yay! Climbed ladder! Up to {ladders[new_position]}")
                players[player] = ladders[new_position]

            move_history[player].append(players[player])

            print(f"{player}'s current position: {players[player]}")

            if players[player] == 100:
                winner = player
                break

    print("\n🎉 Congratulations!", winner, "wins the game!")
    print("\n===== MOVE HISTORY =====")
    for player in move_history:
        print(player, ":", move_history[player])


if __name__ == "__main__":
    play_game()