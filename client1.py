# TCP Client 1
import socket 

host = socket.gethostname() 
port = 2004
BUFFER_SIZE = 2000 
MESSAGE = raw_input("tcp_client_1: Enter message or exit:") 
 
tcp_client_1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
tcp_client_1.connect((host, port))

while MESSAGE != 'exit':
    tcp_client_1.send(MESSAGE)     
    data = tcp_client_1.recv(BUFFER_SIZE)
    print (" Client1 received message: ", data)
    MESSAGE = raw_input("tcp_client_1: Enter message to continue or exit:")

tcp_client_1.close() 