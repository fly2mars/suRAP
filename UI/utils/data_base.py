# base classes

#######################################################
#       Config class
#######################################################
import json
class Config(object):
    def __init__(self, config_file="default"):
        self.data = {}
        self.name = config_file
        if config_file != "":
            config_file = os.path.dirname(os.path.realpath(__file__)) + '\\configs\\' + 'self.name' + '.json'            
        else:
            return
        
        self.data['config_file'] = config_file
        
    def add(self, key, value):
        self.data[key] = value
    
    def get(self, key):
        r = self.data.get(key)
        if r == None:
            r = 0
        return r
        
    def save(self, config_file=""):
        if config_file == "":
            try:
                with open(self.data['config_file'], 'w') as fout:
                    json.dump(self.data, fout)                   
            except Exception as e:
                print("{} in Config.save.")
        return
    
    def load(self, config_file=""):
        if config_file == "":
            try:
                with open(self.data['config_file'], 'r') as fin:
                    self.data = json.load(fin)
            except Exception as e:
                print("{} in Config.save.")
        return self.data
    
#######################################################
#       Widget class
#######################################################    
from PyQt5.QtWidgets import QWidget, QAction, QTableWidget, QTableWidgetItem, QHeaderView
from PyQt5.QtCore import pyqtSlot

class DictView(QTableWidget):
    def __init__(self, parent_widget=None):
        super(DictView, self).__init__(parent_widget)
        
        self.horizontalHeader().hide()
        self.verticalHeader().hide()        
        self.setRowCount(4)
        self.setColumnCount(2)
        self.setColumnWidth(30, 30)        
        
    
    def bind_data(self, dict_data):
        self.setRowCount(len(dict_data))
        i = 0
        for key, value in dict_data.items():
            self.setItem(i, 0, QTableWidgetItem(key))
            self.setItem(i, 1, QTableWidgetItem(str(value)))
            i += 1

        self.move(0 , 0)

