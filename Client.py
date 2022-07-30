from sys import displayhook
from tkinter import *
from tkinter import messagebox
import socket

def UDP(mem):
    serverAddress = ("192.168.0.132", 50014)
    # create socket
    tempSensorSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #send data
    tempSensorSocket.sendto(mem.encode(), serverAddress)
    #get response
    response = tempSensorSocket.recv(50014)
    #print
    display.set(response)
    

def ButtonCallback():
    text = f"{protocol.get()}{userInput.get()}"
    UDP(text)



def main():
   global userInput
   global protocol
   global display
   top = Tk()
   display = StringVar()

   #protocol selection
   protocol = IntVar()
   Radiobutton1 = Radiobutton(top, text="SPI", variable=protocol, value=1)
   Radiobutton1.pack( side = TOP, anchor = W )

   Radiobutton2 = Radiobutton(top, text="I2C", variable=protocol, value=2)
   Radiobutton2.pack( side = TOP, anchor = W )

   Radiobutton3 = Radiobutton(top, text="UART", variable=protocol, value=3)
   Radiobutton3.pack( side = TOP, anchor = W)

   #user text
   userInput = StringVar()
   Label1 = Label(top, text="Text to Send:")
   Label1.pack(side = TOP)
   Entry1 = Entry(top, width=35, bd = 3, textvariable = userInput)
   Entry1.pack(side = TOP)
   
   #button
   B = Button(top, text = "send", command = ButtonCallback)
   B.pack()
   #output
   output = Label(top, textvariable=display)
   output.pack(side = BOTTOM)

   top.mainloop()

main();