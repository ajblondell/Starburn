import json


class CPU:
    def __init__(self, blank=False, cfg_file=None):
        self.cfg_file = cfg_file
        
        if not blank:
            pass
        else:
            self.cfg_file = './config/CPU/blank.json'
        
        if self.cfg_file == None:
            self.cfg_file = './config/CPU/default.json'

        self.load_cfg()
    
    def load_cfg(self):
        # load json file data 
        with open(self.cfg_file, 'r') as fl:
            data = json.loads(fl.read())
            
            # set values
            self.brand = data['brand']
            self.model = data['model']
            self.arch = data['architecture']
            self.cores = data['cores']
            self.clock = data['clock']
            self.gen = data['generation']


class RAM:
    def __init__(self, cfg_file=None, blank=False):
        self.cfg_file = cfg_file

        if not blank:
            pass
        else:
            self.cfg_file = './config/RAM/blank.json'

        if self.cfg_file == None:
            self.cfg_file = './config/RAM/default.json'

        self.load_cfg()
    
    def load_cfg(self):
        # load json file data
        with open(self.cfg_file, 'r') as fl:
            data = json.loads(fl.read())
            fl.close()

        # set values
        self.brand = data['brand']
        self.model = data['model']
        self.size = data['size']
        self.clock = data['clock']
        self.gen = data['generation']
