# coding=gbk
"""
"""
import unittest
import sys
sys.path.append("..")

from utils.data_base import *


class TestClass(unittest.TestCase):
    
    def test1(self):
        config = Config("test1")
        
            
    def test2(self):
        print('test2')

if __name__ == '__main__':
    unittest.main()