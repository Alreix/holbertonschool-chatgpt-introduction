#!/usr/bin/python3

def print_board(board):
    """Print the current state of the Tic Tac Toe board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def check_winner(board):
    """Check if there is a winner on the board."""
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns
    for col in range(len(board[0])):
        if (board[0][col] == board[1][col] == board[2][col]
                and board[0][col] != " "):
            return True

    # Check diagonals
    if (board[0][0] == board[1][1] == board[2][2]
            and board[0][0] != " "):
        return True

    if (board[0][2] == board[1][1] == board[2][0]
            and board[0][2] != " "):
        return True

    return False


def board_full(board):
    """Return True if there is no empty space left on the board."""
    for row in board:
        for cell in row:
            if cell == " ":
                return False
    return True


def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)

        # Saisie sécurisée des coordonnées
        try:
            row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
            col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))
        except ValueError:
            print("Invalid input. Please enter numbers 0, 1, or 2.")
            continue

        # Vérification des limites
        if row < 0 or row > 2 or col < 0 or col > 2:
            print("Invalid coordinates. Row and column must be 0, 1, or 2.")
            continue

        # Vérifier si la case est libre
        if board[row][col] != " ":
            print("That spot is already taken! Try again.")
            continue

        # Placer le symbole du joueur
        board[row][col] = player

        # Vérifier s'il y a un gagnant
        if check_winner(board):
            print_board(board)
            print("Player " + player + " wins!")
            break

        # Vérifier le match nul (board plein sans gagnant)
        if board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        # Changer de joueur
        if player == "X":
            player = "O"
        else:
            player = "X"


tic_tac_toe()

