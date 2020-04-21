#include <Wire.h>
#include <SoftwareSerial.h>
#include <Adafruit_MPL3115A2.h>
#include <Adafruit_LSM6DS33.h>

Adafruit_MPL3115A2 altimeter = Adafruit_MPL3115A2();
Adafruit_LSM6DS33 accelerometer;
SoftwareSerial radioSerial(5, 6);

void setup() {
  accelerometer.begin_I2C()
}

void loop() {
  float altitude = altimeter.getAltitude();

  sensors_event_t accel;
  sensors_event_t gyro;
  sensors_event_t temp;
  accelerometer.getEvent(&accel, &gyro, &temp);

  float data_points[7] = {
    accel.acceleration.x,
    accel.acceleration.y,
    accel.acceleration.z,
    gyro.gyro.x,
    gyro.gyro.y,
    gyro.gyro.z,
    altitude
  }

  for(i=0; i<7; i++) {
    radioSerial.print(String(data_points[i]))
    radioSerial.print(",")
  }
  radioSerial.println()
}
