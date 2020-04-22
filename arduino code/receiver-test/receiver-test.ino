long startTime;

void setup() {
  Serial.begin(9600);
  startTime = millis();
}

void loop() {
  Serial.println(String(millis()-startTime) + ",1,2,3,4,5,6,7,");
  delay(1000);
}
