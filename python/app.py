from read_data import ler_sensor
from voice_recognition import ouvir_condicao
from update_file import guardar_registo, inicializar_csv
import time

inicializar_csv()
print("Sistema iniciado...")

while True:
    dados = ler_sensor()

    if dados:
        print("Dados do sensor:", dados)

        try:
            _, temperatura, humidade = dados.split(";")
            temperatura = float(temperatura)
            humidade = float(humidade)

            pressao = None  # ainda não tens sensor de pressão

            print("Fala agora...")
            condicao = ouvir_condicao()

            guardar_registo(temperatura, pressao, humidade, condicao)
            print("Registo guardado\n")

        except ValueError:
            print("Erro a processar os dados:", dados)

        time.sleep(3)
