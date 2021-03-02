import socket
from threading import Thread
from SocketServer import ThreadingMixIn

#TCP Server Socket Thread Pool

class ClientThread(Thread):

    def __init__(self,ip,port):
        Thread.__init__(self)
        self.ip=ip
        self.port=port
        print("New server socket thread started for " + ip +
              " : " + str(port))

    def run(self):
        while True:
            data=conn.recv(2048)
            print("Server received data: ", data)
            MESSAGE=raw_input("Server: Enter Response from Server/Enter exit: ")
            if MESSAGE=='exit':
                break
            conn.send(MESSAGE)  #echo

#TCP Server Socket Program Stub

TCP_IP='0.0.0.0'
TCP_PORT=2004
BUFFER_SIZE=1024

tcpServer=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
tcpServer.bind((TCP_IP, TCPPORT))
threads=[]

while True:
    tcpServer.listen(4)
    print("Waiting for connections from TCP clients")
    (conn, (ip,port))=tcpServer.accept()
    newThread=ClientThread(ip,port)
    newThread.start()
    threads.append(newThread)

for t in threads:
    t.join()
