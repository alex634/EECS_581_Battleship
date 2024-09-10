class Player:
    def __init__(self):
        #Board 1 and 2 will need to be initialized here

        #Sink, hit, and over variables update every turn
        #This is true if hit, false if miss
        self.__hit = false
        #This is set to true if sunk, false if not
        self.__sink = false
        #This is true if the game is over
        self.__over = false

        
    #Coordinates will be in a tuple of form (<uppercase letter>, <number>)
    #Returns true if out of bounds, false if not
    #This does not check for existence of ships, just that the coordinate is valid
    #Within the board space
    def __bob(self, coord):

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

    #Steps:
    #Make sure point is a valid point using BOB
    #Mark location on board
    #Set hit, sink, over variables
    #If this fails, raise an exception
    def add_Shoot(self, board, coord):
	
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
		
