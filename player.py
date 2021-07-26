class Player:
    def __init__(self,row,col,num_water_buckets):
        self.display = 'A'
        self.num_water_buckets = num_water_buckets
        self.row = int(row)
        self.col = int(col)

    def move(self, move):
        #get the move command and move the player
        if move == 'w':
            self.row -= 1

        elif move == 's':
            self.row +=1

        elif move == 'd':
            self.col += 1
            
        elif move == 'a':
            self.col -= 1

    def move_back(self, move):
        """get the move command and move back the 
        player because walk into the wall"""

        if move == 'w':
            self.row += 1

        elif move == 's':
            self.row -=1

        elif move == 'd':
            self.col -= 1

        elif move == 'a':
            self.col += 1

    def add_water_buckets(self):
        self.num_water_buckets += 1

    def reach_fire(self):
        self.num_water_buckets-=1




