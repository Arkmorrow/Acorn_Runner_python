from game import Game
import os
import sys

def game_finish(msg_end_1,msg_end_2):
    """print end massage"""
    print(msg_end_1)
    print()

    ##set move string
    move_string=''
    i = 0

    while i < len(move_track)-1:
        move_string += move_track[i]
        move_string += ', '
        i += 1
    move_string += move_track[len(move_track)-1]

    ##check if only has one or more moves
    if len(msg_end_2) == 8:

        if len(move_track) == 1:
            print('You made {} move.'.format(len(move_track)))
            print('Your move: {}'.format(move_string))
            print()
            print('=====================\n====== {} =====\n====================='.format(msg_end_2))

        else:
            print('You made {} moves.'.format(len(move_track)))
            print('Your moves: {}'.format(move_string))
            print()
            print('=====================\n====== {} =====\n====================='.format(msg_end_2))

    else:

        if len(move_track) == 1:
            print('You made {} move.'.format(len(move_track)))
            print('Your move: {}'.format(move_string))
            print()
            print('=====================\n===== {} =====\n====================='.format(msg_end_2))
            
        else:
            print('You made {} moves.'.format(len(move_track)))
            print('Your moves: {}'.format(move_string))
            print()
            print('=====================\n===== {} =====\n====================='.format(msg_end_2))
    
    return


# check the arguments is provided
try:
    filename=sys.argv[1]
except IndexError:
    print(' Usage: python3 run.py <filename> [play]')
    sys.exit()

#new game object
game=Game(filename)

##move track
move_track=[]

#start output
print(game.string)

#main game
while True:

    ##check if game is finished and win
    if game.check_win() == True:

        #print end msg
        print()
        print()
        msg_end_1='You conquer the treacherous maze set up by the Fire Nation' \
        ' and reclaim the Honourable Furious Forest Throne, restoring' \
        ' your hometown back to its former glory of rainbow and sunshine!' \
        ' Peace reigns over the lands.'

        msg_end_2='YOU WIN!'

        game_finish(msg_end_1,msg_end_2)
        break

    #check if is end game
    elif game.end == True:

        #print end msg
        print()
        print()
        print('You step into the fires and watch your dreams disappear :(.')
        print()
        msg_end_1='The Fire Nation triumphs! The Honourable Furious Forest' \
        ' is reduced to a pile of ash and is scattered to the winds by the' \
        ' next storm... You have been roasted.'

        msg_end_2='GAME OVER'

        game_finish(msg_end_1,msg_end_2)
        break

    ##if win is False
    elif game.check_win() == False:

        ##input the command
        print()
        input_command = input('Input a move: ')
        
        ##chang to low case if caps
        command = input_command.lower()
        move_command =command == 'w' or command == 'a' \
                       or command == 's' or command == 'd'\
                       or command == 'e'
        
        ##check the command if is move_command
        if move_command == True:

            # make a movement and check check_list
            #0:check wall,1:check water,2:check fire,3:check teleport
            check_list = game.game_move(command,filename)

            #check the wall cell
            if check_list[0] == True:
                print(game.string)
                print()
                print('You walked into a wall. Oof!')
            
            #check the water cell
            elif check_list[1] == True:
                print(game.string)
                move_track.append(command)
                print()
                print("Thank the Honourable Furious Forest, you've found a bucket of water!")

            #check the fire cell
            elif check_list[2] == True and game.end == False:
                print(game.string)
                move_track.append(command)
                print()
                print("With your strong acorn arms, you throw a water bucket at the fire. "\
                    "You acorn roll your way through the extinguished flames!")

            #check the teleport cell
            elif check_list[3] == True:
                print(game.string)
                move_track.append(command)
                print()
                print("Whoosh! The magical gates break Physics as we know it and opens "\
                    "a wormhole through space and time.")

            else:
                move_track.append(command)
                print(game.string)

        ##check the command if is quite command
        elif command == 'q':
            print()
            print('Bye!')
            sys.exit()

        ##if none of the above command is meet, print out a msg
        else:
            print(game.string)
            print()
            print('Please enter a valid move (w, a, s, d, e, q).')
