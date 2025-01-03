# Tic-Tac-Toe Game

# Function to initialize the game board
def initialize_board():
    return [[' ' for _ in range(3)] for _ in range(3)]

# Function to print the game board
def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

# Function to check if a player has won
def check_win(board, player):
    # Check rows, columns, and diagonals
    for row in board:
        if row.count(player) == 3:
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# Function to check if the board is full (for draw condition)
def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

# Function to handle a player's move
def make_move(board, player):
    while True:
        try:
            row, col = map(int, input(f"Player {player}, enter row and column (0, 1, or 2) separated by space: ").split())
            if board[row][col] == ' ':
                board[row][col] = player
                break
            else:
                print("Cell is already occupied. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter row and column values between 0 and 2.")

# Main function to run the game
def play_game():
    board = initialize_board()
    current_player = 'X'

    while True:
        print_board(board)
        make_move(board, current_player)
        
        # Check if the current player has won
        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        
        # Check for draw
        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break
        
        # Switch player
        current_player = 'O' if current_player == 'X' else 'X'

# Run the game
if __name__ == "__main__":
    play_game()
