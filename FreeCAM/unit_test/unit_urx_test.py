# coding=gbk
"""
"""
import copy
import unittest
import logging
if __name__ == '__main__':
    import sys
    sys.path.append("..")

import urx    
import time
import math

ip = '192.168.56.102'

class TestClass(unittest.TestCase):
    
    def test_connection(self):
        logging.basicConfig(level=logging.INFO)
        r = []
        try:
            robot = urx.Robot("192.168.56.102")
            r = robot
            r.set_tcp((0,0,0,0,0,0))
            r.set_payload(0.5, (0,0,0))
            logging.info("Robot object is available as robot or r")   
            j = r.getj()
            print("Initial joint configuration is ", j) 
            p = r.get_pos()
            print("Initial TCP pos is ", p) 
            p = r.getl()
            print("Initial TCP pose is ", p)       
         
        except Exception as e:
            logging.err(str(e))
        
        finally:            
            r.close()
     
    def test2(self):
        robot = urx.Robot("192.168.56.102")
        robot.set_digital_out(0, 1)
        time.sleep(1)
        robot.set_digital_out(0, 0)    
        robot.set_tcp((0, 0, 0.05, 0, 0, 0)) #ckeck Installation tab
        robot.translate((0, 0, -0.05), acc=0.05, vel=0.05) #acceleration, velocity
        robot.close()
        
    def test_matrix(self):
        global ip
        print(ip)        
        rob = urx.Robot(ip)
        #rob = urx.Robot("localhost")
        rob.set_tcp((0,0,0,0,0,0))
        rob.set_payload(0.5, (0,0,0))
        l = 0.05
        v = 0.05
        a = 0.3
        j = rob.getj()
        print("Initial joint configuration is ", j)
        t = rob.get_pose()
        print("Transformation from base to tcp is: ", t)
        print("Translating in x")
        rob.translate((l, 0, 0), acc=a, vel=v)
        pose = rob.getl()
        print("robot tcp is at: ", pose)
        print("moving in z")
        pose[2] += l
        rob.movel(pose, acc=a, vel=v)


        print("Translate in -x and rotate")
        t.orient.rotate_zb(math.pi/4)
        t.pos[0] -= l
        rob.set_pose(t, vel=v, acc=a)
        print("Sending robot back to original position")
        rob.movej(j, acc=0.8, vel=0.2) 
        
        rob.close()   
        
    def test_simple(self):
        global ip
        print(ip)
        logging.basicConfig(level=logging.WARN)
        
        rob = urx.Robot(ip)
        #rob = urx.Robot("localhost")
        rob.set_tcp((0,0,0,0,0,0))
        rob.set_payload(0.5, (0,0,0))        
        l = 0.05
        v = 0.05
        a = 0.3
        pose = rob.getl()
        print("robot tcp is at: ", pose)
        print("absolute move in base coordinate ")
        pose[2] += l
        rob.movel(pose, acc=a, vel=v)
        print("relative move in base coordinate ")
        rob.translate((0, 0, -l), acc=a, vel=v)
        print("relative move back and forth in tool coordinate")
        rob.translate_tool((0, 0, -l), acc=a, vel=v)
        rob.translate_tool((0, 0, l), acc=a, vel=v)        
        
        rob.close()

    def test_movep(self):
        print(ip)
        rob = urx.Robot(ip)
        try:
            l = 0.1
            v = 0.07
            a = 0.1
            r = 0.05
            pose = rob.getl()
            pose[2] += l
            rob.movep(pose, acc=a, vel=v)
            while True:
                p = rob.getl(wait=True)
                if p[2] > pose[2] - 0.05:
                    break
    
            pose[1] += l 
            rob.movep(pose, acc=a, vel=v)
            while True:
                p = rob.getl(wait=True)
                if p[1] > pose[1] - 0.05:
                    break
    
            pose[2] -= l
            rob.movep(pose, acc=a, vel=v)
            while True:
                p = rob.getl(wait=True)
                if p[2] < pose[2] + 0.05:
                    break
    
            pose[1] -= l
            rob.movep(pose, acc=a, vel=v)
    
        finally:
            rob.close()        
if __name__ == '__main__':
    unittest.main()