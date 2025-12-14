import speech_recognition as sr

def ouvir_condicao():
    
    """
    Captura o input de voz do utilizador e retorna o texto em minúsculas.
    Repete se não for possível reconhecer.
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Diz o estado do tempo (ex: sol, chuva, nevoeiro):")
        audio = r.listen(source)
        try:
            texto = r.recognize_google(audio, language='pt-PT')
            print("Reconhecido:", texto)
            return texto.lower()
        except sr.UnknownValueError:
            print("Não percebi, tenta de novo.")
            return ouvir_condicao()
        except sr.RequestError:
            print("Erro no serviço de reconhecimento.")
            return None
