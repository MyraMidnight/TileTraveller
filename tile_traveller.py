#start by putting the player in tile 1,1

grid_rows = 3
grid_col = 3
user_pos = [1,1]

#player has to be able to input travel direction
def move_player(): 
  """User gives directional input, n/N, e/E, s/S, w/W"""
    direction = input("Direction: ")
    #user cannot go outside of the grid
    if direction == "n" or direction == "N": 
        print("north")
    elif direction == "e" or direction == "E": 
        print("east")
    elif direction == "s" or direction == "S": 
        print("south")
    elif direction == "w" or direction == "W": 
        print("west")
    else: 
        print("Not a valid direction!")

def player_location(position) :
    """Finds out if user is within the grid, player_location(position) and feed it a [1,1] position."""
    if 0 < user_pos[0] < 4 and 0 < user_pos[1] < 4 :
        #user is within the grid
        print('Im here')
        return True
    else:
        print('Outside of grid')
        return False




move_player(direction)


