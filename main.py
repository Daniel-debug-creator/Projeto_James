
from formatar import formata
from cesar import cesar
from conta import contar
from comparar import comparar
from comparar import comparar_linear
from substitui import substituir_no_texto

nome_arquivo = 'texto.txt'
try:
    with open(nome_arquivo, 'r') as arquivo:
        texto = arquivo.read()
        print("Conteúdo do arquivo:")
except FileNotFoundError:
    print("Arquivo não encontrado.")

frequencias = {
    'a': 14.63,
    'b': 1.04,
    'c': 3.88,
    'd': 4.99,
    'e': 12.57,
    'f': 1.02,
    'g': 1.30,
    'h': 1.28,
    'i': 6.18,
    'j': 0.40,
    'k': 0.02,
    'l': 2.78,
    'm': 4.74,
    'n': 5.05,
    'o': 10.73,
    'p': 2.52,
    'q': 1.20,
    'r': 6.53,
    's': 7.81,
    't': 4.34,
    'u': 4.63,
    'v': 1.67,
    'w': 0.01,
    'x': 0.21,
    'y': 0.01,
    'z': 0.47
}

# Exemplo de uso:
letra = 'a'
frequencia = frequencias.get(letra)



texto_com_numeros = "Olá, eu tenho 25 anos."
texto_sem_numeros = formata(texto_com_numeros)
forma = formata(texto)
ces = cesar(forma, 2)
ene = contar(ces)
resultado = comparar(ene, frequencias)
resultado2 = comparar_linear(ene, frequencias)

print(forma)
print(ces)
print(ene)
print(resultado)
print(resultado2)
print(substituir_no_texto(ces, resultado))
print(substituir_no_texto(ces, resultado2))


