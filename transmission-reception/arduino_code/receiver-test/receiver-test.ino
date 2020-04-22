#include <SoftwareSerial.h>

void setup() {
  Serial.begin(9600);
}

void loop() {
  Serial.println(String((float)millis()/1000) + ",1,2,3,4,5,6,7,");
  delay(1000);
}
