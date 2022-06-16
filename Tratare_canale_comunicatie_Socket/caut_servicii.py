import socket
def caut_servicii(nume_protocol,port_list):
    for port in port_list:
        try:
            s = socket.getservbyport(port,nume_protocol)
            print("Pe portul : {} am serviciul {} care utilizeaza protocolul {}.".format(port,s,nume_protocol))
        except: continue

if __name__ == "__main__":
    port_list = [1,80,8080]
    nume_protocol = 'udp'
    caut_servicii(nume_protocol,port_list)
    nume_protocol = "tcp"
    caut_servicii(nume_protocol,port_list)