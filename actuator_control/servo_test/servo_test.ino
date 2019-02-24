#include <Servo.h>
#include <stdlib.h>
#include <stdio.h>

 int servoPin = 9;
Servo Servo1;
void setup() {
  // put your setup code here, to run once:
  Servo1.attach(servoPin);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:

  if (Serial.available()) {    
    int angle = Serial.read();
    Serial.println(angle);
    Servo1.write(angle);
  }
  
}
