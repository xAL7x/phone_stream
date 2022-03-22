####### YY #######
YY={
    '1':'y=0,x=720',
    '2':'y=370,x=720',
    '3':'y=740,x=720',
    '4':'y=1110,x=720',
    '5':'y=1480,x=720',
    '6':'y=1850,x=720',
    #---------------------
    '7':'y=0,x=360',
    '8':'y=370,x=360',
    '9':'y=740,x=360',
    '10':'y=1110,x=360',
    '11':'y=1480,x=360',
    '12':'y=1850,x=360',
}

import socket
server=socket.socket()
host="IP";port=8080
server.bind((host,port));server.listen()
client,addr=server.accept()
#___
### SERVER Files
file='help1.py'
text=open(file,'r');text_read=text.read()
text_write=open(file,'w')
Target_name_file='target.txt'
### ______________________________________________________


while True: 
    ###_______________________________________________________
        Y=input('\n What do you want to add [from 1 to ... (exit)]: ')
        if Y=='exit':
            exit()
        client.send(f'{Y}'.encode())
        image_name=input('Image name: ')
        target=input('Target: ')

        file_read=open(f'{Y}{Target_name_file}','r');file_read=file_read.read()
        ### SERVER
        if 'http' in target:
                textY=text_read.replace(f'{file_read}',f'open("{target}")')
                textY=text_read.replace(f'''#Y{Y} URL OR APP
        pass''',f'open("{target}")')
                text_write.write(f"{textY}");text_write.close()
                #### Make files for editing
                file=open(f'{Y}{Target_name_file}','w');file.write(f'open("{target}")');file.close()
        else:
                textY=text_read.replace(f'''#Y{Y} URL OR APP
        pass''',f'subprocess.call("{target}")')
                textY=text_read.replace(f'{file_read}',f'subprocess.call("{target}")')
                text_write.write(textY);text_write.close()
                #### MAke files for editing
                file=open(f'{Y}{Target_name_file}','w');file.write(f'subprocess.call("{target}")');file.close()
        ### SERVER END ###
            #________________________________________________________________________________________________________
        file = open(f'{image_name}', 'rb')
        image_data = file.read(819200)
        client.send(image_data)
        file.close()