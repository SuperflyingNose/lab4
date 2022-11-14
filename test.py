import lib

def test_func_correct ():
    assert lib.func([[1, 2, 3, 4, 5], [1, 2, 3, 5], [1, 2, 4, 5, 6]]) == 3