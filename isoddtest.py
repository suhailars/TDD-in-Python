import isodd
import unittest

class TestData(unittest.TestCase):
	TestData=( (0,1),
                   (1,1),
		           (-1,-1),
                   (-2,-1),
                   (8,9),
                   (10,11),
                   (55,55),
                   (100,101) )


	def testIsOddTestData(self):
		"""isOdd give known result with known output"""
		for integer,fn_value in self.TestData:
			result=isodd.isOdd(integer)
			self.assertEqual(fn_value, result)




class IsOddBadInput(unittest.TestCase):

	def testIsOddInput(self):
		"""isOdd fails for bad input"""
		self.assertRaises(isodd.TypeError, isodd.isOdd, 'hello')




if __name__ == "__main__":
	unittest.main()


