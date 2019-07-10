# -*- coding: utf-8 -*-
#######################################################
# main controller classes
#  - from app.controller import *
#  - use two libs to control extruder and robot
#     - UR robot controller:  Controller.robot   
#     - Marlin extruder controller:  Controller.extruder
#######################################################
from ui.ui_mainwindow import *
from ui.dlg_plane_registration import *
from utils.data_base import *
from utils.suDevice import *
from utils.suCommon import *
from utils.suCAMData import *

class Controller(object):
    def __init__(self, main_window):
        self.setting_robot = Config('robot_setting')
        self.setting_extruder = Config('extruder_setting')
        self.main_window = main_window    
        self.robot = DeviceRobot()
        self.extruder = DeviceExtruder()
        self.gcode = GCode()       
        
        
        #self.load_setting()
        
    def load_setting(self):
        self.main_window.comboBox_device.clear()
        self.setting_robot.load()
        self.main_window.tableWidget_robot_info.bind_data(self.setting_robot.data)
        self.main_window.comboBox_device.add_address(self.setting_robot.data)
        
        self.setting_extruder.load()
        self.main_window.tableWidget_extruder_info.bind_data(self.setting_extruder.data)        
        self.main_window.comboBox_device.add_address(self.setting_extruder.data)
        
        self.main_window.refresh()
        
        return
       
    def message(self, msg=""):
        self.main_window.appendPlainText(msg)
        pass
    
    @unimplemented
    def load_gcode(self, filename):
        pass
    @unimplemented    
    def load_path(self, filename):
        pass
    @unimplemented
    def load_gcode(self):
        pass
    @unimplemented        
    def load_model(self):
        pass
    @unimplemented
    def load_path(self):
        pass
    @unimplemented
    def print_plane_registration(self):
        dlg = DlgPlaneRegistration()
        dlg.set_controller(self)
        dlg.show()
        self.main_window.tableWidget_robot_info.bind_data()
        self.main_window.refresh()
        
    @unimplemented
    def save_config(self):
        
        pass
    @unimplemented
    def extruder_init(self):
        pass
    @unimplemented
    def print(self):
        pass
    
    #@unimplemented
    def robot_connect(self):
        ip = self.setting_robot.get('地址')
        tcp_coord = []
        try:
            tcp_coord = self.robot.connect(ip)
        except Exception as e:
            logging.exception(str(e))
        self.main_window.tableWidget_robot_info.data['工具坐标'] = tcp_coord
        self.main_window.tableWidget_robot_info.bind_data()
        self.main_window.refresh()
        
    @unimplemented
    def robot_disconnect(self):
        pass
    
    def extruder_connect(self):
        port = self.setting_extruder.get('地址')
        band_rate = self.setting_extruder.get('波特率')
        if not self.extruder.is_connected():
            self.extruder.connect(port, band_rate)
        
    @unimplemented
    def extruder_disconnect(self):
        pass    
    @unimplemented
    def print_stop(self):
        pass
    
    def send_command(self):
        cmd_text = self.main_window.text_send.text()
        addr = self.main_window.comboBox_device.get_curent_select()
        if 'COM' in addr:
            self.extruder.send_cmd(cmd_text)
        else:
            self.robot.send_cmd(cmd_text)
        #logging.debug('damn, a bug')
        #logging.info('something to remember')
        #logging.warning('that\'s not right')
        #logging.error('foobar')     
        
        
    
    