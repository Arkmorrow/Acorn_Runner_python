from game_parser import read_lines,get_position
from grid import grid_to_string
from player import Player
from cells import (
    Start,
    End,
    Air,
    Wall,
    Fire,
    Water,
    Teleport
)


class Game:
    def __init__(self, filename):
        self.start_pos = get_position(filename,'X')
        self.end_pos = get_position(filename,'Y')
        self.player = Player(self.start_pos[0],self.start_pos[1],0)
        self.grid = read_lines(filename)
        self.string = grid_to_string(read_lines(filename),self.player)
        self.water_reach = []
        self.fire_reach = []
        self.end = False

    def game_move(self, move,filename):
        """make a movement"""

        if move != 'e':
            self.player.move(move)

        #store the list of check result output
        #0:check wall,1:check water,2:check fire,3:check teleport
        check_list=[]

        #set checks to False first
        wall_check = False
        water_check = False
        fire_check = False
        teleport_check = False
        
        #check if walk out of bounds
        if int(self.player.row) < 0:
            self.player.row += 1
            wall_check = True
        elif int(self.player.col) < 0:
            self.player.col += 1
            wall_check = True

        #set new grid
        grid=read_lines(filename)

        #change the water cell and fire cell to air if reached
        if len(self.water_reach) != 0:
            
            cells=Air()

            #change water cell
            for pos in self.water_reach:
                grid[pos[0]][pos[1]] = cells

            #change fire cell
            for pos in self.fire_reach:
                grid[pos[0]][pos[1]] = cells


        #check if walk into a wall cell
        if grid[self.player.row][self.player.col].display == '*':
            self.player.move_back(move)
            wall_check = True
        
        #set a empty position for water, fire and teleport
        water_pos = []
        fire_pos = []
        teleport = []

        #check if walk into a water cell and store into the water reached list
        if grid[self.player.row][self.player.col].display == 'W':
            self.player.add_water_buckets()

            #set a water position that is reached
            water_pos.append(self.player.row)
            water_pos.append(self.player.col)
            self.water_reach.append(water_pos)
            water_check = True

        #check if walk into a fire
        if grid[self.player.row][self.player.col].display == 'F':
            self.player.reach_fire()

            #check if is the end game or not
            if int(self.player.num_water_buckets) < 0:
                self.player.num_water_buckets = 0
                self.end = True

            #set a fire position that is reached
            fire_pos.append(self.player.row)
            fire_pos.append(self.player.col)
            self.fire_reach.append(fire_pos)
            fire_check = True

        #check if walk into a teleport
        cells = Teleport('num')
        if type(grid[self.player.row][self.player.col]) == type(cells) and wall_check == False:
            teleport_check = True
        
            count_row = 0
            count_cel = 0
            teleport_pos = []

            #find the poition of this pair teleport
            for line in grid:

                for element in line:

                    #store all teleports
                    if grid[self.player.row][self.player.col].display == element.display:
                        teleport_pos.append(count_row)
                        teleport_pos.append(count_cel)
                        teleport.append(teleport_pos)
                        teleport_pos = []

                    count_cel += 1
                    
                count_cel = 0
                count_row += 1
            
            #teleport to the other position
            for tele in teleport:

                if tele[0] != self.player.row or tele[1] != self.player.col:
                    new_player_row = tele[0]
                    new_player_col = tele[1]

            self.player.row = new_player_row
            self.player.col = new_player_col
            
        #set new string
        self.string = grid_to_string(grid,self.player)

        #add result to the check_list
        check_list.append(wall_check)
        check_list.append(water_check)
        check_list.append(fire_check)
        check_list.append(teleport_check)

        return check_list

    def check_win(self):
        """check if the game is finish or not"""

        if self.player.row == int(self.end_pos[0]) and self.player.col == int(self.end_pos[1]):
            return True
        else:
            return False


    def update_player(self,pos,filename):
        """for solver to update new player position"""

        self.player.row = pos[0]
        self.player.col = pos[1]
        self.string = grid_to_string(read_lines(filename),self.player)







    

        


