def comparar(enig, compa):

    letra_eng = list(enig.keys())
    porc_eng = list(enig.values())
    letra_por = list(compa.keys())
    porc_por = list(compa.values())
    resultado_lista = []
    resultado_tupla = {}
    for eng in porc_eng:
        delta = []
        for prob in porc_por:
            delta.append(abs(eng-prob))
        index = delta.index(min(delta))
        resultado_lista.append(letra_por[index])
    for n, c in enumerate(letra_eng):
        resultado_tupla[c] = resultado_lista[n]

    return resultado_tupla

def comparar_linear(enig, compa):

    letra_eng = list(enig.keys())
    porc_eng = list(enig.values())
    letra_por = list(compa.keys())
    porc_por = list(compa.values())

    resultado = {}
    compa_ord = sorted(compa.items(), key=lambda x: x[1], reverse=True)
    print(compa_ord)

    for c in range(0, len(enig)):
        resultado[list(enig.keys())[c]] = list(compa_ord)[c][0]
    return resultado





