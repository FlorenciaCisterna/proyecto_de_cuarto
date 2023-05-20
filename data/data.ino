#include <Wire.h>
#include <MPU6050.h>
#include "I2Cdev.h"

const int thumb=A4;
const int index=A3;
const int middle=A2;
const int heart=A1;
const int pinky=A0;

int thumb_v;
int index_v;
int middle_v;
int heart_v;
int pinky_v;
int ax, ay, az;
int gx, gy, gz;



  
void setup()
{
 
  Serial.begin(57600);    //Iniciando puerto serial
  Wire.begin();           //Iniciando I2C  
  sensor.initialize();    //Iniciando el sensor

  if (sensor.testConnection()) Serial.println("Sensor iniciado correctamente");
  else Serial.println("Error al iniciar el sensor");
}

void loop()
{
  thumb_v=analogRead(thumb);
  index_v=analogRead(index);
  middle_v=analogRead(middle);
  heart_v=analogRead(heart);
  pinky_v=analogRead(pinky);

  Serial.print("thumb: ");
  Serial.print(thumb_v); 
  Serial.print(" ");
  
  Serial.print("index: ");
  Serial.print(index_v); 
  Serial.print(" ");
  
  Serial.print("middle: ");
  Serial.print(middle_v); 
  Serial.print(" ");

  Serial.print("heart: ");
  Serial.print(heart_v); 
  Serial.print(" ");
  
  Serial.print("pinky: ");
  Serial.print(pinky_v); 
  Serial.print(" ");

  Serial.println("\n");
  delay(3000); 
  sensor.getAcceleration(&ax, &ay, &az);
  sensor.getRotation(&gx, &gy, &gz);

  //Mostrar las lecturas separadas por un [tab]
  Serial.print("a[x y z] g[x y z]:\t");
  Serial.print(ax); Serial.print("\t");
  Serial.print(ay); Serial.print("\t");
  Serial.print(az); Serial.print("\t");
  Serial.print(gx); Serial.print("\t");
  Serial.print(gy); Serial.print("\t");
  Serial.println(gz);

  delay(5000);
}


