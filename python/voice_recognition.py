import speech_recognition as sr

# Lista de estados do tempo válidos
CONDICOES_VALIDAS = [
    "sol",
    "chuva",
    "nublado",
    "nevoeiro",
    "trovoada",
    "vento",
    "granizo",
    "céu limpo",
    "seu limpo",
    "parcialmente nublado"
]

def ouvir_condicao():
    """
    Captura o input de voz do utilizador, valida o estado do tempo
    e retorna apenas valores válidos em minúsculas.
    """
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Diz o estado do tempo (ex: sol, chuva, nevoeiro):")
        audio = r.listen(source)

        try:
            texto = r.recognize_google(audio, language='pt-PT').lower()
            print("Reconhecido:", texto)

            # Verificação se o estado é válido
            if texto in CONDICOES_VALIDAS:
                return texto
            else:
                print(f"Estado do tempo ('{texto}') inválido.")
                print(f"Estados do tempo válidos: {CONDICOES_VALIDAS}")
                print("Tenta novamente.")

                return ouvir_condicao()

        except sr.UnknownValueError:
            print("Não percebi, tenta de novo.")
            return ouvir_condicao()

        except sr.RequestError:
            print("Erro no serviço de reconhecimento de voz.")
            return None
