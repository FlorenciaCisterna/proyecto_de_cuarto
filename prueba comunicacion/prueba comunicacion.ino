const int ledPin = 12; // Pin del LED

void setup() {
  pinMode(ledPin, OUTPUT); // Configura el pin del LED como salida
  Serial.begin(9600); // Inicia la comunicación serial a 9600 baudios
}

void loop() {
  if (Serial.available()>0) {
    {    
    char option=Serial.read();// Lee el número entero recibido desde Python
    
    if (option >= '1' && option <= '5') {
      digitalWrite(ledPin, HIGH); // Enciende el LED si el número está entre 1 y 5
    } else {
      digitalWrite(ledPin, LOW); // Apaga el LED si el número no está entre 1 y 5
    }
  }
}
}
