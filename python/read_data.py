import serial
import time

ser = serial.Serial('COM6', 115200, timeout=2)
time.sleep(2)
ser.reset_input_buffer()

def ler_sensor():
    linha = ser.readline()
    if not linha:
        return None

    texto = linha.decode('utf-8', errors='ignore').strip()

    if texto.startswith("FF"):
        return texto

    return None
