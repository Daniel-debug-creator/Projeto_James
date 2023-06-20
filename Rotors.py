
def rotor(letra, dic_de_substituicao, giro):
    letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    final = ''
    pos = letras.index(letra)
    pg = (pos + giro) % 26
    print(pg % 26)
    new_pos = pg
    final += letras[new_pos]
    #print(f'giro {final}')
    texto_rotor = ''
    for i in final:
        texto_rotor += i.replace(i, dic_de_substituicao[i])
    #print(texto_rotor, 'subs')

    return texto_rotor

def rotor_inverso(letra_inv, dic_substituicao, giro):
    letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
              't', 'u', 'v', 'w', 'x', 'y', 'z']

    letra_sub = dic_substituicao[letra_inv]

    final = ''
    pos = letras.index(letra_sub)
    pg = pos - giro
    new_pos = pos - giro
    final += letras[new_pos]
    #print(f'giro {final}')
    texto_rotor = ''

    #print(final, 'subs')

    return final

def rotores(texto, rotor_1, rotor_2, rotor_3, giro1, giro2, giro3, dic_sub_meio):
    texto_quase_final = ''
    for letra in texto:
        print(letra)
        if giro1 + 1 <= 25:
            giro1 += 1
        else:
            giro1 = 0
            if giro2 <= 25:
                giro2 += 1
            else:
                giro2 = 0
                if giro3 <= 25:
                    giro3 += 1
                else:
                    giro3 = 0

        letra1 = rotor(letra, rotor_1, giro1)
        letra2 = rotor(letra1, rotor_2, giro2)
        letra3 = rotor(letra2, rotor_3, giro3)

        letra4 = dic_sub_meio[letra3]
        #print('reflector', letra4)
        letra5 = rotor_inverso(letra4, rotor_3, giro3)
        letra6 = rotor_inverso(letra5, rotor_2, giro2)
        letra7 = rotor_inverso(letra6, rotor_1, giro1)

        texto_quase_final += letra7

    return texto_quase_final