// Incluya la biblioteca MPU6050
#include <Wire.h>
#include <MPU6050.h>
#include <arduino.h>
#include <SoftwareSerial.h>
#include <DFPlayer_Mini_Mp3.h>
SoftwareSerial mp3Serial(10, 11); // RX, TX
String archivos[5] = {"0.mp3", "1.mp3", "2.mp3", "3.mp3", "4.mp3"};

// Dirección I2C del MPU6050
const uint8_t MPU_ADDR = 0x68;
const char separator = ',';
// Objeto de la clase MPU6050
MPU6050 mpu;

// Pines analógicos de los sensores flex
#define FLEX_PIN_1 A0   //  pulgar
#define FLEX_PIN_2 A1  //   indice
#define FLEX_PIN_3 A2  //medio
#define FLEX_PIN_4 A3  // corazon 
#define FLEX_PIN_5 A6  // meñique

void setup() {
  // Inicialice la comunicación serial a una velocidad de 9600 baudios
  Serial.begin(9600);

  // Inicialice la comunicación I2C
  Wire.begin();

  // Inicialice el MPU6050
  mpu.initialize();
  mp3Serial.begin(9600);
  mp3_set_volume(30);
  delay(500);  // Espera 500 ms para que el módulo se inicialice correctamente
  // Configura el módulo MP3-TF16P
  enviarComandoMP3("AT+MP3INIT");  // Inicializa el módulo MP3
  
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
  delay(1000);
  if (Serial.available() > 0) {
    // Lee los datos recibidos
    String dato = Serial.readString();

    // Convierte el dato en un número entero
    int numero = dato.toInt();

    // Verifica si el número es válido
    if (numero >= 0 && numero <= 4) {
      // Construye el comando para reproducir el archivo de audio correspondiente
      String comando = "AT+MP3PLAY=" + archivos[numero];

      // Envía el comando al módulo MP3-TF16P
      enviarComandoMP3(comando);
    }
  }
}

// Función para enviar comandos al módulo MP3-TF16P
void enviarComandoMP3(String comando) {
  mp3Serial.println(comando);
  delay(100);  // Espera 100 ms para recibir la respuesta
  while (mp3Serial.available()) {
    String respuesta = mp3Serial.readString();
    Serial.println(respuesta);  // Imprime la respuesta del módulo MP3-TF16P para depuración
  }
}

