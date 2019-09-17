#start by putting the player in tile 1,1

grid_rows = 3
grid_col = 3
#[1 rows, 1 columns]
user_pos = [1,1]

def player_location(rows, columns) :
    """Finds out if user is within the grid, player_location(position) and feed it a [1,1] position."""
    if 0 < rows < 4 and 0 < columns < 4 :
        #user is within the grid
        print('Im here')
        return True
    else:
        print('Outside of grid')
        return False

#player has to be able to input travel direction
def move_player(direction): 
    """User gives directional input, n/N, e/E, s/S, w/W"""
  # direction = input("Direction: ")
    #user cannot go outside of the grid
    if direction == "n" or direction == "N": 
        #checks if user is within grid if he moves
        if player_location(user_pos[0], user_pos[1]+1) == True:
            user_pos[1] += 1
            print(user_pos)
            print("north")
    elif direction == "e" or direction == "E": 
        #checks if user is within grid if he moves
        if player_location(user_pos[0]+1, user_pos[1]) == True:
            user_pos[0] += 1
            print(user_pos)
            print("east")
    elif direction == "s" or direction == "S": 
        #checks if user is within grid if he moves
        if player_location(user_pos[0], user_pos[1]-1) == True:
            user_pos[1] -= 1
            print(user_pos)
        print("south")
    elif direction == "w" or direction == "W": 
        #checks if user is within grid if he moves
        if player_location(user_pos[0]-1, user_pos[1]) == True:
            user_pos[0] -= 1
            print(user_pos)
        print("west")
    else: 
        print("Not a valid direction!")

direction = input("Direction: ")

move_player(direction)


