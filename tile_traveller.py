#start by putting the player in tile 1,1
#player has to be able to input travel direction

def move_player(direction): 
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

direction = input("Direction: ")

move_player(direction)


