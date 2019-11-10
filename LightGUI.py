import bluetooth
import serial
import pygame

def connectBluetooth():
    #Look for all Bluetooth devices the computer knows about.
    print ("Searching for device...")
    bd_addr = "00:18:E4:35:59:5F"#nearby_devices[selection]
    port = 1
    #Create a connection to the socket for Bluetooth communication
    sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

def connectJoy():
    pygame.init() #initalize pygame
    pygame.joystick.init()# Initialize the joysticks.

def send(msg):#sends the data to the hc-06 module
    try:
        sock.send(msg.encode())
    except:
        print("An error occurred while sending the command.\nPlease resend the command.")          

def normalize(trigger, bumper):#trigger will be -1 to 1, bumper will be 1 or 0
    value = (trigger+1)/2# make trigger a value between 0 and 1
    
    if(bumper == 1):#if bumper is pressed we want to go backwards
        value = -value
    
    value = 90 + 90*value#90 is no motion, if the trigger isn't pulled its value is 0. acceptable values are 0(full reverse) to 180(full forward).
    return int(value)

def Close():
    sock.close()

def getInput():
    # Used to manage how fast the screen updates.
    clock = pygame.time.Clock()

    # Get count of joysticks.
    joystick_count = pygame.joystick.get_count()

    # For each joystick:
    for i in range(joystick_count):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()

    while True:
        #Do no under any surcumstances remove the following loop. The script will stop recieving input if you do.
        for event in pygame.event.get(): # User did something.
            break

        axisL = joystick.get_axis(2)
        buttonL = joystick.get_button(4)
        print("Left Trigger:  " + str(axisL))#left Trigger
        print("Left Bumper:  " + str(buttonL))#left bumper
        leftIn = normalize(axisL, buttonL)

        axisR = joystick.get_axis(5)
        buttonR = joystick.get_button(5)
        print("Right Trigger: " + str(axisR))#right Trigger
        print("Right Bumper: " + str(buttonR))#right bumper
        rightIn = normalize(axisR, buttonR)

        print("\nLeft servo: " + str(leftIn) + "\nright servo: " + str(rightIn))
        send(str(leftIn) + " " + str(rightIn))
        print("")

        #limits the number of loops per seconds
        clock.tick(10)


def main():
    try:
        connectJoy()
    except:
        print("could not find a controller. Please make sure you have one plugged in.")

    try:
        connectBluetooth()
    except:
        print("could not find the device.")

    try:
        sock.connect((bd_addr, port))
    except:
        print("Could not connect to device.")
    
    try:
        getInput()
    except:
        print("An error occured while recieving inputs.")

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
#    if(bluetooth.lookup_name(i) == "HC-06"):
#        selection = num-1
#        break

#Allow the user to select their Arduino bluetooth module. They must have paired it before hand.
#if(selection == -1):
#    selection = int(input("> ")) - 1
#print ("You have selected", bluetooth.lookup_name(nearby_devices[selection]), "With a mac address of", nearby_devices[selection])