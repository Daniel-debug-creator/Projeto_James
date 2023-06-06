def substituir_no_texto(texto, substitui):
    texto_velho = texto
    novo = []
    for letra in texto_velho:
        if letra.isalpha():
            novo.append(substitui[letra])
        else:
            novo.append(letra)
    text_novo = ''
    return text_novo.join(novo)




