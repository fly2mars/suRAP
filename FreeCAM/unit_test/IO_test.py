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
        config.load("../configs/robot_setting.json")
        config.dump()
        config.data['TCP'] = {'x':1,'y':2,'z':0.1}
        config.save("z:/test.json")
        
            
    def test2(self):
        config = Config("test2")
        config.load("z:/test.json")
        config.dump()
        print('test2')
        
    def testFunction(self):
        def f(*args, **kwargs):
            N = len(args)
            params = ''
            for i in range(N-1):
                params += str(args[i])
                params += ', '
            params += str(args[N-1])
            
            N = len(kwargs)
            
            print(params)
        a = ['1','2','3']
        f(3,2,1)
                

if __name__ == '__main__':
    unittest.main()