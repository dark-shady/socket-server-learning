import socket
import sys

HOST = ''
PORT = 8888

s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
print ('Socket created')

try:
	s.bind((HOST , PORT))
except socket.error as msg:
	print ('Bind failed.  Error code : ' + str(msg[0]) + 'Message ' + msg[1])
	sys.exit()

print ('Socket bind complete')

s.listen(5)
print ('Socket now listening')

while True:
        conn.send("Connected to server")
	#Receiving from client
	data = conn.recv(1024)
	print (data.decode())
	reply = 'OK...' + data.decode()
	if not data:
		print('Break?')
		break
	     
	conn.sendall(reply.encode())
     
#came out of loop
conn.close()
