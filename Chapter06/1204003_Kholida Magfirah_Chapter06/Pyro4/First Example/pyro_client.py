import Pyro4

uri = input("insert the PYRO4 server URI (help : PYRONAME:server) ").strip()
name = input("Nama Kamu Siapa? ").strip()
# use name server object lookup uri shortcut
server = Pyro4.Proxy("PYRONAME:server")    
print(server.welcomeMessage(name))




