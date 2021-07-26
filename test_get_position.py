from game_parser import get_position


def test_get_position():

    '''it will read a file and get a element position'''
    assert get_position('board_simple.txt','X') == [0,2],'Test X pos failed'
    print('Test X pos passed')

    assert get_position('board_simple.txt','Z') == [],'Test none pos failled'
    print('Test none pos passed')




def run_tests():
    test_get_position()

