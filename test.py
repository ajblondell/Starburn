from components import Server, CPU
from network import Connection

s1 = Server('S1', ram={'brand':'Roughair','Model':'Vengance Pro','clock':'3200, 32Gb'})
s2 = Server('S2')

Connection.link_servers.from_to(s1,s2)

#print(s1.__dict__)
#print(s2.__dict__)

c1 = CPU(blank=True)
print(c1.__dict__)
