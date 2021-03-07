import socket 
from threading import Thread 
from SocketServer import ThreadingMixIn 

# Multithreaded Python server 
class ClientThread(Thread): 
 
    def __init__(self,ip,port): 
        Thread.__init__(self) 
        self.ip = ip 
        self.port = port 
        print "New server socket thread started for " + ip + ":" + str(port) 
 
    def run(self): 
        while True : 
            data = conn.recv(2048) 
            print "Server received message:", data
            MESSAGE = raw_input("Enter Response from Server or exit:")
            if MESSAGE == 'exit':
                break
            conn.send(MESSAGE)  # echo 

# TCP Server Socket
TCP_IP = '0.0.0.0' 
TCP_PORT = 2004 
BUFFER_SIZE = 20   

tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
tcpServer.bind((TCP_IP, TCP_PORT)) 
threads = [] 
 
while True: 
    tcpServer.listen(5) 
    print "Waiting for connections from TCP clients..." 
    (conn, (ip,port)) = tcpServer.accept() 
    newthread = ClientThread(ip,port) 
    newthread.start() 
    threads.append(newthread) 
 
for t in threads: 
    t.join() 