
from game import Game,Teleport
import sys


def solve(mode,filename):
    """input the mode and return the path points"""

    #set a new start of Game class and start position and end position as tuple
    game = Game(filename)
    start_pos = (game.start_pos[0],game.start_pos[1])
    end_pos = (game.end_pos[0],game.end_pos[1])
    game_end = False
    water_pos = None
    check_if_more_fire= False
    shortest_path = [start_pos]
    
    # set a counter to finding the position of the water cell if have
    position = [0,0]
    count_row = 0
    count_cel = 0

    #finding the position of the water cell if have
    for row in game.grid:

        for cel in row:

            if cel.display == 'W':
                position[0] = count_row
                position[1] = count_cel
                water_pos = (position[0],position[1])

            count_cel += 1

        count_cel = 0
        count_row += 1
 
    """finding the path if DFS"""
    if mode == 'DFS':

        #set search start from the end to the start
        shortest_path_to_water=[]
        check_if_step_fire = False
        visited = {end_pos: None}
        find_water =False
        path = [end_pos]

        #keep lopping if path is not None
        while path:

            #pop the first value in the list and set a new game
            current = path.pop(-1)
            game = Game(filename)
            game.update_player(current,filename)

            #find the path to the water cell if need
            if current == water_pos and game_end == False and find_water ==True:
                
                shortest_path_to_water = []
                
                #add to the path list if current in visited is not None
                while current:

                    current = visited[current]

                    if current:
                        shortest_path_to_water.append(current)

                #re set the visited and find the path start from the water position to end
                find_water =False
                visited = {water_pos: None}
                path = [water_pos]
                continue
 
            #find the path to the starting cell
            if current == start_pos and game_end == False and find_water ==False\
                 and check_if_more_fire ==False:
                
                #add to the path list if current in visited is not None
                while current:

                    current = visited[current]

                    if current:
                        shortest_path.append(current)

                #if path to water is not None, add to the path to the start cell
                if shortest_path_to_water:
                    shortest_path +=shortest_path_to_water

                #set a count for fire cell and water cell
                fire_count = 0
                fire_pos =[]
                water_count = 0

                #count the fire cell and water cell in the path
                for ele in shortest_path:
                    element = list(ele)

                    ##count the fire cell
                    if game.grid[element[0]][element[1]].display == 'F':
                        fire_count+=1
                        fire_pos.append((element[0],element[1]))

                    ##count the water cell
                    if game.grid[element[0]][element[1]].display == 'W':
                        water_count+=1

                
                #check if the water count equal fire count
                if fire_count>water_count:
                    check_if_more_fire=True
                    visited = {fire_pos[0]: None}
                    find_water =False
                    path = [fire_pos[0]]
                    continue

                return shortest_path

            #fine the first walk fire cell to the ending cell
            if current == end_pos and game_end == False and check_if_more_fire == True:
                shortest_path_if_more_fire_in = [end_pos]
                new_shortest_path = []
                new_new_shortest_path =[]
                
                 #add to the path list if current in visited is not None
                while current:
                    current = visited[current]

                    if current:
                        shortest_path_if_more_fire_in.append(current)

                i=len(shortest_path_if_more_fire_in)-1
                #adding up all other past paths to the new versio
                while i>=0:
                    new_shortest_path.append(shortest_path_if_more_fire_in[i])
                    i-=1

                a=0

                #adding up all other past paths to the new new versio
                while True:

                    if shortest_path[a] != new_shortest_path[0]:
                        new_new_shortest_path.append(shortest_path[a])

                    else:
                        break
                    a+=1

                new_new_shortest_path+=new_shortest_path
                
                return new_new_shortest_path

            adj_points = []

            '''find adjacent points'''
            current_row, current_col = current

            #check if walk into a fire cell
            if game.grid[current_row][current_col].display == 'F' and check_if_step_fire == False:
                find_water = True
                check_if_step_fire = True
            
            #UP
            if current_row > 0:
                game=Game(filename)
                game.update_player(current,filename)
                game_end = game.end

                if game.game_move('w',filename)[0] != True :

                    if game.grid[game.player.row][game.player.col].display == 'F' \
                        and check_if_more_fire==True:
                        pass

                    else:
                        adj_points.append((game.player.row,game.player.col))
                        game_end = game.end

            #RIGHT
            if current_col < (len(game.grid[0])-1):
                game=Game(filename)
                game.update_player(current,filename)
                game_end = game.end

                if game.game_move('d',filename)[0] != True: 

                    if game.grid[game.player.row][game.player.col].display == 'F' \
                        and check_if_more_fire==True:
                        pass

                    else:
                        adj_points.append((game.player.row,game.player.col))
                        game_end = game.end

            #DOWN
            if current_row < (len(game.grid) - 1):
                game=Game(filename)
                game.update_player(current,filename)
                game_end = game.end

                if game.game_move('s',filename)[0] != True:

                    if game.grid[game.player.row][game.player.col].display == 'F' \
                        and check_if_more_fire==True:
                        pass

                    else:
                        adj_points.append((game.player.row,game.player.col))
                        game_end = game.end

            #LEFT
            if current_col > 0:
                game=Game(filename)
                game.update_player(current,filename)
                game_end = game.end

                if game.game_move('a',filename)[0] != True:

                    if game.grid[game.player.row][game.player.col].display == 'F' \
                        and check_if_more_fire==True:
                        pass

                    else:
                        adj_points.append((game.player.row,game.player.col))
                        game_end = game.end
            
            #wait
            if current_col > 0:
                game=Game(filename)
                game.update_player(current,filename)
                game_end = game.end

                if game.game_move('e',filename)[3] == True:
                    adj_points.append((game.player.row,game.player.col))
                    game_end = game.end
            
            '''loop through adjacent points'''
            for point in adj_points:

                if point not in visited:
                    visited[point] = current
                    path.append(point)
    
     #finding the path if DFS
    elif mode == 'BFS':

        #set search start from the end to the start
        shortest_path_to_water=[]
        check_if_step_fire = False
        visited = {end_pos: None}
        find_water =False
        path = [end_pos]

        #keep lopping if path is not None
        while path:

            #pop the first value in the list and set a new game
            current = path.pop(0)
            game = Game(filename)
            game.update_player(current,filename)

            #find the path to the water cell if need
            if current == water_pos and game_end == False and find_water ==True:
                
                shortest_path_to_water = []
                
                #add to the path list if current in visited is not None
                while current:

                    current = visited[current]

                    if current:
                        shortest_path_to_water.append(current)

                #re set the visited and find the path start from the water position to end
                find_water =False
                visited = {water_pos: None}
                path = [water_pos]
                continue
 
            #find the path to the starting cell
            if current == start_pos and game_end == False and find_water ==False \
                and check_if_more_fire ==False:
                
                #add to the path list if current in visited is not None
                while current:

                    current = visited[current]

                    if current:
                        shortest_path.append(current)

                #if path to water is not None, add to the path to the start cell
                if shortest_path_to_water:
                    shortest_path +=shortest_path_to_water

                #set a count for fire cell and water cell
                fire_count = 0
                fire_pos =[]
                water_count = 0

                #count the fire cell and water cell in the path
                for ele in shortest_path:
                    element = list(ele)

                    ##count the fire cell
                    if game.grid[element[0]][element[1]].display == 'F':
                        fire_count+=1
                        fire_pos.append((element[0],element[1]))

                    ##count the water cell
                    if game.grid[element[0]][element[1]].display == 'W':
                        water_count+=1
                
                #check if the water count equal fire count
                if fire_count>water_count:
                    check_if_more_fire=True
                    visited = {fire_pos[0]: None}
                    find_water =False
                    path = [fire_pos[0]]
                    continue

                return shortest_path

            #fine the first walk fire cell to the ending cell
            if current == end_pos and game_end == False and check_if_more_fire == True:
                shortest_path_if_more_fire_in = [end_pos]
                new_shortest_path = []
                new_new_shortest_path =[]
                
                 #add to the path list if current in visited is not None
                while current:
                    current = visited[current]

                    if current:
                        shortest_path_if_more_fire_in.append(current)

                i=len(shortest_path_if_more_fire_in)-1
                #adding up all other past paths to the new versio
                while i>=0:
                    new_shortest_path.append(shortest_path_if_more_fire_in[i])
                    i-=1

                a=0

                #adding up all other past paths to the new new versio
                while True:

                    if shortest_path[a] != new_shortest_path[0]:
                        new_new_shortest_path.append(shortest_path[a])

                    else:
                        break
                    a+=1

                new_new_shortest_path+=new_shortest_path
                
                return new_new_shortest_path

            adj_points = []

            '''find adjacent points'''
            current_row, current_col = current

            #check if walk into a fire cell
            if game.grid[current_row][current_col].display == 'F' \
                and check_if_step_fire == False:
                find_water = True
                check_if_step_fire = True
            
            #UP
            if current_row > 0:
                game=Game(filename)
                game.update_player(current,filename)
                game_end = game.end

                if game.game_move('w',filename)[0] != True :

                    if game.grid[game.player.row][game.player.col].display == 'F' \
                        and check_if_more_fire==True:
                        pass

                    else:
                        adj_points.append((game.player.row,game.player.col))
                        game_end = game.end

            #RIGHT
            if current_col < (len(game.grid[0])-1):
                game=Game(filename)
                game.update_player(current,filename)
                game_end = game.end

                if game.game_move('d',filename)[0] != True: 

                    if game.grid[game.player.row][game.player.col].display == 'F' \
                        and check_if_more_fire==True:
                        pass

                    else:
                        adj_points.append((game.player.row,game.player.col))
                        game_end = game.end

            #DOWN
            if current_row < (len(game.grid) - 1):
                game=Game(filename)
                game.update_player(current,filename)
                game_end = game.end

                if game.game_move('s',filename)[0] != True:

                    if game.grid[game.player.row][game.player.col].display == 'F' \
                        and check_if_more_fire==True:
                        pass

                    else:
                        adj_points.append((game.player.row,game.player.col))
                        game_end = game.end

            #LEFT
            if current_col > 0:
                game=Game(filename)
                game.update_player(current,filename)
                game_end = game.end

                if game.game_move('a',filename)[0] != True:

                    if game.grid[game.player.row][game.player.col].display == 'F' \
                        and check_if_more_fire==True:
                        pass

                    else:
                        adj_points.append((game.player.row,game.player.col))
                        game_end = game.end
            
            #wait
            if current_col > 0:
                game=Game(filename)
                game.update_player(current,filename)
                game_end = game.end

                if game.game_move('e',filename)[3] == True:
                    adj_points.append((game.player.row,game.player.col))
                    game_end = game.end
            
            '''loop through adjacent points'''
            for point in adj_points:
                
                if point not in visited:
                    visited[point] = current
                    path.append(point)

