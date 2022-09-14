from components import Server

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


