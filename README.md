Tic Tac Toe   

Creating a Tic-Tac-Toe game in Python requires handling a 3x3 grid where two players take turns to place their respective marks (X or O) and the game checks for valid moves and winning conditions.

### Features:
- **Grid System**: The game board is represented as a 3x3 grid.
- **Turns**: Two players alternate placing their marks.
- **Win Conditions**: The game checks for a win (horizontal, vertical, or diagonal) after every move.
- **Input Validation**: Players can only place their mark on empty spots.
- **Game Over**: The game ends when a player wins or when there is a draw.

### Explanation:

1. **Board Initialization**: The board is initialized as a 3x3 grid with all empty cells (' ').
2. **Board Display**: The `print_board` function prints the current state of the board in a readable format.
3. **Win Check**: The `check_win` function checks if the current player has three marks in a row (horizontally, vertically, or diagonally).
4. **Draw Check**: The `is_board_full` function checks if the board is full, which indicates a draw if no one has won.
5. **Player Input**: The `make_move` function allows players to input the row and column for their move. It ensures the move is valid (i.e., the cell is empty and the input is within the range of 0 to 2).
6. **Game Flow**: The game alternates between players 'X' and 'O' until there is a winner or a draw.

### Sample Gameplay:

```
Player X, enter row and column (0, 1, or 2) separated by space: 0 0

 |   |  
-----
  |   |  
-----
  |   |  

Player O, enter row and column (0, 1, or 2) separated by space: 1 1

X |   |  
-----
  | O |  
-----
  |   |  

Player X, enter row and column (0, 1, or 2) separated by space: 0 1

X | X |  
-----
  | O |  
-----
  |   |  

Player O, enter row and column (0, 1, or 2) separated by space: 2 0

X | X |  
-----
  | O |  
-----
O |   |  

Player X, enter row and column (0, 1, or 2) separated by space: 0 2

X | X | X
-----
  | O |  
-----
O |   |  

Player X wins!
```

### Features:
- **Dynamic Turn Switching**: The game alternates between Player X and Player O after each valid move.
- **Input Validation**: The player is prompted again if the input is invalid (e.g., entering out-of-bounds indices or selecting a non-empty cell).
- **Win Detection**: The game checks for a winner after every move, detecting horizontal, vertical, and diagonal wins.
- **Draw Detection**: If the board is full and no winner is found, the game ends in a draw.

This is a simple and functional implementation of Tic-Tac-Toe. You can enhance this game by adding a GUI (e.g., with `tkinter`) or by implementing a computer opponent.
