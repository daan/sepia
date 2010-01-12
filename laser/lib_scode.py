import struct
import vec2d

SCODE_SET_X=	1 
SCODE_SET_Y=	2
SCODE_SET_ROT=	3
SCODE_SET_SPEED=4
SCODE_MOVE_TO=	5
SCODE_BITMAP=	6
SCODE_DELAY =	7
SCODE_NOP =	8

SEPIA_SETTING_INTENSITY_DELAY_MULTIPLIER=128
SEPIA_SETTING_GALVO_TRAVEL_SPEED=129

galvo_co = [0,0]
next_co  = [0,0]
galvo_speed = 1

def check_value(v) :
	value = int(v)
	if value < 0 : value = 0;
	if value > 4095 : value = 4095
	return value

def sepia_set_delay_multiplier(speed) :
	data = struct.pack("!B",SEPIA_SETTING_INTENSITY_DELAY_MULTIPLIER)
	data += struct.pack("!B",0)
	data += struct.pack("!H",speed)
	return data
def sepia_set_galvo_travel_speed(speed) :
	data = struct.pack("!B",SEPIA_SETTING_GALVO_TRAVEL_SPEED)
	data += struct.pack("!B",0)
	data += struct.pack("!H",speed)
	return data

def scode_image_header(x,y) :
	x = (x >> 4 ) & 0xff
	y = y & 0x0fff
	data = struct.pack("!B",255)
	data += struct.pack("!B",x)
	data += struct.pack("!H",y)
	return data
def scode_header() :
    data = struct.pack("!B",255)
    data += struct.pack("!B",255)
    data += struct.pack("!B",255)
    data += struct.pack("!B",255)
    return data

def scode_set_x(x) :
	x = check_value(x)
	data = struct.pack("!B",SCODE_SET_X)
	data += struct.pack("!B",0)
	data += struct.pack("!H",x)
	return data
	
def scode_set_y(y) :
	y = check_value(y)
	data = struct.pack("!B",SCODE_SET_Y)
	data += struct.pack("!B",0)
	data += struct.pack("!H",y)
	return data

def scode_move_to(steps) :
	data = struct.pack("!B",SCODE_MOVE_TO)
	data += struct.pack("!B",0)
	data += struct.pack("!H",steps)
	return data

def scode_set_speed(speed) :
	data = struct.pack("!B",SCODE_SET_SPEED)
	data += struct.pack("!B",0)
	data += struct.pack("!H",speed)
	return data

def scode_nop() :
	data = struct.pack("!B",SCODE_NOP)
	data += struct.pack("!B",0)
	data += struct.pack("!H",0)
	return data

def scode_delay(delay) :
	data = struct.pack("!B",SCODE_DELAY)
	data += struct.pack("!B",0)
	data += struct.pack("!H",delay)
	return data


def scode_print_package(d) :
	header = struct.unpack("!B",d[0])[0]

	#print struct.unpack("!BBBB",d[0:4])
	
	if int(header) != 255 :
		print "header is not 255 "
		return
	else :
		print "header is ok "

	data = d[4:]
	
	print "package length", len(data)/4

	
	for i in range( len(data)/4 ) :
		#print "cmd"
		#print struct.unpack("!BBBB",d[i*4:i*4+4])
	
		opcode = struct.unpack("!B",data[i*4])[0]
		value = struct.unpack("!H",data[i*4+2:i*4+4])[0]
		if opcode == SCODE_SET_X :
			print "set x to", value
		if opcode == SCODE_SET_Y :
			print "set y to", value
		if opcode == SCODE_MOVE_TO :
			print "move to with steps",value
		if opcode == SCODE_SET_SPEED :
			print "set speed to", value
		if opcode == SCODE_DELAY :
			print "delay", value
		if opcode == SCODE_NOP :
			print "NOP"
			return


if __name__ == "__main__" :

	#
	#	socket
	#
    
    # make a package

	f = open("data.txt", "r")
	#format x y
	
	data = scode_header()
	data += scode_set_speed(1)
	data += scode_nop()
	data += '\n'
	
	for line in f:
		entries = line.split()
		x = entries[0]
		y = entries[1]
		data += scode_header()
		data += scode_set_x(x)
		data += scode_set_y(y)
		data += scode_move_to(0)
		data += scode_delay(100)
		data += scode_nop()
		data += '\n'
    
	# data += scode_set_x(0)
	# data += scode_set_y(0)
	# data += scode_move_to(1)
	# data += scode_delay(100)
	# data += scode_set_x(400)
	# data += scode_set_y(400)
	# data += scode_move_to(1)
	# data += scode_delay(100)

	
    
	output = open("result.txt","w")
	output.write(data);
	#scode_print_package(data)
    
    
    
