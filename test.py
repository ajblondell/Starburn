from src.server import Server
import src.network as net 

if __name__ == '__main__':
    r1 = net.Router()
    print(r1.reserved_ip_file)

    s1 = Server('Server 1', router=r1)
    s2 = Server('Server 2', router=r1)

    net.Connection.link_servers.from_to(s1,s2)


    print(s1.get_info())
    print(s2.get_info())