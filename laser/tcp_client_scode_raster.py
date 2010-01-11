from socket import *
import sys

from lib_scode import *

#
#	
#
if __name__ == "__main__" :
	#
	#	parse commandline
	#
	host = "192.168.0.120"
	host = "localhost"
	port = 1616
	buffer_size = 1028
	address = (host,port)
	#
	#	socket
	#
	print "creating socket (%s,%d)" % (host,port)
	address = (host,port)
	tcp_socket = socket(AF_INET,SOCK_STREAM)
	tcp_socket.connect(address)
	print "sending data to server"

	f = open("result.txt","r")
	i = 0
	for line in f:
		tcp_socket.send(line)
		print("sent line " + str(i))
		scode_print_package(line)	
		i += 1 
		recv = tcp_socket.recv(1024);
	
	tcp_socket.close()

