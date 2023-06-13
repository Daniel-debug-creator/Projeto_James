from Plugboard import plugboard
from Rotors import rotores
from Criar_dicionario import criar_dic
lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

dic_de_substituicao={'g': 'e', 'e': 'g', 'f': 'c', 'c': 'f', 'n': 'l', 'l': 'n', 'a': 'o', 'o': 'a', 'y': 'm', 'm': 'y', 't': 's', 's': 't', 'v': 'z', 'z': 'v', 'h': 'k', 'k': 'h', 'i': 'u', 'u': 'i', 'q': 'b', 'b': 'q', 'p': 'w', 'w': 'p', 'd': 'r', 'r': 'd', 'x': 'j', 'j': 'x'}

letra_crip_1 = plugboard('a', dic_de_substituicao)

rotor1 = {'g': 'f', 'f': 'g', 'l': 'q', 'q': 'l', 'i': 'y', 'y': 'i', 'm': 'b', 'b': 'm', 'w': 'k', 'k': 'w', 'r': 'e', 'e': 'r', 'h': 'd', 'd': 'h', 'j': 'c', 'c': 'j', 'p': 'u', 'u': 'p', 'n': 't', 't': 'n', 's': 'x', 'x': 's', 'z': 'v', 'v': 'z', 'o': 'a', 'a': 'o'}
rotor2 = {'v': 'g', 'g': 'v', 'b': 'j', 'j': 'b', 'm': 's', 's': 'm', 'c': 'i', 'i': 'c', 'k': 'z', 'z': 'k', 'r': 'u', 'u': 'r', 'e': 'y', 'y': 'e', 'p': 'x', 'x': 'p', 'o': 'd', 'd': 'o', 't': 'n', 'n': 't', 'l': 'q', 'q': 'l', 'a': 'h', 'h': 'a', 'f': 'w', 'w': 'f'}
rotor3 = {'j': 'a', 'a': 'j', 'b': 'm', 'm': 'b', 't': 'f', 'f': 't', 'w': 'e', 'e': 'w', 'n': 's', 's': 'n', 'v': 'p', 'p': 'v', 'y': 'g', 'g': 'y', 'l': 'h', 'h': 'l', 'k': 'r', 'r': 'k', 'q': 'c', 'c': 'q', 'i': 'u', 'u': 'i', 'd': 'o', 'o': 'd', 'x': 'z', 'z': 'x'}
refletor = {'v': 'e', 'e': 'v', 'c': 'j', 'j': 'c', 'x': 'y', 'y': 'x', 'b': 'w', 'w': 'b', 'o': 'f', 'f': 'o', 's': 'a', 'a': 's', 'u': 'r', 'r': 'u', 'h': 'k', 'k': 'h', 'l': 'd', 'd': 'l', 'n': 'g', 'g': 'n', 'z': 'i', 'i': 'z', 'q': 'm', 'm': 'q', 'p': 't', 't': 'p'}
print(letra_crip_1)

letra_crip_2 = rotores(letra_crip_1, rotor1, rotor2, rotor3, 0, 0, 0, refletor)
print(letra_crip_2)
letra_crip_final = plugboard(letra_crip_2, dic_de_substituicao)
print(letra_crip_final)

