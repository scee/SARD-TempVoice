import serial
import time

ser = serial.Serial('COM5', 115200, timeout=2)
time.sleep(4)
ser.reset_input_buffer()

def ler_sensor():
    linha = ser.readline()
    if not linha:
        return None

    texto = linha.decode('utf-8', errors='ignore').strip()

    if texto.startswith("FF"):
        return texto

    return None
