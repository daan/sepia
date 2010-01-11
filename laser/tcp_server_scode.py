import os
import sys

from socket import *
import struct

from lib_scode import *

host = "localhost"
port = 1616
buffer_size = 1028

#
#	setup socket
#

address = (host,port)
tcp_socket = socket(AF_INET,SOCK_STREAM)
tcp_socket.bind(address)
tcp_socket.listen(1)
	
def parse_data(data) :
	scode_print_package(data)

#
# 	main
#

while(1) :
	conn,addr = tcp_socket.accept()

	while(1) :
		data = conn.recv(buffer_size)
		if data:
			parse_data(data)
			conn.send("ack");
		else :
			break
	

# Close socket
tcp_socket.close()



