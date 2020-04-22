#include <Wire.h>
#include <SoftwareSerial.h>
#include <Adafruit_MPL3115A2.h>
#include <Adafruit_LSM6DS33.h>

#define DECIMAL_PLACES 4

Adafruit_MPL3115A2 altimeter = Adafruit_MPL3115A2();
Adafruit_LSM6DS33 accelerometer;
SoftwareSerial radioSerial(7, 8);

void setup() {
  accelerometer.begin_I2C();
  radioSerial.begin(9600);
}

void loop() {
  float altitude = altimeter.getAltitude();

  sensors_event_t accel;
  sensors_event_t gyro;
  sensors_event_t temp;
  accelerometer.getEvent(&accel, &gyro, &temp);

  float data_points[8] = {
    (float) millis() / 1000,
    altitude,
    accel.acceleration.x,
    accel.acceleration.y,
    accel.acceleration.z,
    gyro.gyro.x,
    gyro.gyro.y,
    gyro.gyro.z
  };

  for(int i=0; i<8; i++) {
    radioSerial.print(data_points[i], DECIMAL_PLACES);
    radioSerial.print(",");
  }
  radioSerial.println();
}
