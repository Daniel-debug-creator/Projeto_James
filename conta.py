def contar(texto):
    string = texto.replace(" ", "")
    total = len(string)
    print(total)
    dicionario = {}

    for letra in string:
        a = string.count(letra)
        dicionario.update({letra: ((a / total) * 100)})
    return dict(sorted(dicionario.items(), key=lambda x: x[1], reverse=True))