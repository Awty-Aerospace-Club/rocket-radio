void setup() {
  Serial.begin(9600);
}

void loop() {
  unsigned long startTime = micros();
  Serial.println("very, very, very, very, very, very long test string");
  while(!Serial.available()) {
    
  }
  Serial.read();
  unsigned int elapsedTime = micros() - startTime;
  Serial.println(elapsedTime);
}
