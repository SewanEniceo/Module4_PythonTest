import unittest

def check(x):

    return x>=100

class TestCheck(unittest.TestCase):

    def test(self):
        self.assertTrue(check(98))

if __name__== '__main__':

    unittest.main()