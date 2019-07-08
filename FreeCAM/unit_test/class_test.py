# coding=gbk
"""
"""
import unittest
import sys
import inspect
sys.path.append("..")

from utils.data_base import *

class A(object):
    def __init__(self):
        print("A")

def print_name(func):
    def wrap_func(*args, **kwargs):
        print('{} is not implemented.'.format(func.__name__))
        func(*args, **kwargs)
    return wrap_func

class TestClass(unittest.TestCase):
    
    def print_name(func):
        def wrap_func(*args, **kwargs):
            print('{} is not implemented.'.format(func.__name__))
            func(*args, **kwargs)
        return wrap_func
    
    @print_name
    def test1(self):
        config = Config("test1")
        config.load("../configs/robot_setting.json")
        config.dump()
        config.data['TCP'] = {'x':1,'y':2,'z':0.1}
        config.save("z:/test.json")
        
    @print_name
    def test3(self):
        print('---')
        
    @print_name    
    def test2(self):
        config = Config("test2")
        config.load("z:/test.json")
        config.dump()
        print('test2')
        
    
    

if __name__ == '__main__':
    unittest.main()
   