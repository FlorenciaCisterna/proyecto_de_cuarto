#include <MPU6050.h>

// Incluya la biblioteca MPU6050
#include <Wire.h>

#include <MPU6050.h>
#include "Arduino.h"
#include "SoftwareSerial.h"
#include "DFRobotDFPlayerMini.h"

SoftwareSerial mySoftwareSerial(10, 11); // RX, TX
DFRobotDFPlayerMini myDFPlayer;
void printDetail(uint8_t type, int value);
const int verde = 2;
const int rojo= 3;
// Dirección I2C del MPU6050
const uint8_t MPU_ADDR = 0x68;
const char separator = ',';
// Objeto de la clase MPU6050
MPU6050 mpu;
int ax, ay, az;

// Pines analógicos de los sensores flex
#define FLEX_PIN_1 A6   //  pulgar
#define FLEX_PIN_2 A3  //   indice
#define FLEX_PIN_3 A2  //   medio
#define FLEX_PIN_4 A1  //   corazon 
#define FLEX_PIN_5 A0  //   meñique

void setup() {
  // Inicia la comunicación serial a una velocidad de 9600 baudios
  Serial.begin(9600);
   
  // Inicialice la comunicación I2C
  Wire.begin();
  pinMode(12, INPUT_PULLUP);  
  // Inicialice el MPU6050
  mpu.initialize();
  //inicializa audio
  pinMode(verde, OUTPUT);
  pinMode(rojo, OUTPUT);
  mySoftwareSerial.begin(9600);
  myDFPlayer.begin(mySoftwareSerial);
  myDFPlayer.volume(30);  //Set volume 
  
}

void loop() {
  // Lea los valores de los sensores flex
  int flex1 = analogRead(FLEX_PIN_1);
  int flex2 = analogRead(FLEX_PIN_2);
  int flex3 = analogRead(FLEX_PIN_3);
  int flex4 = analogRead(FLEX_PIN_4);
  int flex5 = analogRead(FLEX_PIN_5);
  int pulsador=0;
  pulsador = digitalRead(12);  
  //Valores del giroscopio
 
  int ax, ay, az;
 
  mpu.getAcceleration(&ax,&ay,&az);
  float accel_ang_x=atan(ax/sqrt(pow(ay,2) + pow(az,2)))*(180.0/3.14);
  float accel_ang_y=atan(ay/sqrt(pow(ax,2) + pow(az,2)))*(180.0/3.14);
  
  // Imprima los valores en una tabla en la consola serial
  //Serial.print("pulgar\tindice\tmedio\tcorazon\tmeñique\tacelZ\n");
  
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
    
    pulsador = digitalRead(12);   //lee el estado del botón
  if(pulsador==HIGH) {          //si el estado es pulsado
    Serial.print("0");         //se enciende el led
  }
  else{                                   //si el estado es no pulsado
    Serial.print("1") ;      //se enciende el led
  }  
    Serial.print("\n");
    delay(50);


  if (Serial.available()>0) {
    {    
    char option=Serial.read();// Lee el número entero recibido desde Python
    
    if (option >= '1' && option <= '5') {
      digitalWrite(verde, HIGH); 
      delay(100);
      digitalWrite(verde, LOW); 
      int valor = String(option).toInt();
      myDFPlayer.play(valor);
      
       //Play the first mp3 
    } else {
      digitalWrite(rojo, HIGH); // Apaga el LED si el número no está entre 1 y 5
      delay(100);
      digitalWrite(rojo, LOW); 
    }
    }
  }
}





