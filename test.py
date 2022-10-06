import unittest
from lib import strangeAlg

a = [[15, 1, 2, 25], [25, 7], [89, 1, 12], [2, 15], [1, 12]]
expectedRes = 5

class TestStringMethods(unittest.TestCase):

  def test_alg(self):
      self.assertEqual(strangeAlg(a), expectedRes)