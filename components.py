import random
import json

class Server:
    def __init__(self, name, cpu={'brand':'Elite Compute Devices','model':'ECD3100','cores':'4','clock':'3.9'}, ram={'brand':'Roughair','Model':'Vengance','clock':'3600'}, firewall='MONARCH'):
        self.name = name
        self.cpu = cpu
        self.ram = ram
        self.firewall = firewall
        self.ip = self.genIP()
        self.connections = []
    
    def genIP(self):
        # generates a random ipv4 address
        ip_arr = []

        for _ in range(4):
            ocet = random.randint(0,255)
            ip_arr.append(ocet)

        ip = '.'.join(map(str,ip_arr))

        return ip

    def get_info(self):
        return self.__dict__

    def create_link(self, destination):
        self.connections.append(destination.ip)
        return True


class CPU:
    def __init__(self, blank=False, default=False, brand='None', model='None', architecture='None', clock='None', generation='None', cpu_cfg_file='None'):
        self.brand = brand
        self.model = model
        self.arch = architecture
        self.clock = clock
        self.gen = generation
        self.cpu_cfg_file = cpu_cfg_file
        
        if default:
            self.cpu_cfg_file = './config/cpu_default.json'
            blank = False

        if not blank:
            self.load_cfg()
    
    def load_cfg(self):
        with open(self.cpu_cfg_file, 'r') as fl:
            data = json.loads(fl.read())
            
            self.brand = data['brand']
            self.model = data['model']
            self.arch = data['architecture']
            self.clock = data['clock']
            self.gen = data['generation']

