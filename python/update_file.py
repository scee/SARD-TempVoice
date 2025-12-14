import csv
from datetime import datetime

CSV_FILE = 'registos.csv'


def inicializar_csv():
    try:
        with open(CSV_FILE, 'x', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Timestamp', 'Temperatura', 'Pressao', 'Humidade', 'Condicao'])
    except FileExistsError:
        pass  # já existe

def guardar_registo(temperatura, pressao, humidade, condicao):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(CSV_FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([
            timestamp,
            temperatura,
            pressao if pressao is not None else "",
            humidade,
            condicao
        ])
