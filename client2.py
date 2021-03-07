# TCP Client 2
import socket 

host = socket.gethostname() 
port = 2004
BUFFER_SIZE = 2000 
MESSAGE = raw_input("tcp_client_2: Enter message or exit:")
 
tcp_client_2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
tcp_client_2.connect((host, port))

while MESSAGE != 'exit':
    tcp_client_2.send(MESSAGE)     
    data = tcp_client_2.recv(BUFFER_SIZE)
    print " Client 2 received message:", data
    MESSAGE = raw_input("tcp_client_2: Enter message to continue or exit:")

tcp_client_2.close() 