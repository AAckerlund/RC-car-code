# code based off this repo: https://github.com/huberf/Computer-to-Arduino-Bluetooth
# This project requires PyBluez
import bluetooth
import serial

#Look for all Bluetooth devices the computer knows about.
print ("Searching for device...")

bd_addr = "00:18:E4:35:59:5F"#nearby_devices[selection]

port = 1

#Create a connection to the socket for Bluetooth communication
sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

def disconnect():
    #Close socket connection to device
    self.sock.close()

def main():
    userInput = ""
    possibleInputs = ['r', 'l', 'f', 'b', 's', 'z']
    while(userInput != "q"):
        userInput = input("give me a new command: ")
        if(userInput in possibleInputs):
            try:
                sock.send(userInput.encode())
                print(userInput)
            except:
                print("An error occurred while sending the command. Please resend the command.")
        elif(userInput == 'q'):
            print("Thanks for using")
        else:
            print("\nvalid inputs are as follows:")
            print("\tr (turn right)\n\tl (turn left)\n\tf (go forward)\n\tb (go backwards)\n\ts (stop)\n\tz (random direction)\n\tq (quit the program).\n")

try:
    sock.connect((bd_addr, port))
    try:
        main()
    except:
        print("A fatal error occurred while getting user input.")
except:
    print("Could not connect to device.")
sock.close()

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