#include <SoftwareSerial.h>

SoftwareSerial radioSerial(7, 8);

void setup() {
  Serial.begin(9600);
  radioSerial.begin(9600);
}

void loop() {
  while(radioSerial.available()) {
    Serial.print(radioSerial.read());
  }
}
