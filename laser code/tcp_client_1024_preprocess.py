from socket import *
import sys
import struct
from PIL import Image
import datetime

from lib_scode import *

ROWS = 1024
PACKET_SIZE = 1024
PACKETS_PER_ROW = 4

#
#	
#

def prepare_image_data(filename) :
	img = Image.open(filename)
	lines = []
	
	for y in range(ROWS) :
		black = 0
		data = ""
		for x in range(PACKET_SIZE) :
			rgba = img.getpixel((x,y))
			pixel = ( rgba[0] + rgba[1] + rgba[2] ) / 3
			if pixel != 0 :
				black=1;
			data += struct.pack("B", pixel)
			# print pixel
		if black == 0 :
			#print "skip", y 
			data = None
		#else :
		#	print "line",y
		lines.append(data)
	return lines

def header(x,y) :
	return struct.pack("b",0) + struct.pack("b",x >> 8) + struct.pack("!H",y)

if __name__ == "__main__" :
	#
	#	parse commandline
	#
	import optparse
	op = optparse.OptionParser("send a large image through UDP to a server")
	op.add_option("-a","--address", dest="host", help="host address. default = 192.168.0.120")
	op.set_defaults(host="192.168.0.120")
	op.add_option("-p","--port", dest="port", help="port. default = 1616")
	op.set_defaults(port=1616)
	op.add_option("-b","--buffer", dest="buffer_size", help="buffer size. default = 1024")
	op.set_defaults(buffer_size=1024)
	(opts, args) = op.parse_args()
	if ( len(args) != 1 ) :
		print "provide one image."
		sys.exit(1)

	host = opts.host
	port = opts.port
	buffer_size = opts.buffer_size
	image_filename = args[0]

	#
	#	prepare image data
	#

	lines =  prepare_image_data(image_filename)

	print "image data prepared"

	#
	#	socket
	#
	print "creating socket (%s,%d)" % (host,port)
	address = (host,port)
	tcp_socket = socket(AF_INET,SOCK_STREAM)
	tcp_socket.connect(address)
	print "sending data to server"

	data = scode_header()
	data += sepia_set_delay_multiplier(10) 
	data += scode_nop()

	tcp_socket.send(data)
	data = tcp_socket.recv(1024)

	pre = datetime.datetime.now()
	while(1) :
		for y in range(ROWS):
			if lines[y] == None :
				pass
				#print "empty line %d" % y
			else :
				data = header(1536,1536+y) + lines[y]
				tcp_socket.send(data)
		
				#print "have send (%d,%d)" % (1,y)
				data = tcp_socket.recv(1024)
				#print "ack"
		post = datetime.datetime.now()
		lapse = post-pre
		print "seconds",lapse.seconds

	# Close socket
	tcp_socket.close()

