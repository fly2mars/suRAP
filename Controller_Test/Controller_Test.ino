#include <HerkuleX.h>
#include <Arduino.h>
#include "Config.h"
#include <i2c_t3.h>
//#include "Libraries/HerkuleX/HerkuleX.h"

// global variables declared in pins.h
HardwareSerial* cmdSerial = &Serial5;     // UART used to communicate with Cerebellum
HardwareSerial* logger = &Serial4;      // UART used to log
HardwareSerial* servoComm = &Serial1;   // UART used to communicate with the HerkuleX servos
HardwareSerial* printerComm = &Serial6;   // UART used to control the thermal printer

int n=1; //motor ID - verify your ID !!!!
void setup()  
{
  delay(2000);  //a delay to have time for serial monitor opening
  Serial.begin(115200);    // Open serial communications
  Serial.println("Begin");
  Herkulex.beginSerial(servoComm, 115200); //open serial port 1 
  Herkulex.reboot(n); //reboot first motor
  delay(500);   
  Herkulex.initialize(); //initialize motors
  delay(200);  
}

void loop(){
  Serial.println("Move Angle: -100 degrees");
  Herkulex.moveOneAngle(n, -100, 1000, LED_BLUE); //move motor with 300 speed  
  delay(1200);
  Serial.print("Get servo Angle:");
  Serial.println(Herkulex.getAngle(n));
  Serial.println("Move Angle: 100 degrees");
  Herkulex.moveOneAngle(n, 100, 1000, LED_BLUE); //move motor with 300 speed  
  delay(1200);
  Serial.print("Get servo Angle:");
  Serial.println(Herkulex.getAngle(n));
  
}
