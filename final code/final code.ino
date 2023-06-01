// Incluya la biblioteca MPU6050
#include <Wire.h>
#include <MPU6050.h>
#include "Arduino.h"
#include "SoftwareSerial.h"
#include "DFRobotDFPlayerMini.h"

SoftwareSerial mySoftwareSerial(10, 11); // RX, TX
DFRobotDFPlayerMini myDFPlayer;
void printDetail(uint8_t type, int value);

const int ledPin = 12;
// Dirección I2C del MPU6050
const uint8_t MPU_ADDR = 0x68;
const char separator = ',';
// Objeto de la clase MPU6050
MPU6050 mpu;

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
  mpu.initialize();
  //inicializa audio
  pinMode(ledPin, OUTPUT);
  mySoftwareSerial.begin(9600);
  myDFPlayer.begin(mySoftwareSerial);
  myDFPlayer.volume(30);  //Set volume value. From 0 to 30
  
}

void loop() {
  // Lea los valores de los sensores flex
  int flex1 = analogRead(FLEX_PIN_1);
  int flex2 = analogRead(FLEX_PIN_2);
  int flex3 = analogRead(FLEX_PIN_3);
  int flex4 = analogRead(FLEX_PIN_4);
  int flex5 = analogRead(FLEX_PIN_5);

  // Lea los valores del giroscopio
  //int16_t gyroX, gyroY, gyroZ;
  int ax, ay, az;
 
  mpu.getAcceleration(&ax,&ay,&az);

  // Imprima los valores en una tabla en la consola serial
  //Serial.print("pulgar\tindice\tmedio\tcorazon\tmeñique\tacelZ\n");

  Serial.print(flex1);
  Serial.print("\t");
  Serial.print(flex2);
  Serial.print("\t");
  Serial.print(flex3);
  Serial.print("\t");
  Serial.print(flex4);
  Serial.print("\t");
  Serial.print(flex5);
  Serial.print("\t");
  Serial.print(az);
  Serial.print("\n");
  delay(100);

  if (Serial.available()>0) {
    {    
    char option=Serial.read();// Lee el número entero recibido desde Python
    
    if (option >= '1' && option <= '5') {
      digitalWrite(ledPin, HIGH); // Enciende el LED si el número está entre 1 y 5
      int valor = String(option).toInt();
      myDFPlayer.play(valor); 
       //Play the first mp3 
    } else {
      digitalWrite(ledPin, LOW); // Apaga el LED si el número no está entre 1 y 5
    }
  }
}


   }


