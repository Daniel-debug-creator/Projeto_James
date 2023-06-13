import random


def criar_dic():
    lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z']

    random.shuffle(lista)
    dic_de_substituicao = {}
    for i in range(0,13):
        x = str(lista.pop())
        y = str(lista.pop())
        dic_de_substituicao.update({x: y})
        dic_de_substituicao.update({y: x})
    return dic_de_substituicao