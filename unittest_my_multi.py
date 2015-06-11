from my_multi import multi
from my_multi import intet
import unittest

class TestMyMulti(unittest.TestCase):
	def test_my_multi(self):
		self.assertEqual(multi(3), 30)
		self.assertTrue(type(multi(0)) == int)
		
	def test_my_intet(self):
		self.assertTrue(type(intet("h")) == int)

if __name__ == "__main__":
	unittest.main()