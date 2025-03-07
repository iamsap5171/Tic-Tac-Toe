# Tic Tac Toe Game in Python

def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

def check_winner(board, player):
    # Check all possible winning combinations
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

def is_board_full(board):
    return all(cell != " " for cell in board)

def tic_tac_toe():
    board = [" " for _ in range(9)]  # Initialize empty board
    current_player = "X"  # Start with player X

    while True:
        print_board(board)
        print(f"Player {current_player}'s turn")

        # Get player input
        try:
            move = int(input("Enter your move (0-8): "))
            if move < 0 or move > 8:
                print("Invalid move! Please enter a number between 0 and 8.")
                continue
            if board[move] != " ":
                print("That cell is already taken! Try again.")
                continue
        except ValueError:
            print("Invalid input! Please enter a number between 0 and 8.")
            continue

        # Update the board
        board[move] = current_player

        # Check for a winner
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        # Check for a tie
        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        # Switch players
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()