# base classes

#######################################################
#       Config class
#######################################################
import json, os
class Config(object):
    def __init__(self, config_file="default"):
        self.data = {}
        self.name = config_file
        if config_file != "":
            self.config_file = os.path.dirname(os.path.realpath(__file__)) + '\\..\\configs\\' + self.name + '.json'            
        else:
            return
                
    def add(self, key, value):
        self.data[key] = value
    
    def get(self, key):
        r = self.data.get(key)
        if r == None:
            r = ''
        return r
        
    def save(self, config_file=""):
        if config_file == "":   
            config_file = self.config_file
        
        try:
            with open(config_file, 'w') as fout:
                json.dump(self.data, fout)                   
        except Exception as e:
            print("{} in Config.save.".format(e))        
        return
    
    def load(self, config_file=""):
        if config_file == "":   
            config_file = self.config_file      
        
        try:
            with open(config_file, 'r') as fin:
                self.data = json.load(fin)
        except Exception as e:
            print("{} in Config.load.".format(e))
        return self.data
    
    def dump(self):
        for k,v in self.data.items():
            print("{} = {}".format(k,v))
    


import logging
class WinLogger(logging.Handler):
    def __init__(self, text_window):
        super().__init__()
        self.widget = text_window
        self.widget.setReadOnly(True)
          
    def register_logger(self):
        self.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
        logging.getLogger().addHandler(self)
        # You can control the logging level
        logging.getLogger().setLevel(logging.DEBUG)  
        
    def emit(self, record):
        msg = self.format(record)
        self.widget.appendPlainText(msg)
    
    def disable_console(self):
        logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(name)s - %(levelname)s - %(message)s')
    