if __name__ == "__main__":

    # check the arguments is provided
    try:
        filename = sys.argv[1]
        mode = sys.argv[2]
    except IndexError:
        print('python3 solver.py <filename> <mode>')
        sys.exit()

    
    game = Game(filename)
    move_track =solve(mode,filename)

    #check if have a solution or not
    if move_track == None:
        solution_found = False

    else:
        solution_found = True
        
    #if have solution
    if solution_found == True:

        new_move_trace=[move_track[0]]
        teleport_g =[]
        
        check_tele_1=0
        check_tele_2=1

        #cover to new move track if have a teleport
        while check_tele_2<len(move_track):
            check_tele_1_pos=list(move_track[check_tele_1])
            check_tele_1_row=check_tele_1_pos[0]
            check_tele_1_col=check_tele_1_pos[1]
            check_tele_2_pos=list(move_track[check_tele_2])
            check_tele_2_row=check_tele_2_pos[0]
            check_tele_2_col=check_tele_2_pos[1]


            if isinstance(game.grid[check_tele_1_row][check_tele_1_col],Teleport):

                count_row = 0
                count_cel = 0
                teleport = []
                teleport_pos = []
                

                #find the poition of this pair teleport
                for line in game.grid:
                    for element in line:

                        #store all teleports
                        if game.grid[check_tele_1_row][check_tele_1_col].display == element.display:
                            teleport_pos.append(count_row)
                            teleport_pos.append(count_cel)
                            teleport.append(teleport_pos)
                            teleport_pos = []

                        count_cel += 1
                    count_cel = 0
                    count_row += 1
                
                teleport_g=teleport
                #teleport to the other position
                for tele in teleport:
                    if tele[0] != check_tele_1_row or tele[1] != check_tele_1_col:
                        if check_tele_2_row != tele[0] or check_tele_2_col != tele[1]:
                            new_move_trace.append((tele[0],tele[1]))
            new_move_trace.append(move_track[check_tele_2])
            check_tele_1+=1
            check_tele_2+=1

        move_track = new_move_trace

        
        fire_count=0
        water_count=0

        #count the fire cell and water cell in the new move track
        for ele in move_track:
            element = list(ele)

            if game.grid[element[0]][element[1]].display == 'F':
                fire_count+=1
     
            if game.grid[element[0]][element[1]].display == 'W':
                water_count+=1
        
        if fire_count>water_count:
            print('There is no possible path.')
            sys.exit()

        """change the point to the command"""
        i=0 
        next_i =1
        move_command=[]

        while next_i<len(move_track):
            check_1=False
            check_2=False
            check_3=False

            if int(list(move_track[next_i])[0])-int(list(move_track[i])[0])==1:
                move_command.append('s')

            elif int(list(move_track[next_i])[0])-int(list(move_track[i])[0])== -1:
                move_command.append('w')

            if int(list(move_track[next_i])[1])-int(list(move_track[i])[1])==1:
                move_command.append('d')

            elif int(list(move_track[next_i])[1])-int(list(move_track[i])[1])==-1:
                move_command.append('a')

            #check if is teleport cell
            for point in teleport_g:
                if list(move_track[i]) == point:
                    check_1=True
            for point in teleport_g:
                if list(move_track[next_i]) == point:
                    check_2=True
            if next_i+1<len(move_track):
                for point in teleport_g:
                    if list(move_track[next_i+1]) == point:
                        check_3=True

            if check_1 and check_2 and check_3:
                move_command.append('e')

            i+=1
            next_i+=1

        """print the path and number of moves"""
        print('Path has {} moves.'.format(len(move_command)))

        ##set move string
        move_string=''
        i = 0

        while i < len(move_command)-1:
            move_string += move_command[i]
            move_string += ', '
            i += 1
        move_string += move_command[len(move_command)-1]
        print('Path: {}'.format(move_string))

    elif solution_found == False:
        print("There is no possible path.")
