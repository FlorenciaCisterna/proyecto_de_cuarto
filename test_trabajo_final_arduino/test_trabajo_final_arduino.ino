// Incluya la biblioteca MPU6050
#include <Wire.h>
#include <MPU6050.h>
#include "I2Cdev.h"
#include "Arduino.h"
#include "SoftwareSerial.h"
#include "DFRobotDFPlayerMini.h"

// Dirección I2C del MPU6050
const uint8_t MPU_ADDR = 0x68;
const char separator = ',';
// Objeto de la clase MPU6050
MPU6050 sensor;
int ax, ay, az;
// Pines analógicos de los sensores flex
#define FLEX_PIN_1 A6   //  pulgar
#define FLEX_PIN_2 A3  //   indice
#define FLEX_PIN_3 A2  //medio
#define FLEX_PIN_4 A1  // corazon 
#define FLEX_PIN_5 A0  // meñique

void setup() {
  // Inicialice la comunicación serial a una velocidad de 9600 baudios
  Serial.begin(9600);
  // Inicialice la comunicación I2C
  Wire.begin();
  // Inicialice el MPU6050
  sensor.initialize();
  //inicializa audio
}

void loop() {
  // Lea los valores de los sensores flex
  int flex1 = analogRead(FLEX_PIN_1);
  int flex2 = analogRead(FLEX_PIN_2);
  int flex3 = analogRead(FLEX_PIN_3);
  int flex4 = analogRead(FLEX_PIN_4);
  int flex5 = analogRead(FLEX_PIN_5);
  int pulsador = digitalRead(12);
  // Lea los valores del giroscopio
  //int16_t gyroX, gyroY, gyroZ;
  int ax, ay, az;
 
  sensor.getAcceleration(&ax,&ay,&az);
  float accel_ang_x=atan(ax/sqrt(pow(ay,2) + pow(az,2)))*(180.0/3.14);
  float accel_ang_y=atan(ay/sqrt(pow(ax,2) + pow(az,2)))*(180.0/3.14);
  float accel_ang_z=atan(az/sqrt(pow(az,2) + pow(az,2)))*(180.0/3.14);
  //Mostrar los angulos separadas por un [tab]
 
  // Imprima los valores en una tabla en la consola serial
  //Serial.print("pulgar\tindice\tmedio\tcorazon\tmeñique\tacelZ\n");
    Serial.print(",");
    Serial.print(flex1);
    Serial.print(",");
    Serial.print(flex2);
    Serial.print(",");
    Serial.print(flex3);
    Serial.print(",");
    Serial.print(flex4);
    Serial.print(",");
    Serial.print(flex5);
    Serial.print(",");
    Serial.print(accel_ang_x);
    Serial.print(",");
    Serial.print(accel_ang_y);
    Serial.print(",");
    Serial.print(accel_ang_z);
    Serial.print(",");
    
  Serial.println(); // End of one data row
  delay(50);
    
 
    }







