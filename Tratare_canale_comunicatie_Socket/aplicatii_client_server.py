from socket import *

serverHost = 0
serverPort = 8888

canal_comunicatie_server = socket(AF_INET,SOCK_STREAM)
canal_comunicatie_server.bind((serverHost,serverPort))
canal_comunicatie_server.listen(3)

while True:
    conexiune,addr = canal_comunicatie_server.accept()
    print("Conexiune cu un client : ",addr)
    while True:
        data = conexiune.recv(1024)
        if not data:
            break
        print("Serverul a primit : ",repr(data))
        conexiune.sendall(data)
    conexiune.close()
