from socket import *
import sys

from lib_scode import *

#
#	
#

def grid() :
    # make a package
	size = 50
	data = scode_header()
	data += sepia_set_delay_multiplier(3000) 
	data += scode_move_to(0)
	#data += sepia_set_delay_multiplier(60000) 
	data += scode_move_to(0)
	
	for x in range(10) :
		data += scode_set_x(1024 + x * 2 * size)
		data += scode_set_y(1024)
		data += scode_move_to(0)
		data += scode_set_y(1024+ 10 * 2 * size)
		data += scode_move_to(4)
	for y in range(10) :
		data += scode_set_y(1024 + y * 2 * size)
		data += scode_set_x(1024)
		data += scode_move_to(0)
		data += scode_set_x(1024+ 10 * 2 * size)
		data += scode_move_to(4)

	return data
			


def square() :
    # make a package
	data = scode_header()
	data += sepia_set_delay_multiplier(10) 
	data += scode_set_x(1024)
	data += scode_set_y(1024)
	data += scode_move_to(1)
	data += scode_set_x(1024+2048)
	data += scode_move_to(1)
	data += scode_set_y(1024+2048)
	data += scode_move_to(1)
	data += scode_set_x(1024)
	data += scode_move_to(1)
	data += scode_delay(100)
	data += scode_nop()
	return data

if __name__ == "__main__" :
	#
	#	parse commandline
	#
	host = "localhost"
	# host = "192.168.0.120"
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
		i += 1 
	

	#while (1) :
	#	tcp_socket.send( grid() )
	#	recv = tcp_socket.recv(1024);
	#	#tcp_socket.send( grid() )
	#	# Close socket
	#	print "x"
	tcp_socket.close()

