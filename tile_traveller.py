#start by putting the player in tile 1,1

grid_rows = 3
grid_col = 3
#[1 rows, 1 columns]
user_pos = [1,1]

def player_location(row, col) :
    """Finds out if user is within the grid, player_location(position) and feed it a [1,1] position."""
    if 0 < row < 4 and 0 < col < 4 :
        #user is within the grid
        return True
    else:
        print('Outside of grid')
        return False

def move_player(current_pos, direction):
    new_pos = current_pos
    #north +
    if direction == "n":
        new_pos[1] += 1
    #south -
    elif direction == "s":
        new_pos[1] -= 1
    #east +
    elif direction == "e":
        new_pos[1] += 1
    #west -
    elif direction == "w":
        new_pos[1] -= 1
    #check if new location is within grid
    if player_location(new_pos[0], new_pos[1]) == True:
        return new_pos

#player has to be able to input travel direction
def player_direction(): 
    """User gives directional input, n/N, e/E, s/S, w/W"""
    direction = input("Direction: ").lower()
    #user cannot go outside of the grid
    if direction in ["s", "n", "e", "w"]:  
        print(move_player(user_pos, direction))
    else: 
        print("Not a valid direction!")

def possible_move(user_pos): 
    """function is given user_pos and indicates which direction player can move"""

#direction = input("Direction: ")

player_direction()


