#include "Servo.h"
#include "SoftwareSerial.h"

//Define the pins used for receiving and transmitting information via Bluetooth
#define rxpin 2
#define txpin 3

//Connect the Bluetooth module
SoftwareSerial bluetooth(rxpin, txpin);

Servo l, r;

int speedL, speedR;
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
  
}
 
void loop()
{
  while(bluetooth.available())//input is "<int> <int>"
  {
    int i;
    speedL = 0;
    for(i = 0; i < 3; i++)//ascii value for a space
    {
      k = bluetooth.read();//numbers are 48 above what they truly are
      speedL = (speedL*10) + (k.toInt() - 48);
    }
    if(speedL > 180 || speedL < 0)//speedL is out of bounds
    {
      Serial.println("Left");
      break;
    }
//    Serial.println("k: " + k + " speedL: " + speedL);
    k = bluetooth.read();//reads the space
    
    speedR = 0;
    for(i = 0; i < 3; i++)
    {
      k = bluetooth.read();
      speedR = (speedR*10) + (k.toInt() - 48);
    }
//    Serial.println("k: " + k + " speedR: " + speedR);
//    Serial.println("\n\n");
    if(speedR > 180 || speedR < 0)
    {
      Serial.println("Right");
      break;
    }
    bluetooth.flush();
    l.write(speedL);
    r.write(speedR);
     
    //Wait ten milliseconds to decrease unnecessary hardware strain
    delay(100);
   }
}
