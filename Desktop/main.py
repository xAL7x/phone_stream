import socket,subprocess
from webbrowser import open
server=socket.socket()
host="IP";port=8080
server.bind((host,port));server.listen()
client,addr=server.accept()
while True:
    msg=client.recv(1024).decode()
    if msg=='1':
        #Y1 URL OR APP
        pass
    elif msg=='2':
        #Y2 URL OR APP
        pass
    elif msg=='3':
        #Y3 URL OR APP
        pass
    elif msg=='4':
        #Y4 URL OR APP
        pass
    elif msg=="5":
        #Y5 URL OR APP
        pass
    elif msg=="6":
        #Y6 URL OR APP
        pass
    elif msg=="7":
        #Y7 URL OR APP
        pass
    elif msg=="8":
        #Y7 URL OR APP
        pass
    elif msg=="9":
        #Y7 URL OR APP
        pass
    elif msg=="10":
        #Y7 URL OR APP
        pass
    elif msg=="11":
        #Y7 URL OR APP
        pass
    elif msg=="12":
        #Y7 URL OR APP
        pass
