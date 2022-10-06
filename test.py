import unittest
from lib import strangeAlg

def test_sum():
    a = [[15 , 1 , 2 , 25] , [25 , 7] , [89 , 1 , 12] , [2 , 15] , [1 , 12]]
    expectedRes = 5
    assert strangeAlg(a) == expectedRes, "Wrong result!"

if __name__ == '__main__':
    test_sum()
