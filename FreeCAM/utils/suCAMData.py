from utils.suCommon import *
class CAMData(object):
    def __init__(self):
        self.raw_data = str()
    def load(self, file_name):
        pass
    def gen_extruder_control_sequence(self):
        pass
    def gen_robot_control_sequence(self):
        pass
    
    
class GCode(CAMData):
    def __init__(self):
        super(GCode,self).__init__()
    @unimplemented
    def load(self, file_name):
        pass
    @unimplemented
    def gen_extruder_control_sequence(self):
        pass
    @unimplemented
    def gen_robot_control_sequence(self):
        pass    