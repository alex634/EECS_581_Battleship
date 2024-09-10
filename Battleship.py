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
		
    #Sets a coordinate on the board to a specific value
    #Point must be valid, no parameter checking should occur here
    def __add_Point(self, board, coord, value):

    #Returns the value at a specific point on the board.
    #Point must be valid, no parameter checking should occur here
    def __get_Point(self, board, coord):
    	
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
    def init(self):
	
    #This starts the entire program. The entire interface is ran from this function.
    def start(self):
		
