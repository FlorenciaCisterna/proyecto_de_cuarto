// Librerias I2C para controlar el mpu6050
// la libreria MPU6050.h necesita I2Cdev.h, I2Cdev.h necesita Wire.h
#include "I2Cdev.h"
#include "MPU6050.h"
#include "Wire.h"
// La dirección del MPU6050 puede ser 0x68 o 0x69, dependiendo
// del estado de AD0. Si no se especifica, 0x68 estará implicito
MPU6050 sensor;
// Valores RAW (sin procesar) del acelerometro en los ejes x,y,z
int ax, ay, az;
int gx, gy, gz;
void setup() {
 Serial.begin(57600); //Iniciando puerto serial
 Wire.begin(); //Iniciando I2C
 sensor.initialize(); //Iniciando el sensor
 if (sensor.testConnection()) Serial.println("Sensor iniciado correctamente");
 else Serial.println("Error al iniciar el sensor");
}
void loop() {
 // Leer las aceleraciones
 sensor.getAcceleration(&ax, &ay, &az);
 sensor.getRotation(&gx, &gy, &gz);
 //Calcular los angulos de inclinacion:
 float accel_ang_x=atan(ax/sqrt(pow(ay,2) + pow(az,2)))*(180.0/3.14);
 float accel_ang_y=atan(ay/sqrt(pow(ax,2) + pow(az,2)))*(180.0/3.14);
 float accel_ang_z = atan(sqrt(pow(ay, 2) + pow(ax, 2)) / az) * (180.0 / 3.14);
 
 //Mostrar los angulos separadas por un [tab]
 Serial.print(" X: ");
 Serial.print(accel_ang_x);
 Serial.print("\t"); 
 Serial.print(" Y:");
 Serial.print(accel_ang_y);
 Serial.print("\t");
 Serial.print(" Z:");
 Serial.print(accel_ang_z);
 Serial.print("\t");
 Serial.print("ANG X: ");
 Serial.print(gx);
 Serial.print("\t"); 
 Serial.print("ANG Y:");
 Serial.print(gy);
 Serial.print("\t");
 Serial.print("ANG Z:");
 Serial.print(gz);
 Serial.print("\t");
 Serial.print("\n");
 delay(1000);
} 
