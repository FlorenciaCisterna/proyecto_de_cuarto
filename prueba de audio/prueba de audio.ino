#include <arduino.h>
#include <SoftwareSerial.h>
#include <DFPlayer_Mini_Mp3.h>

SoftwareSerial DFPlayerSerial(10, 11); // RX, TX
void setup()
{
   Serial.begin(9600);
   DFPlayerSerial.begin(9600);
   mp3_set_serial(DFPlayerSerial);
   mp3_set_volume(30);

   // Reproduce el archivo "0001.mp3"
   mp3_play(1);
}

void loop()
{
   // No es necesario agregar más código al bucle loop
}
