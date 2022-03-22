#SOCKET
import socket
import base64
client=socket.socket()
client.connect(('IP',8080))   
##### 
#####
Y=client.recv(1024).decode()
#####
file = open(f'{Y}image.png', "wb")
image_chunk = client.recv(819200)
file.write(image_chunk)
file.close()
	#######