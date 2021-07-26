from game import Game


def test_game():

    '''Test the player movement'''

    filename='board.txt'
    game=Game(filename)

    #out of bouinds and check move up
    game.game_move('w',filename)
    assert game.player.row == 0,'Test out of bounds fail'
    print('Test out of bounds passed')

    #down
    game.game_move('s',filename)
    assert game.player.row == 1,'Test move down fail'
    print('Test move down passed')
    assert game.player.num_water_buckets == 1,'Test add water failed'
    print('Test add water passed')
    
    #left
    assert game.game_move('a',filename)[2]==True,'Test Fire failed'
    print('Test fire passed')
    assert game.player.num_water_buckets == 0,'Test water minus failed'
    print('Test water minus passed')
    assert game.player.col == 1,'Test move left fail'
    print('Test move left passed')

    #check wall
    assert game.game_move('a',filename)[0] ==True,'Test check wall'
    assert game.player.col == 1,'Test move wall fail'
    print('Test wall passed')

    #right
    game.game_move('d',filename)
    assert game.player.col == 2,'Test move right fail'
    print('Test move right passed')

    #check if water cell disappear
    assert game.player.num_water_buckets == 0,'Test water disappear failed'
    print('Test water disapper passed')

    #Test update player position
    game.update_player([2,2],filename)
    assert [game.player.row,game.player.col] == [2,2],\
        'Test update player position failed'
    print('Test update player position passed')

    #Test check win
    assert game.check_win() == True,'Test check win failed'
    print('Test check win passed')

    filename_2 ='board_test_tele.txt'
    new_game=Game(filename_2)

    #up
    new_game.game_move('w',filename_2)[3] == True,'Test teleport failed'
    print('Tesst teleport passed')

    #check it move to other teleport
    assert [new_game.player.row,new_game.player.col]==[1,2],\
        'Test move teleport failed'
    print('Test teleport move passed')
    


def run_tests():
    test_game()
