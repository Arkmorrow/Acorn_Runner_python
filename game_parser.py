import sys
from cells import (
    Start,
    End,
    Air,
    Wall,
    Fire,
    Water,
    Teleport
)

def get_position(filename,element):
    """get element position and return the position"""
    #finding the element position
    ls=read_lines(filename)
    position = []
    count_row = 0
    count_cel = 0

    #count the position
    for row in ls:

        for cel in row:

            if cel.display == element:
                position.append(count_row)
                position.append(count_cel)

            count_cel += 1
            
        count_cel = 0
        count_row += 1
    
    return position

def read_lines(filename):
    """Read in a file, process them using parse(),
    and return the contents as a list of list of cells."""

    #catch the error if file not found
    try:
        file = open(filename,'r')
        lines = file.readlines()
        file.close()
        new_lines = parse(lines)

        return new_lines

    except FileNotFoundError:
        print('{} does not exist!'.format(filename))
        sys.exit()



def parse(lines):
    """Transform the input into a grid.

    Arguments:
        lines -- list of strings representing the grid

    Returns:
        list -- contains list of lists of Cells
    """
    #deal with \n characters
    new_line = []

    for line in lines:
        string=''

        for a in line:

            if a != '\n':
                string += a

        new_line.append(string)

    #Transform the input into a grid and check error
    grid = []
    x_count = 0
    y_count = 0
    check_tele = False
    
    #check if the configuration contains an unknown letter and count X and Y
    for line in new_line:
        for element in line:

            #check if is a teleport int
            try:
                tele_num = int(element)

                if tele_num == 0:
                    check_tele = False
                else:
                    check_tele = True

            except ValueError:
                check_tele = False

            #check if contains an unknown letter
            check_result = element != ' ' and element != '*' and element != 'X' and element != 'Y' \
                           and element != 'W' and element != 'F' and check_tele == False

            if check_result == True:
                raise ValueError('Bad letter in configuration file: {}.'.format(element))
            
            #count the X and Y and check if their is more than one
            if element == 'X':
                x_count += 1

            if element == 'Y':
                y_count += 1
    
    #check the configuration file contain exactly one X
    if x_count > 1 or x_count == 0:
        raise ValueError('Expected 1 starting position, got {}.'.format(x_count)) 

    #check the configuration file contain exactly one Y
    if y_count > 1 or y_count == 0:
        raise ValueError('Expected 1 ending position, got {}.'.format(y_count))

    #Transform the input into a grid
    for line in new_line:
        ls= []
        for element in line:

            #check if is a teleport int
            try:
                tele_num = int(element)
                check_tele = True
            except ValueError:
                check_tele = False

            #check if is a air
            if element == ' ':
                cells = Air()
                ls.append(cells)

            #check if is a X
            elif element == 'X':
                cells = Start()
                ls.append(cells)

            #check if is a Y
            elif element == 'Y':
                cells = End()
                ls.append(cells)

            #check if is a wall
            elif element == '*':
                cells = Wall()
                ls.append(cells)

            #check if is a water
            elif element == 'W':
                cells = Water()
                ls.append(cells)

            #check if is a fire
            elif element == 'F':
                cells = Fire()
                ls.append(cells)

            #store the tele and check if in exact pairs
            elif check_tele == True:
                tele_count = 0

                for line in new_line:

                    for check_element in line:

                        if element == check_element:
                            tele_count += 1

                if tele_count == 2:
                    cells = Teleport(tele_num)
                    ls.append(cells)
                    
                else:
                    msg = 'Teleport pad {} does not have an exclusively matching pad.'.format(element)
                    raise ValueError(msg)  

        grid.append(ls)

    return grid

