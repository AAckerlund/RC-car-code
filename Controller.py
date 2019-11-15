import bluetooth
import serial
import pygame

def connectBluetooth():#attempts to create a connection to a bluetooth device

    #Look for all Bluetooth devices the computer knows about.
    bd_addr = "00:18:E4:35:59:5F"#the mac address of the device you wish to connect to (this particular addess is for an hc-06 module)
    port = 1
    
    sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)#Create a connection to the socket for Bluetooth communication

    try:#attemp to connect
        sock.connect((bd_addr, port))
        return sock
    except:
        print("Could not connect to device.")

def connectJoy():#connects to an avaliable controller
    pygame.init() #initalize pygame
    pygame.joystick.init()# Initialize the joysticks.

def send(sock, msg):#sends the data (msg) to the bluetooth module (sock)
    sock.send(msg.encode())

def normalize(trigger, bumper):#uses the data gathered to generate a number between 0 and 180
    #trigger will be -1 to 1, bumper will be 1 or 0
    value = (trigger+1)/2# make trigger a value between 0 and 1
    
    if(bumper == 1):#if bumper is pressed we want to go backwards
        value = -value
    
    value = 90 + 90*value#90 is no motion, if the trigger isn't pulled its value is 0. acceptable values are 0(full reverse) to 180(full forward).
    return int(value)

def Close(sock):#allows us to close the connection to the given (sock) bluetooth device
    sock.close()

def normString(l, r):#ensures that the data sent is going to be consistent in length and format.
    #data will be sent in the form of a string that looks like "xxx xxx" where each x is an integer value
    returnString = ""
    #generate the first 3 digit integer value
    if(l < 100):#there are only 2 digits in the given number so we should add another one to the start (keeps the value the same but adds another digit).
        returnString += "0" + str(l)
        if(l == 0):#if the integer value is 0 then we need to add a second digit.
            returnString += "0"
    else:#if the integer is 100 or greater then we don't need to add anything to it.
        returnString += str(l)

    returnString += " "#add a separator value 

    #generate the second 3 digit integer value. Same logic as above
    if(r < 100):
        returnString += "0" + str(r)
        if(r == 0):
            returnString += "0"
    else:
        returnString += str(r)

    return returnString#return the value we have generated.
    
def getInput(sock):#gets the user input
    # Used to manage how fast the screen updates.
    clock = pygame.time.Clock()

    joystick = pygame.joystick.Joystick(0)
    joystick.init()

    while True:#create an infinite loop continuously detect input
        #Do no under any surcumstances remove the following loop. The script will stop recieving input if you do.
        for event in pygame.event.get(): # User did something.
            break
        
        #data for left side
        #joystick.get_axis(2) gets the value of the left trigger
        #joystick.get_button(4) gets the value of the left bumper

        #data for right side
        #joystick.get_axis(5) gets the data for the right trigger
        #joystick.get_button(5) gets the data for the right bumper

        #print(normString(normalize(joystick.get_axis(2), joystick.get_button(4)), normalize(joystick.get_axis(5), joystick.get_button(5))))
        send(sock, normString(normalize(joystick.get_axis(2), joystick.get_button(4)), normalize(joystick.get_axis(5), -1*(joystick.get_button(5)-1))))

        #limits the number of loops per seconds
        clock.tick(10)

def main():
    try:
        connectJoy()
    except:
        print("could not find a controller. Please make sure you have one plugged in.")
    print("joystick connected")
    try:
        sock = connectBluetooth()
    except:
        print("could not find the device.")
    print("connection connected")
    try:
        getInput(sock)
    except:
        print("An error occured while recieving inputs.")
    Close(sock)

main()

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

#Allow the user to select their  bluetooth module. They must have paired it before hand.
#if(selection == -1):
#    selection = int(input("> ")) - 1
#print ("You have selected", bluetooth.lookup_name(nearby_devices[selection]), "With a mac address of", nearby_devices[selection])