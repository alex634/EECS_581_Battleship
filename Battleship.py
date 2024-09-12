import re  # Import the regular expressions module for pattern matching.
import os  # Import the operating system module for clearing the terminal.
import time  # Import the time module for implementing delays.

class Player:
    def __init__(self):
        # Initialize a 10x10 board filled with zeros to represent empty cells.
        self.board = [[0]*10 for _ in range(10)]  
        # List to keep track of the ships placed by the player.
        self.ships = []  
        # Set to keep track of hit positions.
        self.hits = set()  
        # Set to keep track of miss positions.
        self.misses = set()  

    def place_ship(self, size, position, direction=None):
        """Place a ship on the board."""
        col, row = self.convert_position_to_indices(position)  # Convert the position to board indices.
        
        if size == 1:
            direction = 'H'  # For a 1x1 ship, direction is irrelevant.

        if direction == 'H':
            if col + size > 10:  # Check if the ship fits horizontally on the board.
                return False
            for i in range(size):
                if col + i >= 10 or self.board[row][col + i] != 0:  # Check if the ship overlaps with existing ships.
                    return False
            for i in range(size):
                self.board[row][col + i] = size  # Place the ship on the board horizontally.
        elif direction == 'V':
            if row + size > 10:  # Check if the ship fits vertically on the board.
                return False
            for i in range(size):
                if row + i >= 10 or self.board[row + i][col] != 0:  # Check if the ship overlaps with existing ships.
                    return False
            for i in range(size):
                self.board[row + i][col] = size  # Place the ship on the board vertically.
        else:
            return False  # Return False for invalid direction.

        self.ships.append((position, size, direction))  # Add the ship details to the player's ships list.
        return True

    def receive_shot(self, position):
        """Receive a shot on the board and return the result."""
        col, row = self.convert_position_to_indices(position)  # Convert the shot position to board indices.
        if self.board[row][col] != 0:
            self.board[row][col] = 'X'  # Mark the shot as a hit on the board.
            self.hits.add(position)  # Add the position to the hits set.
            # Check if the ship is sunk by verifying if all its parts are hit.
            if all(self.board[r][c] == 'X' for r in range(10) for c in range(10) if (self.board[r][c] == self.board[row][col])):
                return 'Sunk'  # Return 'Sunk' if the entire ship is destroyed.
            return 'Hit'  # Return 'Hit' if only part of the ship is hit.
        else:
            self.misses.add(position)  # Add the position to the misses set.
            return 'Miss'  # Return 'Miss' if no ship is hit.

    def print_board(self, reveal_ships=False):
        """Print the board. If reveal_ships is True, show ships."""
        # Print column labels from A to J.
        print("  " + " ".join(chr(ord('A') + i) for i in range(10)))
        for i in range(10):
            # Print the row label and the data for each cell in the row.
            row = str(i + 1) + " "
            for j in range(10):
                if reveal_ships:
                    cell = self.board[i][j]
                    if cell == 0:
                        row += ". "  # Print a dot for empty cells.
                    elif cell == 'X':
                        row += "X "  # Print an 'X' for hit cells.
                    else:
                        row += f"{cell} "  # Print the ship size for ship cells.
                else:
                    position = chr(ord('A') + j) + str(i + 1)
                    if position in self.hits:
                        row += "X "  # Print an 'X' for hit positions.
                    elif position in self.misses:
                        row += "O "  # Print an 'O' for miss positions.
                    else:
                        row += ". "  # Print a dot for unexplored positions.
            print(row)

    def convert_position_to_indices(self, position):
        """Convert board position from letter-number format to indices."""
        col = ord(position[0]) - ord('A')  # Convert column letter to index (0-9).
        row = int(position[1:]) - 1  # Convert row number to index (0-9).
        return col, row  # Return the column and row indices.


class Interface:
    def __init__(self):

    # prints out the game board list for debug purpose
    def __debug_show_list(self):

    # print out the game board for players
    def __show_board(self):

    # print out the hidden game board for players
    def __hidden_board(self):
        

    #This starts the entire program. The entire interface is ran from this function.
    def start(self):
		
