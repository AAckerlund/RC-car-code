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
char k = 'a';

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
  while(bluetooth.available())
  {
    k = bluetooth.read();
    Serial.println(k);

    if(k == 'f')//go forward
    {
      speedL = 110;
      speedR = 70;
    }
    else if(k == 'b')//go backward
    {
      speedL = 70;
      speedR = 110;
    }

    else if(k == 'r')//go right
    {
      speedR = 110;
      speedL = 100;
    }
    else if(k == 'l')//go left
    {
      speedR = 80;
      speedL = 70;
    }
    else if(k == 'z')//do random
    {
      speedL = random(0,180);
      speedR = random(0,180);
    }
    else//stop
    {
      speedL = 90;
      speedR = 90;
    }
     l.write(speedL);
     r.write(speedR);
     
    //Wait ten milliseconds to decrease unnecessary hardware strain
     delay(10);
   }
}
