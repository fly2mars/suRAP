import logging  
class DeviceBase(object):
    def __init__(self):
        self.params = {}
        self.is_open = False
    
    def is_connected(self):
        return self.is_open
        
    def connect(self, addr):
        pass
    
    def disconnect(self):
        pass
    
    def send_cmd(self, cmd_str):
        logging.debug('send command')
        pass
    
    def get_status(self):
        pass
    
import serial
import time
class DeviceExtruder(DeviceBase):
    def __init__(self):
        super(DeviceExtruder, self).__init__()
    
    def connect(self, port, band_rate=115200):
        try:
            self.params['port'] = port
            self.params['band_rate'] = band_rate
            self.s = serial.Serial(port,band_rate, timeout=0.5) 
            self.is_open = True
            logging.info('{} is openned with {} band'.format(port, band_rate))
            self.s.write(str.encode("\r\n\r\n"))  # Hit enter a few times to wake the marlin board
        except Exception as e:
            logging.error(str(e))
        
    def disconnect(self):
        pass
    
    def send_cmd(self,cmd_str):
        logging.debug('Sending: ' + cmd_str)
        try:
            self.s.write(str.encode(cmd_str + '\n')) # Send g-code block      
            str_out = self.s.readlines()
            logging.info(str_out)            
        except Exception as e:
            logging.exception(str(e))        
        
            # # Wait for response with carriage return        
        pass
    
    def disconnect(self):
        if self.is_connected():
            self.s.close()
            self.is_open = False
        logging.info('Connection with extruder is closed')
    
    def get_status(self):
        pass    
    

import urx
class DeviceRobot(DeviceBase, urx.Robot):
    def __init__(self):
        super(DeviceRobot, self).__init__()
        
    def connect(self, addr):
        p = []
        rob=[]
        try:
            rob = urx.Robot(addr)     
            logging.info(rob)
            self.is_open = True
            logging.info('connect robot')
            p = rob.getl()
            logging.info('TCP = {}'.format(p))            
            rob.close()
            time.sleep(2)
        except rob.secmon._s_secondary.timeout as e:
            logging.exception(str(e))
             
        self.is_open = False
        return p
        
        
    
    def disconnect(self):
        if self.is_connected():
            self.s.close()
            self.is_open = False
            logging.info('Connection with robot is closed')
    
    def send_cmd(self, cmd_str):
        logging.debug('TODO: convert gcode to movej')
        
    
    def get_status(self):
        
        pass    