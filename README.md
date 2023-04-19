   # TicTacToe-in-Python-with-GUI
   
   This is a simple implementation of Tic Tac Toe game using Python and the tkinter library for building the GUI. The game can be played between two players, where each player takes turns to place their symbol (X or O) on a 3x3 grid. The game is won by the player who first gets three of their symbols in a row, either horizontally, vertically or diagonally.
  
 * How it works...
    
The program consists of two classes: TicTacToe and TicTacToeGUI.

TicTacToe class is responsible for keeping track of the game state, including the current player, the state of the board, and whether the game is over or not. The class has methods for checking for a winner, making a move, and switching the current player.

TicTacToeGUI class is responsible for creating the GUI using tkinter library. It creates a 3x3 grid of buttons, with each button representing a cell in the game board. When a button is clicked, it calls the button_clicked method of the TicTacToeGUI class, which in turn calls the make_move method of the TicTacToe class. If the move is valid, the button text is updated with the current player's symbol (X or O), and the check_for_winner method of the TicTacToe class is called to check if there is a winner. If a winner is found, a message box is displayed, and the game is over. If there is no winner yet, the switch_player method of the TicTacToe class is called to switch the current player.

The reset_game method of the TicTacToeGUI class is used to reset the game state, by creating a new instance of the TicTacToe class and resetting the button texts.

The run method of the TicTacToeGUI class is used to start the main event loop of the tkinter library.

