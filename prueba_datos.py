import serial
import time
ser = serial.Serial('COM5', 9600)  # Replace 'COM3' with the name of the serial port on your computer

audio= input("numero del 0-4: ")
ser.write(audio.encode())
time.sleep(0.1)
ser.close()