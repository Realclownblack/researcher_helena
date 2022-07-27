import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import os
import wikipedia
from wikipedia import WikipediaException


class Cerebro_Helena():
    def __init__(self,Asistente_name = 'Helena'):
        self.name_user = 'Pesquisador'
        self.Asistente_name = Asistente_name
        self.microfone = sr.Recognizer()
        self.iniciar = False
        self.incializar_programa()

    def Helena_ouvindo(self):
        self.contador = 0
        while (True):
            with sr.Microphone(device_index=0) as source:
                self.microfone.adjust_for_ambient_noise(source)
                self.audio = self.microfone.listen(source)
                try:
                    self.frase = self.microfone.recognize_google(self.audio, language='pt-BR')
                    print(f"{self.name_user} >>> " + self.frase)
                except sr.UnknownValueError:
                    self.contador += 1
                    if (self.iniciar == True):
                        self.Helena_falando(nome_audio="helena_nao_entedeu", audio="Não entendi,pode repetir")
                    else:
                        pass
                if (self.contador == 1):
                    True
                    self.contador -= 1
                elif (self.contador == 0):
                    return self.frase

    def Helena_falando(self,nome_audio,audio):
        self.tts = gTTS(text=audio, lang="pt-br")
        self.nome_audio = nome_audio
        self.audio_file = f'{self.nome_audio}.mp3'
        self.tts.save(self.audio_file)
        playsound(self.audio_file)
        print(f'{self.Asistente_name} >>> ', audio)
        os.remove(self.audio_file)

    def incializar_programa(self):
        self.comandos_para_ligar = ['helena iniciar','iniciar','helena pesquisar','helena quero saber','pesquisar']
        print("__" * 40)
        print("Helena Pesquisadora".center(80))
        print("--" * 40)
        while (True):
            self.comando_iniciar = self.Helena_ouvindo().lower()
            if self.comando_iniciar in self.comandos_para_ligar:
                while (True):
                    self.iniciar = True
                    self.Helena_falando(audio="o'que deseja pesquisar? ", nome_audio="helena_perguntando_oque_saber")
                    self.pesquisa_user = self.Helena_ouvindo()
                    self.Helena_pesquisando_dados(self.pesquisa_user)
            else:
                True

    def Helena_buscando(self,buscar_por):
        self.buscar_por = buscar_por
        wikipedia.set_lang(prefix='pt')
        try:
            self.resultado_pesquisa = wikipedia.summary(self.buscar_por)
            self.resultado_pesquisa = self.resultado_pesquisa.replace('(',' ')
            self.resultado_pesquisa = self.resultado_pesquisa.replace(')', ' ')
            self.Helena_falando(nome_audio="helena_pesquisou_por",audio=f"{self.resultado_pesquisa}")
            self.Helena_saindo()
        except WikipediaException:
            True

    def Helena_pesquisando_dados(self,pralavra_chave):
        if('pesquisar por' in pralavra_chave):
            pralavra_chave = pralavra_chave.replace('pesquisar por','')
            self.Helena_buscando(pralavra_chave)
        if('sair' in pralavra_chave):
            self.Helena_saindo()
        if(pralavra_chave == ''):
            self.Helena_falando(nome_audio="helena_nao_entendeu",audio='Não conseguir encontrar isso ')
            True
        True
    def Helena_saindo(self):
        if __name__ == '__main__':
            Cerebro_Helena()
if __name__ == '__main__':
    Cerebro_Helena()
