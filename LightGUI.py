import bluetooth
import serial
import tkinter as tk

#Look for all Bluetooth devices the computer knows about.
print ("Searching for device...")

bd_addr = "00:18:E4:35:59:5F"#nearby_devices[selection]

port = 1

#Create a connection to the socket for Bluetooth communication
sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

def forward():
    send("f")
def back():
    send("b")
def left():
    send("l")
def right():
    send("r")
def stop():
    send("s")

def send(msg):#sends the data to the hc-06 module
    try:
        sock.send(msg.encode())
        msgLabel.config(text=msg)
    except:
        msgLabel.config(text="An error occurred while sending the command.\nPlease resend the command.")          

def onClose():
    sock.close()
    root.destroy()

#makes the GUI
root = tk.Tk()
root.title("RC Controller")
root.protocol("WM_DELETE_WINDOW", onClose)

frame = tk.Frame(root)
frame.pack()

#Declares all elemens of the GUI
buttonWidth = 13
f = tk.Button(frame, text="forward", command=forward, width=buttonWidth)
b = tk.Button(frame, text="back", command=back, width=buttonWidth)
l = tk.Button(frame, text="left", command=left, width=buttonWidth)
r = tk.Button(frame, text="right", command=right, width=buttonWidth)
s = tk.Button(frame, text="stop", command=stop, width=buttonWidth)
msgLabel = tk.Label(frame, text="")

try:
    sock.connect((bd_addr, port))
except:
    msgLabel.config(text="Could not connect to device.")

#Positions all elements of the GUI
f.pack(side=tk.TOP)
msgLabel.pack(side=tk.BOTTOM)
b.pack(side=tk.BOTTOM)
l.pack(side=tk.LEFT)
r.pack(side=tk.RIGHT)
s.pack()

root.mainloop()

#The below code is used to find all nearby bluetooth devices.

#Create an array with all the MAC addresses of the detected devices
#nearby_devices = bluetooth.discover_devices()

#Run through all the devices found and list their name
#num = 0
#selection = -1
#print ("Select your device by entering its coresponding number...")
#for i in nearby_devices:
#    num+=1
#    print (num , ": " , bluetooth.lookup_name(i))
#    if(bluetooth.lookup_name(i) == "HC-06"):
#        selection = num-1
#        break

#Allow the user to select their Arduino bluetooth module. They must have paired it before hand.
#if(selection == -1):
#    selection = int(input("> ")) - 1
#print ("You have selected", bluetooth.lookup_name(nearby_devices[selection]), "With a mac address of", nearby_devices[selection])