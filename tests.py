import unittest

class tests(unittest.TestCase):

    def test_pass(self):
        self.assertEqual(1, 1)

    def test_pass2(self):
        self.assertEqual(1, 1)

    def test_pass3(self):
        self.assertEqual(1, 1)

    def test_fail(self):
        self.assertEqual(1, 1)

    def test_lowercase(self):
        self.assertTrue('asasha'.islower())
		
		self.assertGreater(2, 1)
		
		self.assertGreater(1, 1)
