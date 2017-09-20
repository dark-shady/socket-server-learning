import socket   #for sockets
import sys	#for sys.exit
 
try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as msg:
	print ('Failed to creat socket.  Error code:' +str(msg[0]) + ' , Error message : ' + msg[1])
	sys.exit()
	
print ('Socket Created')

host = 'localhost'
port = 8888
s.settimeout(5)
try:
	remote_ip = socket.gethostbyname(host)
except socket.gaierror:
	print ('Hostname could not be resolved')
	sys.exit()

print ('IP address of ' + host + ' is ' + remote_ip)

try: 
	s.connect((remote_ip, port))
	print ('Connected to ' + host + ' on IP ' + remote_ip + ' on port ' + str(port) + '')
except socket.error as msg:
	print ('Failed to connect to ' + host + ' on IP ' + remote_ip + ' on port ' + str(port) + '')
	sys.exit()

reply = s.recv(4096)

print (reply.decode())



while 1:
	try:
		message = input("What would you like to say")
		s.sendall(message.encode())
		print('Message send successful')
		received = s.recv(1024)
		print(received.decode())
	except socket.error:
		print ('Send failed')
		sys.exit()



print (reply)

s.close()
