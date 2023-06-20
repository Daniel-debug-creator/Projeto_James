# código que simula o que ocorre no rotor
def rotor(letra, dic_de_substituicao, giro):
    #simula o giro que ocorre no rotor, "girando as letras"
    letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    final = ''
    pos = letras.index(letra)
    pg = (pos + giro) % 26
    new_pos = pg
    final += letras[new_pos]

    # simula a substituição que ocorre dentro do rotor
    texto_rotor = dic_de_substituicao[final]

    # retorna o final
    return texto_rotor


def rotor_inverso(letra_inv, dic_substituicao, giro):
    # a mesma coisa que ocorre no rotor, mas como isso é a volta tem que substituir primeiro e depois gira

    # substitui
    letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
              't', 'u', 'v', 'w', 'x', 'y', 'z']
    letra_sub = dic_substituicao[letra_inv]

    final = ''
    # responsavel pela parte que gira
    pos = letras.index(letra_sub)
    new_pos = pos - giro
    final += letras[new_pos]

    return final


def rotores(texto, rotor_1, rotor_2, rotor_3, giro1, giro2, giro3, dic_sub_meio):
    # simula o giro de varios rotores juntos

    # divide o texto por letra já que na maquina era feita uma por fez
    texto_quase_final = ''
    for letra in texto:
        print(letra)

        # simula o giro que ocorre quando uma tecla é apertada
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

        # giro dos três motores
        letra1 = rotor(letra, rotor_1, giro1)
        letra2 = rotor(letra1, rotor_2, giro2)
        letra3 = rotor(letra2, rotor_3, giro3)

        #reflector
        letra4 = dic_sub_meio[letra3]

        #giro dos três motores na volta
        letra5 = rotor_inverso(letra4, rotor_3, giro3)
        letra6 = rotor_inverso(letra5, rotor_2, giro2)
        letra7 = rotor_inverso(letra6, rotor_1, giro1)

        texto_quase_final += letra7

    return texto_quase_final
