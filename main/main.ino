#include <Servo.h> // Use the built-in Servo library

Servo servo1; // create first servo object
Servo servo2; // create second servo object

void setup() {
  Serial.begin(9600);
  Serial.println("Dual Servo test starting...");
  // Attach servo1 to pin 10
  servo1.attach(10);
  // Attach servo2 to pin 11
  servo2.attach(11);
}

void loop() {
  // For continuous rotation servos:
  Serial.println("Servo1 at max speed CW, Servo2 at max speed CCW");
  servo1.write(0);   // servo1: maximum speed clockwise
  servo2.write(180); // servo2: maximum speed counterclockwise
  delay(1000);

  // Swap directions if needed for demonstration
  Serial.println("Servo1 at max speed CCW, Servo2 at max speed CW");
  servo1.write(180); // servo1: maximum speed counterclockwise
  servo2.write(0);   // servo2: maximum speed clockwise
  delay(1000);
}
