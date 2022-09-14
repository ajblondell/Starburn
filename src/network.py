import random

class Connection:
    def __init__(self):
        pass

    class link_servers:
        def from_to(inputA, inputB):
            try:
                inputA.create_link(inputB)
                inputB.create_link(inputA)
                status = '[Link Servers]: Link {inputA} to {inputB} Successful'
            except:
                status = f'[Link Servers]: Error linking {inputA} to {inputB}'

            return status

class Router:
    # (!)---fix me---(!):
    # has issue where __init__ is called twice
    def __init__(self, reserved_ip_file=None):
        self.id = random.randint(00000,99999)
        if not reserved_ip_file == None:
            self.reserved_ip_file = reserved_ip_file
        else:
            self.reserved_ip_file = self.new_reserved_ip_file()
            
        
    
    def new_reserved_ip_file(self):
        file = f'{self.id}.rtf'
        open(file,'x')

        return file

    def gen_ip(self):
        # generates a random ipv4 address
        ip_arr = []

        for _ in range(4):
            ocet = random.randint(0,255)
            ip_arr.append(ocet)

        ip = '.'.join(map(str,ip_arr))

        return ip
    
    def reserve_ip(self, ip):
        with open(self.reserved_ip_file, 'a') as ripfl:
            ripfl.write(f'{ip}\n')
            ripfl.close()
    
    def is_valid_ip(self, ip):
        with open(self.reserved_ip_file, 'r') as ripfl:
            valid = True
            line = ripfl.readline()
            while line != '':
                line = ripfl.readline()
                if line == ip:
                    valid = False
            ripfl.close()

            return valid