import unittest
from unittest import result
from bin.controller import *

class TestEntropy(unittest.TestCase):
    def test_copy(self):
        result = files.copy_image('COVID','D:/test.png')
        self.assertIn('COVID',result)
        
    def test_update(self):
        result = files.update('Normal','D:/test2.png')
        self.assertIn('Normal',result)
        
        
suite = unittest.TestLoader().loadTestsFromTestCase(TestEntropy)
_=unittest.TextTestRunner().run(suite)
        