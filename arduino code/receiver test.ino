long startTime;

void setup() {
  Serial.begin(9600);
  startTime = millis();
}

void loop() {
  Serial.println(String(millis()-startTime) + ",123,");
  delay(1000);
}
