# -*- coding: utf-8 -*-
# View class for main_window
from ui.ui_mainwindow import *
from app.controller import *
from utils.data_base import *
from ui.suWidgets import *
from ui.ui_about import *
from PyQt5.QtWidgets import QDialog, QFileDialog
from os import path
class Viewer(Ui_MainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.controller = Controller(self)    # 循环引用，注意释放
               
        #self.setupUi(self)
        #self._connect_signals()
    
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        Ui_MainWindow.setupUi(self,MainWindow)                            
        #self.tableWidget_robot_info = DictView(self.groupBox)        
        #self.tableWidget_robot_info.setObjectName("tableWidget_robot_info")
        self.load_config()    
        
        # set logger window
        self.logger = WinLogger(self.text_console)
        self.logger.register_logger()
        
        self._connect_signals(MainWindow)
        
        self.setFixedSize(self.size())
        
    def _connect_signals(self, MainWindow):
        self.action_exit.triggered.connect(self.app_quit)
        self.action_about.triggered.connect(self.about)
        self.action_connection_setting.triggered.connect(self.connection_setting)
        self.action_extruder_setting.triggered.connect(self.extruder_setting)
        self.action_load_config.triggered.connect(self.load_config)
        self.action_load_gcode.triggered.connect(self.load_gcode)
        self.action_load_model.triggered.connect(self.load_model)
        self.action_load_path.triggered.connect(self.load_path)
        self.action_registration.triggered.connect(self.print_plane_registration)
        self.action_save_config.triggered.connect(self.save_config)
        self.cb_extruder_connect.clicked.connect(self.extruder_connect)
        self.cb_extruder_init.clicked.connect(self.extruder_init)
        self.cb_print.clicked.connect(self.print)
        self.cb_robot_connect.clicked.connect(self.robot_connect)
        self.cb_robot_disconnect.clicked.connect(self.robot_disconnect)
        self.cb_stop.clicked.connect(self.print_stop)
        self.cb_send_command.clicked.connect(self.send_command)
        
    def app_quit(self):
        self.MainWindow.close()
    
    def about(self):
        dialog = QDialog()
        dialog.ui = Ui_AboutDialog()
        dialog.ui.setupUi(dialog)
        dialog.setModal(True)
        dialog.show()
        dialog.exec_()
    
    def refresh(self):
        self.tableWidget_robot_info.setGeometry(QtCore.QRect(10, 20, 321, 121))
        self.tableWidget_extruder_info.setGeometry(QtCore.QRect(10, 20, 321, 141))
        self.tableWidget_printer_info.setGeometry(QtCore.QRect(10, 20, 321, 121))             
        self.update()
        
    def connection_setting(self):
        
        pass
     
    def extruder_setting(self):
        self.controller.setting_extruder.load()
        pass
        
    def load_config(self):
        self.controller.load_setting()            
        self.refresh()
    
    def load_gcode(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '', 
                                            "G code (*.gcode);")
        if fname[0]:
            ext_file = path.splitext(fname[0])[1]
            if  ext_file in fname[1]:                
                logging.info("Load " + fname[0])
                self.controller.gcode.load(fname[0])
            else:
                return        
       
        
    
    def load_model(self):
        self.controller.load_model()
    
    def load_path(self):
        self.controller.load_path()
        pass
    
    def print_plane_registration(self):
        self.controller.print_plane_registration()
        pass
    
    def save_config(self):
        self.controller.save_config()
        pass
    
    def extruder_init(self):
        logging.info('todo')
        pass
    
    def robot_connect(self):
        self.controller.robot_connect()
        pass
    
    def robot_disconnect(self):
        self.controller.robot_disconnect()
        pass
    
    def extruder_connect(self):
        self.controller.extruder_connect()
    
    def print(self):
        self.controller.print()
        pass
    
    def print_stop(self):
        self.controller.print_stop()
        pass
    
    def send_command(self):
        self.controller.send_command()
    
    