# src/sub_main.py

import sys,os,json
sys.path.append("..")

from utils.class_utils import *

class Config(object):
    def __init__(self, config_file=""):
        self.data = {}
        if config_file == "":
            config_file = os.path.dirname(os.path.realpath(__file__)) + '\\configs\\' + 'config.json'            
        self.data['config_file'] = config_file
        
    def add(self, key, value):
        self.data[key] = value
        
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

conf = Config()
conf.add("newkey",'ok')
conf.save()
f = conf.load()
print(f.keys())
print(f.values())


