def plugboard(texto, dic_de_substituicao):
    texto_new = ''
    for i in texto:
        texto_new += i.replace(i, dic_de_substituicao[i])
    return texto_new