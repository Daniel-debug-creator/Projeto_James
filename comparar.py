def comparar(enig, compa):
    letra_eng = list(enig.keys())
    porc_eng = list(enig.values())
    letra_por = list(compa.keys())
    porc_por = list(compa.values())
    delta = []
    for eng in porc_eng:
        for prob in porc_por:
            delta.append(abs(eng-prob))
        index = delta.index(min(delta))
        print(delta[index])
