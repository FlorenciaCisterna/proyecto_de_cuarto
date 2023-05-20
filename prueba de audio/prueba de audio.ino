
#include <arduino.h>
#include <SoftwareSerial.h>
#include <DFPlayer_Mini_Mp3.h>
SoftwareSerial DFPlayerSerial(10, 11); // RX, TX
/*
mp3_play();      //start play
mp3_play(1);   //play "mp3/0005.mp3"
mp3_pause();
mp3_stop();
mp3_next();      
mp3_prev();
mp3_set_volume(20);   //0~30
mp3_set_EQ();   //0~5
void mp3_single_loop(boolean state);   //set single loop
void mp3_random_play();
*/
void setup()
{
   Serial.begin(9600);
   DFPlayerSerial.begin(9600);
   mp3_set_serial(DFPlayerSerial);
   mp3_set_volume(20);
}
void loop()
{
   mp3_play(5);
   delay(300);
   mp3_next();
   delay(300);
   mp3_play(2);
   delay(300);
   mp3_next();
   delay(300);   
   mp3_play(3);
   delay(300);
    mp3_next();
   delay(300);
   mp3_play(4);
   delay(300);
    mp3_next();
   delay(300);
  
   Serial.print(" listo ");
 

}