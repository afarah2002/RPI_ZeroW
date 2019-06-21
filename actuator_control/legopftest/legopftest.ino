// Motor control digital output pins defined as global constants
const int controlPin1A = 2;                
const int controlPin2A = 5;                 
const int ENablePin = 9;                   
// Servo control digital output pins defined as global constants 
const int controlPin3A = 6;              
const int controlPin4A = 8;                  
const int servoENablePin = 3;  
        
// Motor control global variables: 
int motorSpeed = 0;                          // Motor speed 0..255
int motorDirection = 1;                      // Forward (1) or reverse (0)
// Servo control global variables:
int steering = 0;                            // Servo position 0..255
int steeringDirection = 0;                   // Left (0) and Right (1)

void setup() {
  // put your setup code here, to run once:
  //other stuff....
 
  // Declare digital output pins:
  pinMode(controlPin1A, OUTPUT);      // 1A
  pinMode(controlPin2A, OUTPUT);      // 2A
  pinMode(ENablePin, OUTPUT);         // EN1,2
  pinMode(controlPin3A, OUTPUT);      // 3A
  pinMode(controlPin4A, OUTPUT);      // 4A
  pinMode(servoENablePin, OUTPUT);    // EN3,4
 
  digitalWrite(ENablePin, HIGH);       // motor off
//  digitalWrite(servoENablePin, LOW);  // steering centered

}

void loop() {
  // put your main code here, to run repeatedly:

    digitalWrite(controlPin1A, HIGH);

    digitalWrite(controlPin2A, LOW);

}
