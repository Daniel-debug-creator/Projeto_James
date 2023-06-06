def contar(texto):
    string = texto.replace(" ", "")
    total = len(string)

    dicionario = {}

    for letra in string:
        if letra.isalpha():
            a = string.count(letra)
            dicionario.update({letra: ((a / total) * 100)})

    return dict(sorted(dicionario.items(), key=lambda x: x[1], reverse=True))