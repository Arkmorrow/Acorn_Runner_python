def grid_to_string(grid, player):
    """Turns a grid and player into a string

    Arguments:
        grid -- list of list of Cells
        player -- a Player with water buckets

    Returns:
        string: A string representation of the grid and player.
    """
    #show the player
    player_row = player.row
    player_col = player.col
    grid[player_row][player_col] = player

    #change grid to a single string
    string=''
    for line in grid:

        for element in line:
            string += str(element.display)
            
        string += '\n'
    
    #add a space
    string += '\n'
    
    #return the number of water buckets the player has
    if player.num_water_buckets == 1:
        msg_wb='You have {} water bucket.'.format(player.num_water_buckets)

    else:
        msg_wb='You have {} water buckets.'.format(player.num_water_buckets)
    
    #add msg to the string
    string += msg_wb
    
    return string