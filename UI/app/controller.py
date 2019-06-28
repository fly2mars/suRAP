#######################################################
# main controller classes
#  - from app.controller import *
#######################################################
from ui.mainwindow import *
from utils.data_base import *

class Controller(object):
    def __init__(self, main_window):
        self.setting_robot = Config('robot_setting')
        self.main_window = main_window
        
        self.load_setting()
        
    def load_setting(self):
        pass
    
    def load_gcode(self, filename):
        pass
        
    def load_path(self, filename):
        pass
    
    def message(self, msg=""):
        pass
        
        
        
    
    