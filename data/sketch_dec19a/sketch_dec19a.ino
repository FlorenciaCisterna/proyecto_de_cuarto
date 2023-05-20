// C++ code
//

 const int thumb=A0;
 const int index=A1;
 const int middle=A2;
 const int ring=A3;
 const int pinky=A4;
 int thumb_v;
 int index_v;
 int middle_v;
 int ring_v;
 int pinky_v;
  
void setup()
{
 Serial.begin(9600);
}

void loop()
{
  thumb_v=analogRead(thumb);
  index_v=analogRead(index);
  middle_v=analogRead(middle);
  ring_v=analogRead(ring);
  pinky_v=analogRead(pinky);
  

  Serial.print("Thumb: ");
  Serial.print(thumb_v);
  Serial.print(" ");

  Serial.print("Index: ");
  Serial.print(index_v);
  Serial.print(" ");

    Serial.print("Middle: ");
  Serial.print(middle_v);
  Serial.print(" ");

    Serial.print("Ring: ");
  Serial.print(ring_v);
  Serial.print(" ");

    Serial.print("Pinky: ");
  Serial.print(pinky_v);
  Serial.print(" ");
  delay(9000);
  
}