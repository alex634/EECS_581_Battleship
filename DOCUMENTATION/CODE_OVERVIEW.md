## Class Descriptions

### Player

The `Player` class represents an individual player in the Battleship game. Each player has their own board, where they place their ships and record the opponent’s hits or misses.

#### Attributes

- `self.name`: Stores the name of the player.
- `self.board`: A 2D list representing the player's board where ships are placed and shots are recorded.
- `self.ships`: A dictionary that keeps track of the ships owned by the player and their respective sizes.
- `self.hits`: A list that records the coordinates of successful hits made by the player.

#### Functions

- **`place_ship(self, ship_size, start, direction)`**
  - **Input Variables:**
    - `ship_size`: The size of the ship to be placed.
    - `start`: A tuple representing the starting coordinate `(row, column)` for placing the ship.
    - `direction`: A string ('H' for horizontal, 'V' for vertical) representing the direction in which the ship will be placed.
  - **Purpose:** Places a ship of the given size on the player's board starting from the given coordinate in the specified direction. The function checks if the placement is valid (i.e., within bounds and not overlapping with other ships).

- **`receive_shot(self, coordinate)`**
  - **Input Variables:**
    - `coordinate`: A tuple representing the `(row, column)` coordinates of the shot fired by the opponent.
  - **Purpose:** Processes a shot at the given coordinate on the player's board. It checks whether the shot hits or misses a ship and updates the board accordingly.

- **`all_ships_sunk(self)`**
  - **Purpose:** Returns `True` if all ships have been sunk, indicating the player has lost the game. This function checks the status of all ships to determine if they have been completely destroyed.

- **`record_hit(self, coordinate)`**
  - **Input Variables:**
    - `coordinate`: A tuple representing the coordinate of the hit.
  - **Purpose:** Adds the given coordinate to the list of successful hits. This helps track the hits made by the player for scorekeeping or strategy planning.

### Interface

The `Interface` class handles the interaction between the players and the game. It manages game flow, player input, and displays the status of the game boards.

#### Attributes

- `self.players`: A list containing the two player objects.
- `self.current_player`: Tracks which player is currently taking their turn.
- `self.other_player`: Tracks the opponent of the current player.

#### Functions

- **`game_setup(self)`**
  - **Purpose:** Sets up the game by prompting each player to place their ships on their respective boards. It also initializes the player objects and their boards.

- **`take_turn(self)`**
  - **Purpose:** Manages the flow of a single turn, where the current player fires a shot at the opponent's board. This function gathers input, checks for hits or misses, and switches the turn to the other player.

- **`check_winner(self)`**
  - **Purpose:** Determines if the game has been won by checking if all ships of the opponent have been sunk. If so, it announces the winner.

- **`switch_player(self)`**
  - **Purpose:** Switches the turn to the next player. This ensures that after one player takes their turn, control of the game shifts to the opponent.

- **`clear_terminal_with_countdown(self)`**
  - **Purpose:** Clears the terminal screen and initiates a countdown before the next player's turn starts. This adds an element of suspense and ensures that each player’s moves remain hidden from the opponent.

- **`display_boards(self)`**
  - **Purpose:** Displays both the player's own board and their opponent’s board. The player’s board shows their ships and hits, while the opponent’s board displays the hits and misses they've made.
