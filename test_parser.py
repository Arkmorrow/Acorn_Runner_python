from game_parser import parse


def test_parse():

    '''test if raise error correctly'''
    try:
        parse([''])

    except ValueError as e:
        assert type(e) == ValueError,'Test ValueError failed'
        assert str(e) == 'Expected 1 starting position, got 0.','Test ValueError msg failed'

    try:
        parse(['Z'])

    except ValueError as e:
        assert type(e) == ValueError,'Test ValueError failed'
        assert str(e) == 'Bad letter in configuration file: Z.','Test ValueError msg failed'

    try:
        parse(['X','1'])

    except ValueError as e:
        assert type(e) == ValueError,'Test ValueError failed'
        assert str(e) == 'Expected 1 ending position, got 0.','Test ValueError msg failed'

    try:
        parse(['X','Y','1'])

    except ValueError as e:
        assert type(e) == ValueError,'Test ValueError failed'
        assert str(e) == 'Teleport pad 1 does not have an exclusively matching pad.','Test ValueError msg failed'

    try:
        parse(['X','Y','0'])

    except ValueError as e:
        assert type(e) == ValueError,'Test ValueError failed'
        assert str(e) == 'Bad letter in configuration file: 0.','Test ValueError msg failed'

    # edge cases
    try:
        parse(['X','Y','-1'])

    except ValueError as e:
        assert type(e) == ValueError,'Test ValueError failed'
        assert str(e) == 'Bad letter in configuration file: -.','Test ValueError msg failed'
        
    #print('Test ValueError passed')


    ''' test if return right class'''
    assert parse(['X','Y'])[0][0].display == 'X','Test start class failed'
    print('Test start class passed')

    assert parse(['X','Y'])[1][0].display == 'Y','Test end class failed'
    print('Test end class passed')
    
    assert parse(['X','*','Y'])[1][0].display == '*','Test wall class failed'
    print('Test wall class passed')

    assert parse(['X',' ','Y'])[1][0].display == ' ','Test air class failed'
    print('Test air class passed')

    assert parse(['X','W','Y'])[1][0].display == 'W','Test water class failed'
    print('Test water class passed')

    assert parse(['X','F','Y'])[1][0].display == 'F','Test fire class failed'
    print('Test fire class passed')


    ''' test if can deal \n'''
    assert parse(['X\n','Y'])[0][0].display == 'X','Test deal failed'
    print('Test deal passed')


def run_tests():
    test_parse()


