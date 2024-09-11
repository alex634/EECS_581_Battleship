class Player:
    def __init__(self):
        #Board 1 and 2 will need to be initialized here
        self._board_One = [[0 for _ in range(10)] for _ in range(10)]  # Your own board (0 represents empty)
        self._board_Two = [[0 for _ in range(10)] for _ in range(10)]  # Opponent's board (tracking board)

        #Sink, hit, and over variables update every turn
        #This is true if hit, false if miss
        self.__hit = False
        #This is set to true if sunk, false if not
        self.__sink = False
        #This is true if the game is over
        self.__over = False

        
    #Coordinates will be in a tuple of form (<uppercase letter>, <number>)
    #Returns true if out of bounds, false if not
    #This does not check for existence of ships, just that the coordinate is valid
    #Within the board space
    def __bob(self, coord):
        x, y = self.__str_coord_to_xy(coord)
        return not (1 <= x <= 10 and 1 <= y <= 10)

    # takes in a tuple (<uppercase letter>, <number>)
    # returns interger repersentation of the coordinate in the XY plane
    def __str_coord_to_xy(self, coord): 
        # ord returns the interger repersentation of the ascii character
        # 64 is the offset for the A character
        x = ord(coord[0]) - 64
        y = int(coord[1])

        return x,y
        
    #Sets a coordinate on the board to a specific value
    #Point must be valid, no parameter checking should occur here
    def __add_Point(self, board, coord, value):
        x,y = self.__str_coord_to_xy(coord)
        board[y][x] = value
        
    #Returns the value at a specific point on the board.
    #Point must be valid, no parameter checking should occur here
    def __get_Point(self, board, coord):
        x,y = self.__str_coord_to_xy(coord)
        return board[y][x]
    	
    #Steps:
    #Make sure all locations the ship will exist along are valid using BOB
    #Make sure the ship doesn't overlap with any other ship
    #If this fails, raise an exception
    def add_Ship(self, board, coord, size, downright):
        # Convert coordinate to indices
        x, y = self.__str_coord_to_xy(coord)

        # Check if placing the ship would go out of bounds
        if downright == 'H':  # Horizontal placement
            # Ensure the ship fits horizontally within the board
            if x + size - 1 > 10:
                raise Exception(
                    f"Ship placement exceeds board boundaries horizontally. Try placing the ship closer to the left.")
            # Ensure no overlap with other ships
            for i in range(size):
                if self.__get_Point(board, (chr(ord(coord[0]) + i), coord[1])) != 0:
                    raise Exception("Invalid ship placement or overlap detected")
            # Place the ship
            for i in range(size):
                self.__add_Point(board, (chr(ord(coord[0]) + i), coord[1]), size)

        elif downright == 'V':  # Vertical placement
            # Ensure the ship fits vertically within the board
            if y + size - 1 > 10:
                raise Exception(
                    f"Ship placement exceeds board boundaries vertically. Try placing the ship closer to the top.")
            # Ensure no overlap with other ships
            for i in range(size):
                if self.__get_Point(board, (coord[0], str(int(coord[1]) + i))) != 0:
                    raise Exception("Invalid ship placement or overlap detected")
            # Place the ship
            for i in range(size):
                self.__add_Point(board, (coord[0], str(int(coord[1]) + i)), size)
        else:
            raise Exception("Invalid direction parameter, use 'H' or 'V'")

    # Steps:
    # Make sure point is a valid point using BOB
    # Mark location on board
    # Set hit, sink, over variables
    # If this fails, raise an exception
    def add_Shoot(self, board, coord):
        # Validate the shooting point
        if self.__bob(coord):
            raise Exception("Shot out of bounds")

        # Get the value at the shooting point
        point = self.__get_Point(board, coord)
        if point > 0:  # Hit a ship (positive value indicates a ship)
            self.__hit = True
            self.__add_Point(board, coord, -point)  # Mark as hit by setting the value to its negative counterpart
            # Check if the ship is sunk
            self.__sink = self.check_sunk(board, point)
        elif point == 0:  # Missed
            self.__hit = False
            self.__add_Point(board, coord, -6)  # Mark as miss
        else:
            raise Exception("This position has already been attacked")


    def check_sunk(self, board, ship_size):
        for row in board:
            if ship_size in row:  # If any part of the ship is still present (positive value), it's not sunk
                return False
        return True  # If no part of the ship is left, it's sunk
	
    def status(self):
        return self.__hit, self.__sink, self.__over
	
    #Returns both player's boards
    #Remember to define these in init
    def get_Boards(self):
        return self._board_One, self._board_Two

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
		
