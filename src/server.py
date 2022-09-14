from .network import Router
from .components import RAM, CPU
class Server:
    def __init__(self, name, cpu=CPU(), ram=RAM(), firewall='MONARCH', router=Router()):
        self.name = name
        self.cpu = cpu
        self.ram = ram
        self.router = router
        self.firewall = firewall
        self.ip = router.gen_ip()
        while not self.router.is_valid_ip(self.ip):
            self.ip = self.router.gen_ip()
        self.router.reserve_ip(self.ip)
        self.connections = []
    
    

    def get_info(self):
        infolist = [
            '-------- Server Info --------\n'
            f'Server : {self.name}\n',
            f'IP : {self.ip}\n',
            '\n',
            f'CPU :\n',
            f'    Brand : {self.cpu.brand}\n',
            f'    Model : {self.cpu.model}\n',
            f'    Architecture : {self.cpu.arch}\n',
            f'    Cores : {self.cpu.cores}\n',
            f'    Clock : {self.cpu.clock}\n',
            f'    Generation : {self.cpu.gen}\n',
            '\n',
            'RAM :\n',
            f'    Brand : {self.ram.brand}\n',
            f'    Model : {self.ram.model}\n',
            f'    Size : {self.ram.size}\n',
            f'    Clock : {self.ram.clock}\n',
            f'    Generation : {self.ram.gen}\n',
            '\n',
            f'Connections : {self.connections}\n'
        ]
        return ''.join(infolist)

    def create_link(self, destination):
        self.connections.append(destination.ip)
        return True