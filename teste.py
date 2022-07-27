import  wikipedia
pesquisa = str(input("pesquisar por >>> "))
wikipedia.set_lang(prefix= 'pt')
if('pesquisar por' in pesquisa):
    pesquisa = pesquisa.replace('pesquisar por','')
    print(pesquisa)
    resultado_pesquisa = wikipedia.summary(pesquisa)
    resultado_pesquisa = resultado_pesquisa.replace('(',' ')
    resultado_pesquisa = resultado_pesquisa.replace(')',' ')
    #traduzir = Translator(from_lang="pt-br", to_lang="english")
    #resultado_traduzido = traduzir.translate(resultado_pesquisa)
    print(resultado_pesquisa)