
from formatar import formata
from cesar import cesar
from conta import contar
from comparar import comparar

texto = """Mesmo com o desenvolvimento da Inteligência Artificial para construir códigos praticamente impossíveis de serem quebrados, a sofisticação da máquina Enigma é motivo de curiosidade para os especialistas da área. Fabricado a partir da década de 1920 na Alemanha, o equipamento contava com um teclado e um conjunto de discos rotativos conhecidos como rotores: ao apertar uma tecla, uma corrente elétrica circulava no interior da Enigma e fazia os rotores funcionarem de modo constante. Com isso, eram  criadas diferentes possibilidades de codificação: as chaves com as palavras cifradas eram trocadas diariamente e, para desvendar a mensagem, era necessário um caderno e o uso de outra máquina Enigma para desembaralhar o conteúdo transmitido a partir de telégrafos.

Com a crescente ameaça do nazifascismo na Europa, um grupo de cientistas contratados pelo serviço de inteligência britânico foi reunido durante a Segunda Guerra Mundial para desvendar o código militar alemão. Em uma mansão vitoriana na cidade de Bletchley, o matemático Alan Turing liderou o trabalho da produção de uma máquina conhecida como "a bomba". 

Tal instrumento identificava pontos fracos da codificação da Enigma e foi responsável por revelar a posição dos submarinos alemães e outras informações sensíveis do Exército nazista. Com as diversas informações interceptadas, o grupo também pode ter colaborado para encurtar a duração da guerra.

Veja a reconstrução em 3D da máquina Enigma realizada pela Universidade de Manchester:


Curte o conteúdo da GALILEU? Tem mais de onde ele veio: baixe o app Globo Mais para ler reportagens exclusivas e ficar por dentro de todas as publicações da Editora Globo. Você também pode assinar a revista, a partir de R$ 4,90, e ter acesso às nossas edições."""

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

if frequencia:
    print(f"A letra '{letra}' tem a frequência de: {frequencia}%")
else:
    print(f"A letra '{letra}' não está no dicionário.")

texto_com_numeros = "Olá, eu tenho 25 anos."
texto_sem_numeros = formata(texto_com_numeros)

ene = contar(cesar(formata(texto), 2))

comparar(ene, frequencias)
