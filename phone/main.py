import socket

from tkinter import * 
from tkinter.ttk import *

client=socket.socket()
client.connect(('IP',8080))    

# creating tkinter window
root = Tk()  
root.configure(bg='#000')

# Creating a photoimage object to use image 
Y1_image = PhotoImage(file="1image.png")        
Y2_image = PhotoImage(file="2image.png")
Y3_image = PhotoImage(file="3image.png")
Y4_image = PhotoImage(file="4image.png")
Y5_image = PhotoImage(file='5image.png')
Y6_image = PhotoImage(file='6image.png')
Y7_image = PhotoImage(file='7image.png')
Y8_image = PhotoImage(file='8image.png')
Y9_image = PhotoImage(file='9image.png')
Y10_image = PhotoImage(file='10image.png')
Y11_image = PhotoImage(file='11image.png')
Y12_image = PhotoImage(file='12image.png')

def Y1_command():
    client.send('1'.encode())
        
def Y2_command():
    client.send('2'.encode())
        
def Y3_command():
    client.send('3'.encode()) 
        
def Y4_command():
    client.send('4'.encode())	
            
def Y5_command():
    client.send('5'.encode())
    
def Y6_command():
    client.send('6'.encode())
        
def Y7_command():
    client.send('7'.encode())
    
def Y8_command():
    client.send('8'.encode())
def Y9_command():
    client.send('9'.encode())
        
def Y10_command():
    client.send('10'.encode())
    
def Y11_command():
    client.send('11'.encode())
def Y12_command():
    client.send('12'.encode())

Y1_Button = Button(root,image=Y1_image,command=Y1_command).place(y=0,x=720)

Y2_Button = Button(root,image = Y2_image,command=Y2_command).place(y=370,x=720)

Y3_Button = Button(root,image = Y3_image,command=Y3_command).place(y=740,x=720)

Y4_Button = Button(root,image = Y4_image,command=Y4_command).place(y=1110,x=720)

Y5_Button = Button(root,image = Y5_image,command=Y5_command).place(y=1480,x=720)

Y6_Button = Button(root,image = Y6_image,command=Y6_command).place(y=1850,x=720)

Y7_Button = Button(root,image = Y7_image,command=Y7_command).place(y=0,x=360)

Y8_Button = Button(root,image = Y8_image,command=Y8_command).place(y=370,x=360)

Y9_Button = Button(root,image = Y9_image,command=Y9_command).place(y=740,x=360)

Y10_Button = Button(root,image = Y10_image,command=Y10_command).place(y=1110,x=360)

Y11_Button = Button(root,image = Y11_image,command=Y11_command).place(y=1480,x=360)

Y12_Button = Button(root,image = Y12_image,command=Y12_command).place(y=1850,x=360)
root.mainloop()