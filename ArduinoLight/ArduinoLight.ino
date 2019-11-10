#include "Servo.h"
#include "SoftwareSerial.h"

//Define the pins used for receiving and transmitting information via Bluetooth
#define rxpin 2
#define txpin 3

//Connect the Bluetooth module
SoftwareSerial bluetooth(rxpin, txpin);

Servo l, r;

int speedL, speedR;
/*
char inData[64];
char inChar = -1;
*/
String k = String("a");
int spaceLoc = 0;

void setup()
{ 
//  Serial.println("I've Started");
  Serial.begin(9600); //initialize serial COM at 9600 baudrate
  
  //Initialize the bluetooth
  bluetooth.begin(9600);

  l.attach(12);
  r.attach(13);
  //speed value are 0-180 with 90 being stopped (in theory)
  speedL = 90;
  speedR = 90;
  //Set the lightbulb pin to put power out
//  Serial.println("Setup Finished");
  
}
 
void loop()
{
  while(bluetooth.available())//input is "<int> <int>"
  {
    k = String(bluetooth.read());//proceeding assuming that the entire string is read at once.
    Serial.println(k);
    for(int i = 0; i<k.length(); i++)
    {
      if(k.charAt(i).equals(" ")
      {
        spaceLoc = i;
        break;
      }
    }
    speedL = k.substring(0,i-1).toInt();
    speedR = k.substring(i+1,k.length()-1).toInt();
    
    l.write(speedL);
    r.write(speedR);
     
    //Wait ten milliseconds to decrease unnecessary hardware strain
    delay(10);
   }
}
