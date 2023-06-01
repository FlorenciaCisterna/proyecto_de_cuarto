import serial
import time
arduino_port = 'COM6'  # Cambia esto al puerto serial correcto en tu computadora
baud_rate = 9600

# Abre la comunicación serial con Arduino
ser = serial.Serial(arduino_port, baud_rate, timeout=1)
time.sleep(2)
# Envía un número entero a Arduino
ser.write(b'5')
ser.close()
