from Plugboard import plugboard
from Rotors import rotores
from Rotors import rotor
from Rotors import rotor_inverso
from Criar_dicionario import criar_dic
lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# dicionario da substituição que vão ser realizadas no plug_board

dic_de_substituicao={'g': 'e', 'e': 'g', 'f': 'c', 'c': 'f', 'n': 'l', 'l': 'n', 'a': 'o', 'o': 'a', 'y': 'm', 'm': 'y', 't': 's', 's': 't', 'v': 'z', 'z': 'v', 'h': 'k', 'k': 'h', 'i': 'u', 'u': 'i', 'q': 'b', 'b': 'q', 'p': 'w', 'w': 'p', 'd': 'r', 'r': 'd', 'x': 'j', 'j': 'x'}

# substituição que vai ser realizada no rotor1
rotor1 = {'g': 'f', 'f': 'g', 'l': 'q', 'q': 'l', 'i': 'y', 'y': 'i', 'm': 'b', 'b': 'm', 'w': 'k', 'k': 'w', 'r': 'e', 'e': 'r', 'h': 'd', 'd': 'h', 'j': 'c', 'c': 'j', 'p': 'u', 'u': 'p', 'n': 't', 't': 'n', 's': 'x', 'x': 's', 'z': 'v', 'v': 'z', 'o': 'a', 'a': 'o'}

# substituição que vai ser realizada no rotor2
rotor2 = {'v': 'g', 'g': 'v', 'b': 'j', 'j': 'b', 'm': 's', 's': 'm', 'c': 'i', 'i': 'c', 'k': 'z', 'z': 'k', 'r': 'u', 'u': 'r', 'e': 'y', 'y': 'e', 'p': 'x', 'x': 'p', 'o': 'd', 'd': 'o', 't': 'n', 'n': 't', 'l': 'q', 'q': 'l', 'a': 'h', 'h': 'a', 'f': 'w', 'w': 'f'}

# substituição que vai ser realizada no rotor3
rotor3 = {'j': 'a', 'a': 'j', 'b': 'm', 'm': 'b', 't': 'f', 'f': 't', 'w': 'e', 'e': 'w', 'n': 's', 's': 'n', 'v': 'p', 'p': 'v', 'y': 'g', 'g': 'y', 'l': 'h', 'h': 'l', 'k': 'r', 'r': 'k', 'q': 'c', 'c': 'q', 'i': 'u', 'u': 'i', 'd': 'o', 'o': 'd', 'x': 'z', 'z': 'x'}

# substituição que vai ser realizada na reflexão dos rotores
refletor = {'v': 'e', 'e': 'v', 'c': 'j', 'j': 'c', 'x': 'y', 'y': 'x', 'b': 'w', 'w': 'b', 'o': 'f', 'f': 'o', 's': 'a', 'a': 's', 'u': 'r', 'r': 'u', 'h': 'k', 'k': 'h', 'l': 'd', 'd': 'l', 'n': 'g', 'g': 'n', 'z': 'i', 'i': 'z', 'q': 'm', 'm': 'q', 'p': 't', 't': 'p'}


#realiza a substituição que o ocorre no plugboard
texto_crip_1 = plugboard('xphwf', dic_de_substituicao)

print(texto_crip_1)

# realiza as etapas dos rotores
texto_crip_2 = rotores(texto_crip_1, rotor1, rotor2, rotor3, 5, 5, 5, refletor)
#print(texto_crip_2)

# realiza as etapas dos plugboard na volta
texto_crip_final = plugboard(texto_crip_2, dic_de_substituicao)

#resultado
print(texto_crip_final)
